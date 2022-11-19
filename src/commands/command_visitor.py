from .grammar.CommandParser import CommandParser
from .grammar.CommandParserVisitor import CommandParserVisitor
from .impl.pipe import Pipe
from .impl.seq import Seq


class CommandVisitor(CommandParserVisitor):
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
        return "".join(self.visit(content) for content in ctx.contents)

    def visitUnquoted(self, ctx: CommandParser.UnquotedContext):
        return ctx.UNQUOTED().getText()

    def visitInRedirection(self, ctx: CommandParser.InRedirectionContext):
        pass

    def visitOutRedirection(self, ctx: CommandParser.OutRedirectionContext):
        pass

    def visitSingleQuoted(self, ctx: CommandParser.SingleQuotedContext):
        return ctx.SQ_CONTENT().getText()

    def visitBackQuoted(self, ctx: CommandParser.BackQuotedContext):
        pass

    def visitDoubleQuoted(self, ctx: CommandParser.DoubleQuotedContext):
        return "".join(self.visit(content) for content in ctx.contents)

    def visitDqContent(self, ctx: CommandParser.DqContentContext):
        return ctx.DQ_CONTENT().getText()
