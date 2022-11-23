from antlr4 import InputStream, CommonTokenStream
from collections import deque
from .command import Command
from .command_error_listener import CommandErrorListener
from .exceptions.redirection_error import RedirectionError
from glob import glob
from .grammar.CommandLexer import CommandLexer
from .grammar.CommandParser import CommandParser
from .grammar.CommandParserVisitor import CommandParserVisitor
from .impl.call import Call
from .impl.pipe import Pipe
from .impl.seq import Seq
import re


class CommandVisitor(CommandParserVisitor):
    @classmethod
    def parse(cls, cmdline: str) -> Command:
        input_stream = InputStream(cmdline)
        lexer = CommandLexer(input_stream)
        common_token_stream = CommonTokenStream(lexer)
        parser = CommandParser(common_token_stream)

        parser.removeErrorListeners()
        parser.addErrorListener(CommandErrorListener.INSTANCE)

        tree = parser.cmdline()
        command = tree.accept(cls())
        return command

    def visitCmdline(self, ctx: CommandParser.CmdlineContext):
        return self.visit(ctx.command())

    def visitSeq(self, ctx: CommandParser.SeqContext):
        return Seq(self.visit(ctx.left), self.visit(ctx.right))

    def visitSinglePipe(self, ctx: CommandParser.SinglePipeContext):
        return Pipe(self.visit(ctx.left), self.visit(ctx.right))

    def visitNestedPipe(self, ctx: CommandParser.NestedPipeContext):
        return Pipe(self.visit(ctx.left), self.visit(ctx.right))

    def __new_io_files(self, redirect, i_file: str, o_file: str) -> tuple:
        if redirect.op.text == "<":
            if i_file is None:
                return self.visit(redirect), o_file
            else:
                raise RedirectionError("several input redirection files")
        else:
            if o_file is None:
                return i_file, self.visit(redirect)
            else:
                raise RedirectionError("several output redirection files")

    def visitCall(self, ctx: CommandParser.CallContext):
        i_file, o_file, arguments = None, None, self.visit(ctx.argument())

        for redirect in ctx.redirections:
            i_file, o_file = self.__new_io_files(redirect, i_file, o_file)

        for atom in ctx.atoms:
            if atom.redirection() is not None:
                redirect = atom.redirection()
                i_file, o_file = self.__new_io_files(redirect, i_file, o_file)
            else:
                arguments.extend(self.visit(atom.argument()))

        return Call(arguments[0], arguments[1:], i_file, o_file)

    def visitArgument(self, ctx: CommandParser.ArgumentContext):
        visited_elems = [self.visit(elem) for elem in ctx.elements]
        split_elems, glob_elems = "".join(visited_elems).split("\n"), list()
        is_globs, split_elem_index = [False] * len(split_elems), 0

        for elem, visited_elem in zip(ctx.elements, visited_elems):
            if hasattr(elem, "UNQUOTED") and "*" in visited_elem:
                is_globs[split_elem_index] = True
            else:
                split_elem_index += visited_elem.count("\n")

        for is_glob, split_elem in zip(is_globs, split_elems):
            if is_glob:
                glob_elem = glob(split_elem)

                if len(glob_elem) == 0:
                    glob_elems.append(split_elem)
                else:
                    glob_elems.extend(glob_elem)
            else:
                glob_elems.append(split_elem)

        return glob_elems

    def visitUnquoted(self, ctx: CommandParser.UnquotedContext):
        return ctx.getText()

    def visitRedirection(self, ctx: CommandParser.RedirectionContext):
        file_names = self.visit(ctx.argument())

        if len(file_names) != 1:
            raise RedirectionError("several redirection files")

        return file_names[0]

    def visitQuoted(self, ctx: CommandParser.QuotedContext):
        if ctx.backQuoted() is not None:
            return re.sub("[\t ]+", "\n", self.visit(ctx.backQuoted()).strip())

        return self.visitChildren(ctx)

    def visitSingleQuoted(self, ctx: CommandParser.SingleQuotedContext):
        return ctx.SQ_CONTENT().getText()

    def visitBackQuoted(self, ctx: CommandParser.BackQuotedContext):
        temp_out = deque()
        CommandVisitor.parse(ctx.BQ_CONTENT().getText()).eval(None, temp_out)
        return "".join(temp_out).replace("\n", " ")

    def visitDoubleQuoted(self, ctx: CommandParser.DoubleQuotedContext):
        return "".join(self.visit(element) for element in ctx.elements)

    def visitDqContent(self, ctx: CommandParser.DqContentContext):
        return ctx.getText()
