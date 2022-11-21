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

    def __split_and_glob(self, elems: list) -> list:
        visited_elems = [self.visit(elem) for elem in elems]
        split_elems = "".join(visited_elems).split("\n")
        glob_indexes, glob_index, glob_elems = set(), 0, list()

        for elem, visited_elem in zip(elems, visited_elems):
            if hasattr(elem, "UNQUOTED") and "*" in visited_elem:
                glob_indexes.add(glob_index)
            else:
                glob_index += visited_elem.count("\n")

        for index, split_elem in enumerate(split_elems):
            if index in glob_indexes:
                glob_elem = glob(split_elem)

                if len(glob_elem) == 0:
                    glob_elems.append(split_elem)
                else:
                    glob_elems.extend(glob_elem)
            else:
                glob_elems.append(split_elem)

        return glob_elems

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
        return self.__split_and_glob(ctx.elements)

    def visitUnquoted(self, ctx: CommandParser.UnquotedContext):
        return ctx.getText()

    def visitRedirection(self, ctx: CommandParser.RedirectionContext):
        return self.visit(ctx.argument())

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
