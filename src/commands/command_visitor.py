from antlr4 import InputStream, CommonTokenStream
from collections import deque
from .command import Command
from glob import glob
from .grammar.CommandLexer import CommandLexer
from .grammar.CommandParser import CommandParser
from .grammar.CommandParserVisitor import CommandParserVisitor
from .impl.pipe import Pipe
from .impl.seq import Seq
import re


class CommandVisitor(CommandParserVisitor):
    @classmethod
    def convert(cls, cmdline: str) -> Command:
        input_stream = InputStream(cmdline)
        lexer = CommandLexer(input_stream)
        common_token_stream = CommonTokenStream(lexer)
        parser = CommandParser(common_token_stream)
        tree = parser.cmdline()
        command = tree.accept(cls())
        return command

    @staticmethod
    def __get_glob_indexes(elems: list, visited_elems: list) -> set:
        glob_indexes, arg_count = set(), 0

        for elem, visited_elem in zip(elems, visited_elems):
            if hasattr(elem, "UNQUOTED") and "*" in visited_elem:
                glob_indexes.add(arg_count)
            else:
                arg_count += visited_elem.count("\n")

        return glob_indexes

    @staticmethod
    def __get_glob_args(elems: list, visited_elems: list) -> list:
        glob_indexes = CommandVisitor.__get_glob_indexes(elems, visited_elems)
        args, glob_args = "".join(visited_elems).split("\n"), list()

        for index, arg in enumerate(args):
            if index in glob_indexes:
                glob_arg = glob(arg)

                if len(glob_arg) == 0:
                    glob_args.append(arg)
                else:
                    glob_args.extend(glob_arg)
            else:
                glob_args.append(arg)

        return glob_args

    def visitCmdline(self, ctx: CommandParser.CmdlineContext):
        return self.visit(ctx.command())

    def visitSeq(self, ctx: CommandParser.SeqContext):
        return Seq(self.visit(ctx.left), self.visit(ctx.right))

    def visitSinglePipe(self, ctx: CommandParser.SinglePipeContext):
        return Pipe(self.visit(ctx.left), self.visit(ctx.right))

    def visitNestedPipe(self, ctx: CommandParser.NestedPipeContext):
        return Pipe(self.visit(ctx.left), self.visit(ctx.right))

    def visitCall(self, ctx: CommandParser.CallContext):
        pass

    def visitArgument(self, ctx: CommandParser.ArgumentContext):
        visited_elements = [self.visit(element) for element in ctx.elements]
        return CommandVisitor.__get_glob_args(ctx.elements, visited_elements)

    def visitUnquoted(self, ctx: CommandParser.UnquotedContext):
        return ctx.getText()

    def visitInRedirection(self, ctx: CommandParser.InRedirectionContext):
        pass

    def visitOutRedirection(self, ctx: CommandParser.OutRedirectionContext):
        pass

    def visitQuoted(self, ctx: CommandParser.QuotedContext):
        if ctx.backQuoted() is not None:
            return re.sub("[\t ]+", "\n", self.visit(ctx.backQuoted()).strip())

        return self.visitChildren(ctx)

    def visitSingleQuoted(self, ctx: CommandParser.SingleQuotedContext):
        return ctx.SQ_CONTENT().getText()

    def visitBackQuoted(self, ctx: CommandParser.BackQuotedContext):
        temp_out = deque()
        CommandVisitor.convert(ctx.BQ_CONTENT().getText()).eval(None, temp_out)
        return "".join(temp_out).replace("\n", " ")

    def visitDoubleQuoted(self, ctx: CommandParser.DoubleQuotedContext):
        return "".join(self.visit(element) for element in ctx.elements)

    def visitDqContent(self, ctx: CommandParser.DqContentContext):
        return ctx.DQ_CONTENT().getText()
