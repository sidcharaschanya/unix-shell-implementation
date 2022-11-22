# Generated from CommandParser.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,129,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,1,1,1,1,1,1,3,1,33,8,1,1,1,1,1,1,1,5,1,38,8,1,10,1,12,1,41,9,
        1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,51,8,2,10,2,12,2,54,9,2,1,
        3,3,3,57,8,3,1,3,1,3,1,3,5,3,62,8,3,10,3,12,3,65,9,3,1,3,1,3,1,3,
        5,3,70,8,3,10,3,12,3,73,9,3,1,3,3,3,76,8,3,1,4,1,4,3,4,80,8,4,1,
        5,4,5,83,8,5,11,5,12,5,84,1,6,1,6,3,6,89,8,6,1,7,1,7,3,7,93,8,7,
        1,7,1,7,1,7,3,7,98,8,7,1,7,3,7,101,8,7,1,8,1,8,1,8,3,8,106,8,8,1,
        9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,5,11,118,8,11,10,11,
        12,11,121,9,11,1,11,1,11,1,12,1,12,3,12,127,8,12,1,12,0,2,2,4,13,
        0,2,4,6,8,10,12,14,16,18,20,22,24,0,0,132,0,26,1,0,0,0,2,32,1,0,
        0,0,4,42,1,0,0,0,6,56,1,0,0,0,8,79,1,0,0,0,10,82,1,0,0,0,12,88,1,
        0,0,0,14,100,1,0,0,0,16,105,1,0,0,0,18,107,1,0,0,0,20,111,1,0,0,
        0,22,115,1,0,0,0,24,126,1,0,0,0,26,27,3,2,1,0,27,28,5,0,0,1,28,1,
        1,0,0,0,29,30,6,1,-1,0,30,33,3,4,2,0,31,33,3,6,3,0,32,29,1,0,0,0,
        32,31,1,0,0,0,33,39,1,0,0,0,34,35,10,2,0,0,35,36,5,4,0,0,36,38,3,
        2,1,3,37,34,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,
        3,1,0,0,0,41,39,1,0,0,0,42,43,6,2,-1,0,43,44,3,6,3,0,44,45,5,5,0,
        0,45,46,3,6,3,0,46,52,1,0,0,0,47,48,10,1,0,0,48,49,5,5,0,0,49,51,
        3,6,3,0,50,47,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,
        53,5,1,0,0,0,54,52,1,0,0,0,55,57,5,6,0,0,56,55,1,0,0,0,56,57,1,0,
        0,0,57,63,1,0,0,0,58,59,3,14,7,0,59,60,5,6,0,0,60,62,1,0,0,0,61,
        58,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,
        0,65,63,1,0,0,0,66,71,3,10,5,0,67,68,5,6,0,0,68,70,3,8,4,0,69,67,
        1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,75,1,0,0,0,
        73,71,1,0,0,0,74,76,5,6,0,0,75,74,1,0,0,0,75,76,1,0,0,0,76,7,1,0,
        0,0,77,80,3,14,7,0,78,80,3,10,5,0,79,77,1,0,0,0,79,78,1,0,0,0,80,
        9,1,0,0,0,81,83,3,12,6,0,82,81,1,0,0,0,83,84,1,0,0,0,84,82,1,0,0,
        0,84,85,1,0,0,0,85,11,1,0,0,0,86,89,3,16,8,0,87,89,5,7,0,0,88,86,
        1,0,0,0,88,87,1,0,0,0,89,13,1,0,0,0,90,92,5,8,0,0,91,93,5,6,0,0,
        92,91,1,0,0,0,92,93,1,0,0,0,93,94,1,0,0,0,94,101,3,10,5,0,95,97,
        5,9,0,0,96,98,5,6,0,0,97,96,1,0,0,0,97,98,1,0,0,0,98,99,1,0,0,0,
        99,101,3,10,5,0,100,90,1,0,0,0,100,95,1,0,0,0,101,15,1,0,0,0,102,
        106,3,18,9,0,103,106,3,22,11,0,104,106,3,20,10,0,105,102,1,0,0,0,
        105,103,1,0,0,0,105,104,1,0,0,0,106,17,1,0,0,0,107,108,5,1,0,0,108,
        109,5,10,0,0,109,110,5,1,0,0,110,19,1,0,0,0,111,112,5,2,0,0,112,
        113,5,11,0,0,113,114,5,2,0,0,114,21,1,0,0,0,115,119,5,3,0,0,116,
        118,3,24,12,0,117,116,1,0,0,0,118,121,1,0,0,0,119,117,1,0,0,0,119,
        120,1,0,0,0,120,122,1,0,0,0,121,119,1,0,0,0,122,123,5,3,0,0,123,
        23,1,0,0,0,124,127,3,20,10,0,125,127,5,12,0,0,126,124,1,0,0,0,126,
        125,1,0,0,0,127,25,1,0,0,0,16,32,39,52,56,63,71,75,79,84,88,92,97,
        100,105,119,126
    ]

