# Generated from CommandParser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CommandParser import CommandParser
else:
    from CommandParser import CommandParser

# This class defines a complete generic visitor for a parse tree produced by CommandParser.

class CommandParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CommandParser#cmdline.
    def visitCmdline(self, ctx:CommandParser.CmdlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#callCommand.
    def visitCallCommand(self, ctx:CommandParser.CallCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#pipeCommand.
    def visitPipeCommand(self, ctx:CommandParser.PipeCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#seq.
    def visitSeq(self, ctx:CommandParser.SeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#singlePipe.
    def visitSinglePipe(self, ctx:CommandParser.SinglePipeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#nestedPipe.
    def visitNestedPipe(self, ctx:CommandParser.NestedPipeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#call.
    def visitCall(self, ctx:CommandParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#atom.
    def visitAtom(self, ctx:CommandParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#argument.
    def visitArgument(self, ctx:CommandParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#quotedArgElem.
    def visitQuotedArgElem(self, ctx:CommandParser.QuotedArgElemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#unquoted.
    def visitUnquoted(self, ctx:CommandParser.UnquotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#inRedirection.
    def visitInRedirection(self, ctx:CommandParser.InRedirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#outRedirection.
    def visitOutRedirection(self, ctx:CommandParser.OutRedirectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#quoted.
    def visitQuoted(self, ctx:CommandParser.QuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#singleQuoted.
    def visitSingleQuoted(self, ctx:CommandParser.SingleQuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#backQuoted.
    def visitBackQuoted(self, ctx:CommandParser.BackQuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#doubleQuoted.
    def visitDoubleQuoted(self, ctx:CommandParser.DoubleQuotedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#bqDqElem.
    def visitBqDqElem(self, ctx:CommandParser.BqDqElemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandParser#dqContent.
    def visitDqContent(self, ctx:CommandParser.DqContentContext):
        return self.visitChildren(ctx)



del CommandParser