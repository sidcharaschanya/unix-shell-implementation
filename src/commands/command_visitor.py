from antlr4 import *
from collections import deque
from .command import Command
import glob
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
    def __get_glob_arguments(arguments: list, glob_indexes: list) -> list:
        glob_arguments = list()

        for index, argument in enumerate(arguments):
            if index in glob_indexes:
                glob_argument = glob.glob(argument)

                if len(glob_argument) == 0:
                    glob_arguments.append(argument)
                else:
                    glob_arguments.extend(glob_argument)
            else:
                glob_arguments.append(argument)

        return glob_arguments

    @staticmethod
    def __get_glob_indexes(visited_elements: list, elements: list) -> list:
        glob_indexes, argument_count = list(), 0

        for visited_element, element in zip(visited_elements, elements):
            if hasattr(element, "UNQUOTED") and "*" in visited_element:
                glob_indexes.append(argument_count)
            else:
                argument_count += visited_element.count("\n")

        return glob_indexes

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

        return CommandVisitor.__get_glob_arguments(
            "".join(visited_elements).split("\n"),
            CommandVisitor.__get_glob_indexes(visited_elements, ctx.elements)
        )

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