class CommandParser ( Parser ):

    grammarFileName = "CommandParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "';'", "'|'", "<INVALID>", "<INVALID>", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "SQ", "BQ", "DQ", "SEQ", "PIPE", "WS", 
                      "UNQUOTED", "LT", "GT", "SQ_CONTENT", "BQ_CONTENT", 
                      "DQ_CONTENT" ]

    RULE_cmdline = 0
    RULE_command = 1
    RULE_pipe = 2
    RULE_call = 3
    RULE_atom = 4
    RULE_argument = 5
    RULE_argumentElement = 6
    RULE_redirection = 7
    RULE_quoted = 8
    RULE_singleQuoted = 9
    RULE_backQuoted = 10
    RULE_doubleQuoted = 11
    RULE_doubleQuotedElement = 12

    ruleNames =  [ "cmdline", "command", "pipe", "call", "atom", "argument", 
                   "argumentElement", "redirection", "quoted", "singleQuoted", 
                   "backQuoted", "doubleQuoted", "doubleQuotedElement" ]

    EOF = Token.EOF
    SQ=1
    BQ=2
    DQ=3
    SEQ=4
    PIPE=5
    WS=6
    UNQUOTED=7
    LT=8
    GT=9
    SQ_CONTENT=10
    BQ_CONTENT=11
    DQ_CONTENT=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CmdlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(CommandParser.CommandContext,0)


        def EOF(self):
            return self.getToken(CommandParser.EOF, 0)

        def getRuleIndex(self):
            return CommandParser.RULE_cmdline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmdline" ):
                return visitor.visitCmdline(self)
            else:
                return visitor.visitChildren(self)




    def cmdline(self):

        localctx = CommandParser.CmdlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_cmdline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.command(0)
            self.state = 27
            self.match(CommandParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandParser.RULE_command

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class CallCommandContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def call(self):
            return self.getTypedRuleContext(CommandParser.CallContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallCommand" ):
                return visitor.visitCallCommand(self)
            else:
                return visitor.visitChildren(self)


    class PipeCommandContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def pipe(self):
            return self.getTypedRuleContext(CommandParser.PipeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPipeCommand" ):
                return visitor.visitPipeCommand(self)
            else:
                return visitor.visitChildren(self)


    class SeqContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.CommandContext
            super().__init__(parser)
            self.left = None # CommandContext
            self.right = None # CommandContext
            self.copyFrom(ctx)

        def SEQ(self):
            return self.getToken(CommandParser.SEQ, 0)
        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.CommandContext)
            else:
                return self.getTypedRuleContext(CommandParser.CommandContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeq" ):
                return visitor.visitSeq(self)
            else:
                return visitor.visitChildren(self)



    def command(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CommandParser.CommandContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_command, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = CommandParser.PipeCommandContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 30
                self.pipe(0)
                pass

            elif la_ == 2:
                localctx = CommandParser.CallCommandContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 31
                self.call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CommandParser.SeqContext(self, CommandParser.CommandContext(self, _parentctx, _parentState))
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_command)
                    self.state = 34
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 35
                    self.match(CommandParser.SEQ)
                    self.state = 36
                    localctx.right = self.command(3) 
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PipeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandParser.RULE_pipe

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SinglePipeContext(PipeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.PipeContext
            super().__init__(parser)
            self.left = None # CallContext
            self.right = None # CallContext
            self.copyFrom(ctx)

        def PIPE(self):
            return self.getToken(CommandParser.PIPE, 0)
        def call(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.CallContext)
            else:
                return self.getTypedRuleContext(CommandParser.CallContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinglePipe" ):
                return visitor.visitSinglePipe(self)
            else:
                return visitor.visitChildren(self)


    class NestedPipeContext(PipeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.PipeContext
            super().__init__(parser)
            self.left = None # PipeContext
            self.right = None # CallContext
            self.copyFrom(ctx)

        def PIPE(self):
            return self.getToken(CommandParser.PIPE, 0)
        def pipe(self):
            return self.getTypedRuleContext(CommandParser.PipeContext,0)

        def call(self):
            return self.getTypedRuleContext(CommandParser.CallContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNestedPipe" ):
                return visitor.visitNestedPipe(self)
            else:
                return visitor.visitChildren(self)



    def pipe(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CommandParser.PipeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_pipe, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = CommandParser.SinglePipeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 43
            localctx.left = self.call()
            self.state = 44
            self.match(CommandParser.PIPE)
            self.state = 45
            localctx.right = self.call()
            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CommandParser.NestedPipeContext(self, CommandParser.PipeContext(self, _parentctx, _parentState))
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_pipe)
                    self.state = 47
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 48
                    self.match(CommandParser.PIPE)
                    self.state = 49
                    localctx.right = self.call() 
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._redirection = None # RedirectionContext
            self.redirections = list() # of RedirectionContexts
            self._atom = None # AtomContext
            self.atoms = list() # of AtomContexts

        def argument(self):
            return self.getTypedRuleContext(CommandParser.ArgumentContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParser.WS)
            else:
                return self.getToken(CommandParser.WS, i)

        def redirection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.RedirectionContext)
            else:
                return self.getTypedRuleContext(CommandParser.RedirectionContext,i)


        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.AtomContext)
            else:
                return self.getTypedRuleContext(CommandParser.AtomContext,i)


        def getRuleIndex(self):
            return CommandParser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = CommandParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 55
                self.match(CommandParser.WS)


            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8 or _la==9:
                self.state = 58
                localctx._redirection = self.redirection()
                localctx.redirections.append(localctx._redirection)
                self.state = 59
                self.match(CommandParser.WS)
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.argument()
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 67
                    self.match(CommandParser.WS)
                    self.state = 68
                    localctx._atom = self.atom()
                    localctx.atoms.append(localctx._atom) 
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 74
                self.match(CommandParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def redirection(self):
            return self.getTypedRuleContext(CommandParser.RedirectionContext,0)


        def argument(self):
            return self.getTypedRuleContext(CommandParser.ArgumentContext,0)


        def getRuleIndex(self):
            return CommandParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = CommandParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.redirection()
                pass
            elif token in [1, 2, 3, 7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.argument()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._argumentElement = None # ArgumentElementContext
            self.elements = list() # of ArgumentElementContexts

        def argumentElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.ArgumentElementContext)
            else:
                return self.getTypedRuleContext(CommandParser.ArgumentElementContext,i)


        def getRuleIndex(self):
            return CommandParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = CommandParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 81
                    localctx._argumentElement = self.argumentElement()
                    localctx.elements.append(localctx._argumentElement)

                else:
                    raise NoViableAltException(self)
                self.state = 84 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandParser.RULE_argumentElement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class QuotedArgElemContext(ArgumentElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.ArgumentElementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def quoted(self):
            return self.getTypedRuleContext(CommandParser.QuotedContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuotedArgElem" ):
                return visitor.visitQuotedArgElem(self)
            else:
                return visitor.visitChildren(self)


    class UnquotedContext(ArgumentElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.ArgumentElementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def UNQUOTED(self):
            return self.getToken(CommandParser.UNQUOTED, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnquoted" ):
                return visitor.visitUnquoted(self)
            else:
                return visitor.visitChildren(self)



    def argumentElement(self):

        localctx = CommandParser.ArgumentElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_argumentElement)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3]:
                localctx = CommandParser.QuotedArgElemContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.quoted()
                pass
            elif token in [7]:
                localctx = CommandParser.UnquotedContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(CommandParser.UNQUOTED)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RedirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def argument(self):
            return self.getTypedRuleContext(CommandParser.ArgumentContext,0)


        def LT(self):
            return self.getToken(CommandParser.LT, 0)

        def WS(self):
            return self.getToken(CommandParser.WS, 0)

        def GT(self):
            return self.getToken(CommandParser.GT, 0)

        def getRuleIndex(self):
            return CommandParser.RULE_redirection

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRedirection" ):
                return visitor.visitRedirection(self)
            else:
                return visitor.visitChildren(self)




    def redirection(self):

        localctx = CommandParser.RedirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_redirection)
        self._la = 0 # Token type
        try:
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                localctx.op = self.match(CommandParser.LT)
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 91
                    self.match(CommandParser.WS)


                self.state = 94
                self.argument()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                localctx.op = self.match(CommandParser.GT)
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==6:
                    self.state = 96
                    self.match(CommandParser.WS)


                self.state = 99
                self.argument()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleQuoted(self):
            return self.getTypedRuleContext(CommandParser.SingleQuotedContext,0)


        def doubleQuoted(self):
            return self.getTypedRuleContext(CommandParser.DoubleQuotedContext,0)


        def backQuoted(self):
            return self.getTypedRuleContext(CommandParser.BackQuotedContext,0)


        def getRuleIndex(self):
            return CommandParser.RULE_quoted

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuoted" ):
                return visitor.visitQuoted(self)
            else:
                return visitor.visitChildren(self)




    def quoted(self):

        localctx = CommandParser.QuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_quoted)
        try:
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.singleQuoted()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.doubleQuoted()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 104
                self.backQuoted()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleQuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQ(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParser.SQ)
            else:
                return self.getToken(CommandParser.SQ, i)

        def SQ_CONTENT(self):
            return self.getToken(CommandParser.SQ_CONTENT, 0)

        def getRuleIndex(self):
            return CommandParser.RULE_singleQuoted

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleQuoted" ):
                return visitor.visitSingleQuoted(self)
            else:
                return visitor.visitChildren(self)




    def singleQuoted(self):

        localctx = CommandParser.SingleQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_singleQuoted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(CommandParser.SQ)
            self.state = 108
            self.match(CommandParser.SQ_CONTENT)
            self.state = 109
            self.match(CommandParser.SQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BackQuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BQ(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParser.BQ)
            else:
                return self.getToken(CommandParser.BQ, i)

        def BQ_CONTENT(self):
            return self.getToken(CommandParser.BQ_CONTENT, 0)

        def getRuleIndex(self):
            return CommandParser.RULE_backQuoted

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBackQuoted" ):
                return visitor.visitBackQuoted(self)
            else:
                return visitor.visitChildren(self)




    def backQuoted(self):

        localctx = CommandParser.BackQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_backQuoted)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(CommandParser.BQ)
            self.state = 112
            self.match(CommandParser.BQ_CONTENT)
            self.state = 113
            self.match(CommandParser.BQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoubleQuotedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._doubleQuotedElement = None # DoubleQuotedElementContext
            self.elements = list() # of DoubleQuotedElementContexts

        def DQ(self, i:int=None):
            if i is None:
                return self.getTokens(CommandParser.DQ)
            else:
                return self.getToken(CommandParser.DQ, i)

        def doubleQuotedElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandParser.DoubleQuotedElementContext)
            else:
                return self.getTypedRuleContext(CommandParser.DoubleQuotedElementContext,i)


        def getRuleIndex(self):
            return CommandParser.RULE_doubleQuoted

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoubleQuoted" ):
                return visitor.visitDoubleQuoted(self)
            else:
                return visitor.visitChildren(self)




    def doubleQuoted(self):

        localctx = CommandParser.DoubleQuotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_doubleQuoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(CommandParser.DQ)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2 or _la==12:
                self.state = 116
                localctx._doubleQuotedElement = self.doubleQuotedElement()
                localctx.elements.append(localctx._doubleQuotedElement)
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 122
            self.match(CommandParser.DQ)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoubleQuotedElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandParser.RULE_doubleQuotedElement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DqContentContext(DoubleQuotedElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.DoubleQuotedElementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DQ_CONTENT(self):
            return self.getToken(CommandParser.DQ_CONTENT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDqContent" ):
                return visitor.visitDqContent(self)
            else:
                return visitor.visitChildren(self)


    class BqDqElemContext(DoubleQuotedElementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CommandParser.DoubleQuotedElementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def backQuoted(self):
            return self.getTypedRuleContext(CommandParser.BackQuotedContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBqDqElem" ):
                return visitor.visitBqDqElem(self)
            else:
                return visitor.visitChildren(self)



    def doubleQuotedElement(self):

        localctx = CommandParser.DoubleQuotedElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_doubleQuotedElement)
        try:
            self.state = 126
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = CommandParser.BqDqElemContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.backQuoted()
                pass
            elif token in [12]:
                localctx = CommandParser.DqContentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.match(CommandParser.DQ_CONTENT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.command_sempred
        self._predicates[2] = self.pipe_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def command_sempred(self, localctx:CommandContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def pipe_sempred(self, localctx:PipeContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




