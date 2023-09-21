# Generated from E:/University/Term6/Compiler/HW1/Q5/grammer\URL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("I\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\6\n/\n\n\r\n\16\n\60\3\13\3\13\3\13")
        buf.write("\6\13\66\n\13\r\13\16\13\67\3\f\3\f\5\f<\n\f\3\f\3\f\7")
        buf.write("\f@\n\f\f\f\16\fC\13\f\3\r\6\rF\n\r\r\r\16\rG\2\2\16\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\3\2\7\3\2\62;\5\2\62;CHch\6\2\62;C\\c|\u0080\u0080\7")
        buf.write("\2--/\60\62;C\\c|\4\2\f\f\17\17\2N\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5\37\3\2\2\2\7!")
        buf.write("\3\2\2\2\t#\3\2\2\2\13%\3\2\2\2\r\'\3\2\2\2\17)\3\2\2")
        buf.write("\2\21+\3\2\2\2\23.\3\2\2\2\25\65\3\2\2\2\27;\3\2\2\2\31")
        buf.write("E\3\2\2\2\33\34\7<\2\2\34\35\7\61\2\2\35\36\7\61\2\2\36")
        buf.write("\4\3\2\2\2\37 \7<\2\2 \6\3\2\2\2!\"\7\61\2\2\"\b\3\2\2")
        buf.write("\2#$\7\60\2\2$\n\3\2\2\2%&\7%\2\2&\f\3\2\2\2\'(\7A\2\2")
        buf.write("(\16\3\2\2\2)*\7(\2\2*\20\3\2\2\2+,\7?\2\2,\22\3\2\2\2")
        buf.write("-/\t\2\2\2.-\3\2\2\2/\60\3\2\2\2\60.\3\2\2\2\60\61\3\2")
        buf.write("\2\2\61\24\3\2\2\2\62\63\7\'\2\2\63\64\t\3\2\2\64\66\t")
        buf.write("\3\2\2\65\62\3\2\2\2\66\67\3\2\2\2\67\65\3\2\2\2\678\3")
        buf.write("\2\2\28\26\3\2\2\29<\t\4\2\2:<\5\25\13\2;9\3\2\2\2;:\3")
        buf.write("\2\2\2<A\3\2\2\2=@\t\5\2\2>@\5\25\13\2?=\3\2\2\2?>\3\2")
        buf.write("\2\2@C\3\2\2\2A?\3\2\2\2AB\3\2\2\2B\30\3\2\2\2CA\3\2\2")
        buf.write("\2DF\t\6\2\2ED\3\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2H")
        buf.write("\32\3\2\2\2\t\2\60\67;?AG\2")
        return buf.getvalue()


class URLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    DIGITS = 9
    HEX = 10
    STRING = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'://'", "':'", "'/'", "'.'", "'#'", "'?'", "'&'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "DIGITS", "HEX", "STRING", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "DIGITS", "HEX", "STRING", "WS" ]

    grammarFileName = "URL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


