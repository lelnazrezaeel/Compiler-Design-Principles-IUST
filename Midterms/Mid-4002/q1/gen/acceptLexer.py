# Generated from /home/loop/uni/compiler/q1/accept.g4 by ANTLR 4.10.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,14,63,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,
        1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,
        1,12,1,12,1,13,1,13,0,0,14,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,
        9,19,10,21,11,23,12,25,13,27,14,1,0,0,62,0,1,1,0,0,0,0,3,1,0,0,0,
        0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,
        15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,
        25,1,0,0,0,0,27,1,0,0,0,1,29,1,0,0,0,3,33,1,0,0,0,5,35,1,0,0,0,7,
        39,1,0,0,0,9,41,1,0,0,0,11,43,1,0,0,0,13,45,1,0,0,0,15,47,1,0,0,
        0,17,49,1,0,0,0,19,53,1,0,0,0,21,55,1,0,0,0,23,57,1,0,0,0,25,59,
        1,0,0,0,27,61,1,0,0,0,29,30,5,70,0,0,30,31,5,49,0,0,31,32,5,58,0,
        0,32,2,1,0,0,0,33,34,5,44,0,0,34,4,1,0,0,0,35,36,5,70,0,0,36,37,
        5,50,0,0,37,38,5,58,0,0,38,6,1,0,0,0,39,40,5,55,0,0,40,8,1,0,0,0,
        41,42,5,52,0,0,42,10,1,0,0,0,43,44,5,51,0,0,44,12,1,0,0,0,45,46,
        5,48,0,0,46,14,1,0,0,0,47,48,5,49,0,0,48,16,1,0,0,0,49,50,5,50,0,
        0,50,51,5,48,0,0,51,52,5,48,0,0,52,18,1,0,0,0,53,54,5,50,0,0,54,
        20,1,0,0,0,55,56,5,53,0,0,56,22,1,0,0,0,57,58,5,54,0,0,58,24,1,0,
        0,0,59,60,5,56,0,0,60,26,1,0,0,0,61,62,5,57,0,0,62,28,1,0,0,0,1,
        0,0
    ]

class acceptLexer(Lexer):

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
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'F1:'", "','", "'F2:'", "'7'", "'4'", "'3'", "'0'", "'1'", 
            "'200'", "'2'", "'5'", "'6'", "'8'", "'9'" ]

    symbolicNames = [ "<INVALID>",
 ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13" ]

    grammarFileName = "accept.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


