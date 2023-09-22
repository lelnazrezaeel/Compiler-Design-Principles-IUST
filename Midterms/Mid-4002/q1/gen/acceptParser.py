# Generated from /home/loop/uni/compiler/q1/accept.g4 by ANTLR 4.10.1
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
        4,1,14,146,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,3,0,47,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,61,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,
        2,75,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,89,
        8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,103,8,4,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,117,8,5,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,128,8,6,1,7,1,7,1,8,1,8,1,9,
        1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,14,0,0,15,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,8,2,0,4,8,10,14,2,0,5,
        8,10,12,2,0,6,8,10,10,2,0,7,8,10,10,1,0,7,8,2,0,4,8,10,13,2,0,5,
        8,10,10,2,0,5,8,10,11,149,0,46,1,0,0,0,2,60,1,0,0,0,4,74,1,0,0,0,
        6,88,1,0,0,0,8,102,1,0,0,0,10,116,1,0,0,0,12,127,1,0,0,0,14,129,
        1,0,0,0,16,131,1,0,0,0,18,133,1,0,0,0,20,135,1,0,0,0,22,137,1,0,
        0,0,24,139,1,0,0,0,26,141,1,0,0,0,28,143,1,0,0,0,30,31,5,1,0,0,31,
        32,3,2,1,0,32,33,5,2,0,0,33,34,3,4,2,0,34,35,5,2,0,0,35,36,3,6,3,
        0,36,47,1,0,0,0,37,38,5,3,0,0,38,39,3,8,4,0,39,40,5,2,0,0,40,41,
        3,10,5,0,41,42,5,2,0,0,42,43,3,12,6,0,43,44,1,0,0,0,44,45,5,0,0,
        1,45,47,1,0,0,0,46,30,1,0,0,0,46,37,1,0,0,0,47,1,1,0,0,0,48,61,3,
        14,7,0,49,50,3,14,7,0,50,51,3,14,7,0,51,61,1,0,0,0,52,53,3,16,8,
        0,53,54,3,14,7,0,54,55,3,14,7,0,55,61,1,0,0,0,56,57,5,4,0,0,57,58,
        3,24,12,0,58,59,3,24,12,0,59,61,1,0,0,0,60,48,1,0,0,0,60,49,1,0,
        0,0,60,52,1,0,0,0,60,56,1,0,0,0,61,3,1,0,0,0,62,75,3,14,7,0,63,64,
        3,14,7,0,64,65,3,14,7,0,65,75,1,0,0,0,66,67,3,18,9,0,67,68,3,14,
        7,0,68,69,3,14,7,0,69,75,1,0,0,0,70,71,5,5,0,0,71,72,3,20,10,0,72,
        73,3,20,10,0,73,75,1,0,0,0,74,62,1,0,0,0,74,63,1,0,0,0,74,66,1,0,
        0,0,74,70,1,0,0,0,75,5,1,0,0,0,76,89,3,14,7,0,77,78,3,14,7,0,78,
        79,3,14,7,0,79,89,1,0,0,0,80,81,3,20,10,0,81,82,3,14,7,0,82,83,3,
        14,7,0,83,89,1,0,0,0,84,85,5,6,0,0,85,86,3,26,13,0,86,87,3,28,14,
        0,87,89,1,0,0,0,88,76,1,0,0,0,88,77,1,0,0,0,88,80,1,0,0,0,88,84,
        1,0,0,0,89,7,1,0,0,0,90,103,3,14,7,0,91,92,3,14,7,0,92,93,3,14,7,
        0,93,103,1,0,0,0,94,95,5,7,0,0,95,96,3,14,7,0,96,97,3,14,7,0,97,
        103,1,0,0,0,98,99,5,8,0,0,99,100,3,20,10,0,100,101,3,18,9,0,101,
        103,1,0,0,0,102,90,1,0,0,0,102,91,1,0,0,0,102,94,1,0,0,0,102,98,
        1,0,0,0,103,9,1,0,0,0,104,117,3,14,7,0,105,106,3,14,7,0,106,107,
        3,14,7,0,107,117,1,0,0,0,108,109,3,18,9,0,109,110,3,14,7,0,110,111,
        3,14,7,0,111,117,1,0,0,0,112,113,5,5,0,0,113,114,3,16,8,0,114,115,
        3,22,11,0,115,117,1,0,0,0,116,104,1,0,0,0,116,105,1,0,0,0,116,108,
        1,0,0,0,116,112,1,0,0,0,117,11,1,0,0,0,118,128,3,14,7,0,119,120,
        3,14,7,0,120,121,3,14,7,0,121,128,1,0,0,0,122,123,3,22,11,0,123,
        124,3,14,7,0,124,125,3,14,7,0,125,128,1,0,0,0,126,128,5,9,0,0,127,
        118,1,0,0,0,127,119,1,0,0,0,127,122,1,0,0,0,127,126,1,0,0,0,128,
        13,1,0,0,0,129,130,7,0,0,0,130,15,1,0,0,0,131,132,7,1,0,0,132,17,
        1,0,0,0,133,134,7,2,0,0,134,19,1,0,0,0,135,136,7,3,0,0,136,21,1,
        0,0,0,137,138,7,4,0,0,138,23,1,0,0,0,139,140,7,5,0,0,140,25,1,0,
        0,0,141,142,7,6,0,0,142,27,1,0,0,0,143,144,7,7,0,0,144,29,1,0,0,
        0,7,46,60,74,88,102,116,127
    ]

class acceptParser ( Parser ):

    grammarFileName = "accept.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'F1:'", "','", "'F2:'", "'7'", "'4'", 
                     "'3'", "'0'", "'1'", "'200'", "'2'", "'5'", "'6'", 
                     "'8'", "'9'" ]

    symbolicNames = [  ]

    RULE_compilationUnit = 0
    RULE_a = 1
    RULE_b = 2
    RULE_c = 3
    RULE_d = 4
    RULE_e = 5
    RULE_f = 6
    RULE_g = 7
    RULE_h = 8
    RULE_i = 9
    RULE_j = 10
    RULE_k = 11
    RULE_l = 12
    RULE_m = 13
    RULE_n = 14

    ruleNames =  [ "compilationUnit", "a", "b", "c", "d", "e", "f", "g", 
                   "h", "i", "j", "k", "l", "m", "n" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CompilationUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def a(self):
            return self.getTypedRuleContext(acceptParser.AContext,0)


        def b(self):
            return self.getTypedRuleContext(acceptParser.BContext,0)


        def c(self):
            return self.getTypedRuleContext(acceptParser.CContext,0)


        def EOF(self):
            return self.getToken(acceptParser.EOF, 0)

        def d(self):
            return self.getTypedRuleContext(acceptParser.DContext,0)


        def e(self):
            return self.getTypedRuleContext(acceptParser.EContext,0)


        def f(self):
            return self.getTypedRuleContext(acceptParser.FContext,0)


        def getRuleIndex(self):
            return acceptParser.RULE_compilationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilationUnit" ):
                listener.enterCompilationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilationUnit" ):
                listener.exitCompilationUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompilationUnit" ):
                return visitor.visitCompilationUnit(self)
            else:
                return visitor.visitChildren(self)




    def compilationUnit(self):

        localctx = acceptParser.CompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compilationUnit)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [acceptParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(acceptParser.T__0)
                self.state = 31
                self.a()
                self.state = 32
                self.match(acceptParser.T__1)
                self.state = 33
                self.b()
                self.state = 34
                self.match(acceptParser.T__1)
                self.state = 35
                self.c()
                pass
            elif token in [acceptParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.match(acceptParser.T__2)
                self.state = 38
                self.d()
                self.state = 39
                self.match(acceptParser.T__1)
                self.state = 40
                self.e()
                self.state = 41
                self.match(acceptParser.T__1)
                self.state = 42
                self.f()
                self.state = 44
                self.match(acceptParser.EOF)
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


    class AContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def g(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(acceptParser.GContext)
            else:
                return self.getTypedRuleContext(acceptParser.GContext,i)


        def h(self):
            return self.getTypedRuleContext(acceptParser.HContext,0)


        def l(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(acceptParser.LContext)
            else:
                return self.getTypedRuleContext(acceptParser.LContext,i)


        def getRuleIndex(self):
            return acceptParser.RULE_a

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterA" ):
                listener.enterA(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitA" ):
                listener.exitA(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA" ):
                return visitor.visitA(self)
            else:
                return visitor.visitChildren(self)




    def a(self):

        localctx = acceptParser.AContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_a)
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.g()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.g()
                self.state = 50
                self.g()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.h()
                self.state = 53
                self.g()
                self.state = 54
                self.g()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 56
                self.match(acceptParser.T__3)
                self.state = 57
                self.l()
                self.state = 58
                self.l()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def g(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(acceptParser.GContext)
            else:
                return self.getTypedRuleContext(acceptParser.GContext,i)


        def i(self):
            return self.getTypedRuleContext(acceptParser.IContext,0)


        def j(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(acceptParser.JContext)
            else:
                return self.getTypedRuleContext(acceptParser.JContext,i)


        def getRuleIndex(self):
            return acceptParser.RULE_b

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterB" ):
                listener.enterB(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitB" ):
                listener.exitB(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitB" ):
                return visitor.visitB(self)
            else:
                return visitor.visitChildren(self)




    def b(self):

        localctx = acceptParser.BContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_b)
        try:
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.g()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.g()
                self.state = 64
                self.g()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.i()
                self.state = 67
                self.g()
                self.state = 68
                self.g()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 70
                self.match(acceptParser.T__4)
                self.state = 71
                self.j()
                self.state = 72
                self.j()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def g(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(acceptParser.GContext)
            else:
                return self.getTypedRuleContext(acceptParser.GContext,i)


        def j(self):
            return self.getTypedRuleContext(acceptParser.JContext,0)


        def m(self):
            return self.getTypedRuleContext(acceptParser.MContext,0)


        def n(self):
            return self.getTypedRuleContext(acceptParser.NContext,0)


        def getRuleIndex(self):
            return acceptParser.RULE_c

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterC" ):
                listener.enterC(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitC" ):
                listener.exitC(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitC" ):
                return visitor.visitC(self)
            else:
                return visitor.visitChildren(self)




    def c(self):

        localctx = acceptParser.CContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_c)
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.g()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.g()
                self.state = 78
                self.g()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.j()
                self.state = 81
                self.g()
                self.state = 82
                self.g()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 84
                self.match(acceptParser.T__5)
                self.state = 85
                self.m()
                self.state = 86
                self.n()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def g(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(acceptParser.GContext)
            else:
                return self.getTypedRuleContext(acceptParser.GContext,i)


        def j(self):
            return self.getTypedRuleContext(acceptParser.JContext,0)


        def i(self):
            return self.getTypedRuleContext(acceptParser.IContext,0)


        def getRuleIndex(self):
            return acceptParser.RULE_d

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterD" ):
                listener.enterD(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitD" ):
                listener.exitD(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitD" ):
                return visitor.visitD(self)
            else:
                return visitor.visitChildren(self)




    def d(self):

        localctx = acceptParser.DContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_d)
        try:
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.g()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.g()
                self.state = 92
                self.g()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.match(acceptParser.T__6)
                self.state = 95
                self.g()
                self.state = 96
                self.g()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 98
                self.match(acceptParser.T__7)
                self.state = 99
                self.j()
                self.state = 100
                self.i()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def g(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(acceptParser.GContext)
            else:
                return self.getTypedRuleContext(acceptParser.GContext,i)


        def i(self):
            return self.getTypedRuleContext(acceptParser.IContext,0)


        def h(self):
            return self.getTypedRuleContext(acceptParser.HContext,0)


        def k(self):
            return self.getTypedRuleContext(acceptParser.KContext,0)


        def getRuleIndex(self):
            return acceptParser.RULE_e

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterE" ):
                listener.enterE(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitE" ):
                listener.exitE(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitE" ):
                return visitor.visitE(self)
            else:
                return visitor.visitChildren(self)




    def e(self):

        localctx = acceptParser.EContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_e)
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.g()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.g()
                self.state = 106
                self.g()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 108
                self.i()
                self.state = 109
                self.g()
                self.state = 110
                self.g()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 112
                self.match(acceptParser.T__4)
                self.state = 113
                self.h()
                self.state = 114
                self.k()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def g(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(acceptParser.GContext)
            else:
                return self.getTypedRuleContext(acceptParser.GContext,i)


        def k(self):
            return self.getTypedRuleContext(acceptParser.KContext,0)


        def getRuleIndex(self):
            return acceptParser.RULE_f

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF" ):
                listener.enterF(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF" ):
                listener.exitF(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitF" ):
                return visitor.visitF(self)
            else:
                return visitor.visitChildren(self)




    def f(self):

        localctx = acceptParser.FContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_f)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.g()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.g()
                self.state = 120
                self.g()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                self.k()
                self.state = 123
                self.g()
                self.state = 124
                self.g()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 126
                self.match(acceptParser.T__8)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return acceptParser.RULE_g

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterG" ):
                listener.enterG(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitG" ):
                listener.exitG(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG" ):
                return visitor.visitG(self)
            else:
                return visitor.visitChildren(self)




    def g(self):

        localctx = acceptParser.GContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_g)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << acceptParser.T__3) | (1 << acceptParser.T__4) | (1 << acceptParser.T__5) | (1 << acceptParser.T__6) | (1 << acceptParser.T__7) | (1 << acceptParser.T__9) | (1 << acceptParser.T__10) | (1 << acceptParser.T__11) | (1 << acceptParser.T__12) | (1 << acceptParser.T__13))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return acceptParser.RULE_h

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterH" ):
                listener.enterH(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitH" ):
                listener.exitH(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitH" ):
                return visitor.visitH(self)
            else:
                return visitor.visitChildren(self)




    def h(self):

        localctx = acceptParser.HContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_h)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << acceptParser.T__4) | (1 << acceptParser.T__5) | (1 << acceptParser.T__6) | (1 << acceptParser.T__7) | (1 << acceptParser.T__9) | (1 << acceptParser.T__10) | (1 << acceptParser.T__11))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return acceptParser.RULE_i

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterI" ):
                listener.enterI(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitI" ):
                listener.exitI(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitI" ):
                return visitor.visitI(self)
            else:
                return visitor.visitChildren(self)




    def i(self):

        localctx = acceptParser.IContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_i)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << acceptParser.T__5) | (1 << acceptParser.T__6) | (1 << acceptParser.T__7) | (1 << acceptParser.T__9))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return acceptParser.RULE_j

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJ" ):
                listener.enterJ(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJ" ):
                listener.exitJ(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJ" ):
                return visitor.visitJ(self)
            else:
                return visitor.visitChildren(self)




    def j(self):

        localctx = acceptParser.JContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_j)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << acceptParser.T__6) | (1 << acceptParser.T__7) | (1 << acceptParser.T__9))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return acceptParser.RULE_k

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterK" ):
                listener.enterK(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitK" ):
                listener.exitK(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitK" ):
                return visitor.visitK(self)
            else:
                return visitor.visitChildren(self)




    def k(self):

        localctx = acceptParser.KContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_k)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            _la = self._input.LA(1)
            if not(_la==acceptParser.T__6 or _la==acceptParser.T__7):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return acceptParser.RULE_l

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterL" ):
                listener.enterL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitL" ):
                listener.exitL(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitL" ):
                return visitor.visitL(self)
            else:
                return visitor.visitChildren(self)




    def l(self):

        localctx = acceptParser.LContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_l)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << acceptParser.T__3) | (1 << acceptParser.T__4) | (1 << acceptParser.T__5) | (1 << acceptParser.T__6) | (1 << acceptParser.T__7) | (1 << acceptParser.T__9) | (1 << acceptParser.T__10) | (1 << acceptParser.T__11) | (1 << acceptParser.T__12))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return acceptParser.RULE_m

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterM" ):
                listener.enterM(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitM" ):
                listener.exitM(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitM" ):
                return visitor.visitM(self)
            else:
                return visitor.visitChildren(self)




    def m(self):

        localctx = acceptParser.MContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_m)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << acceptParser.T__4) | (1 << acceptParser.T__5) | (1 << acceptParser.T__6) | (1 << acceptParser.T__7) | (1 << acceptParser.T__9))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return acceptParser.RULE_n

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterN" ):
                listener.enterN(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitN" ):
                listener.exitN(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitN" ):
                return visitor.visitN(self)
            else:
                return visitor.visitChildren(self)




    def n(self):

        localctx = acceptParser.NContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_n)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << acceptParser.T__4) | (1 << acceptParser.T__5) | (1 << acceptParser.T__6) | (1 << acceptParser.T__7) | (1 << acceptParser.T__9) | (1 << acceptParser.T__10))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





