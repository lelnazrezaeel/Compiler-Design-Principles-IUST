# Generated from E:/University/Term6/Compiler/HW1/Q6/grammer\connectStrings.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write(",\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\5\3\25\n\3\3\3\5\3\30\n\3\3\3\7\3")
        buf.write("\33\n\3\f\3\16\3\36\13\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\2\2\7\2\4\6\b\n\2\2\2*\2\f\3\2")
        buf.write("\2\2\4\24\3\2\2\2\6\37\3\2\2\2\b#\3\2\2\2\n\'\3\2\2\2")
        buf.write("\f\r\7\3\2\2\r\16\5\4\3\2\16\17\7\3\2\2\17\20\7\2\2\3")
        buf.write("\20\3\3\2\2\2\21\25\5\6\4\2\22\25\5\b\5\2\23\25\5\n\6")
        buf.write("\2\24\21\3\2\2\2\24\22\3\2\2\2\24\23\3\2\2\2\25\34\3\2")
        buf.write("\2\2\26\30\7\4\2\2\27\26\3\2\2\2\27\30\3\2\2\2\30\31\3")
        buf.write("\2\2\2\31\33\5\4\3\2\32\27\3\2\2\2\33\36\3\2\2\2\34\32")
        buf.write("\3\2\2\2\34\35\3\2\2\2\35\5\3\2\2\2\36\34\3\2\2\2\37 ")
        buf.write("\7\6\2\2 !\7\5\2\2!\"\7\7\2\2\"\7\3\2\2\2#$\7\b\2\2$%")
        buf.write("\7\5\2\2%&\7\t\2\2&\t\3\2\2\2\'(\7\n\2\2()\7\5\2\2)*\7")
        buf.write("\13\2\2*\13\3\2\2\2\5\24\27\34")
        return buf.getvalue()


class connectStringsParser ( Parser ):

    grammarFileName = "connectStrings.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\"'", "';'", "'='", "'server'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'Initial Catalog'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Se_keyword", "Se_description", "S_keyword", "S_description", 
                      "C_keyword", "C_description", "STRING" ]

    RULE_start = 0
    RULE_connect_strings = 1
    RULE_server = 2
    RULE_security = 3
    RULE_catalog = 4

    ruleNames =  [ "start", "connect_strings", "server", "security", "catalog" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    Se_keyword=4
    Se_description=5
    S_keyword=6
    S_description=7
    C_keyword=8
    C_description=9
    STRING=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def connect_strings(self):
            return self.getTypedRuleContext(connectStringsParser.Connect_stringsContext,0)


        def EOF(self):
            return self.getToken(connectStringsParser.EOF, 0)

        def getRuleIndex(self):
            return connectStringsParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = connectStringsParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(connectStringsParser.T__0)
            self.state = 11
            self.connect_strings()
            self.state = 12
            self.match(connectStringsParser.T__0)
            self.state = 13
            self.match(connectStringsParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Connect_stringsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def server(self):
            return self.getTypedRuleContext(connectStringsParser.ServerContext,0)


        def security(self):
            return self.getTypedRuleContext(connectStringsParser.SecurityContext,0)


        def catalog(self):
            return self.getTypedRuleContext(connectStringsParser.CatalogContext,0)


        def connect_strings(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(connectStringsParser.Connect_stringsContext)
            else:
                return self.getTypedRuleContext(connectStringsParser.Connect_stringsContext,i)


        def getRuleIndex(self):
            return connectStringsParser.RULE_connect_strings

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConnect_strings" ):
                listener.enterConnect_strings(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConnect_strings" ):
                listener.exitConnect_strings(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConnect_strings" ):
                return visitor.visitConnect_strings(self)
            else:
                return visitor.visitChildren(self)




    def connect_strings(self):

        localctx = connectStringsParser.Connect_stringsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_connect_strings)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [connectStringsParser.Se_keyword]:
                self.state = 15
                self.server()
                pass
            elif token in [connectStringsParser.S_keyword]:
                self.state = 16
                self.security()
                pass
            elif token in [connectStringsParser.C_keyword]:
                self.state = 17
                self.catalog()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 26
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 21
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==connectStringsParser.T__1:
                        self.state = 20
                        self.match(connectStringsParser.T__1)


                    self.state = 23
                    self.connect_strings() 
                self.state = 28
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ServerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Se_keyword(self):
            return self.getToken(connectStringsParser.Se_keyword, 0)

        def Se_description(self):
            return self.getToken(connectStringsParser.Se_description, 0)

        def getRuleIndex(self):
            return connectStringsParser.RULE_server

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterServer" ):
                listener.enterServer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitServer" ):
                listener.exitServer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitServer" ):
                return visitor.visitServer(self)
            else:
                return visitor.visitChildren(self)




    def server(self):

        localctx = connectStringsParser.ServerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_server)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(connectStringsParser.Se_keyword)
            self.state = 30
            self.match(connectStringsParser.T__2)
            self.state = 31
            self.match(connectStringsParser.Se_description)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SecurityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def S_keyword(self):
            return self.getToken(connectStringsParser.S_keyword, 0)

        def S_description(self):
            return self.getToken(connectStringsParser.S_description, 0)

        def getRuleIndex(self):
            return connectStringsParser.RULE_security

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSecurity" ):
                listener.enterSecurity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSecurity" ):
                listener.exitSecurity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSecurity" ):
                return visitor.visitSecurity(self)
            else:
                return visitor.visitChildren(self)




    def security(self):

        localctx = connectStringsParser.SecurityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_security)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(connectStringsParser.S_keyword)
            self.state = 34
            self.match(connectStringsParser.T__2)
            self.state = 35
            self.match(connectStringsParser.S_description)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CatalogContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def C_keyword(self):
            return self.getToken(connectStringsParser.C_keyword, 0)

        def C_description(self):
            return self.getToken(connectStringsParser.C_description, 0)

        def getRuleIndex(self):
            return connectStringsParser.RULE_catalog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatalog" ):
                listener.enterCatalog(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatalog" ):
                listener.exitCatalog(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCatalog" ):
                return visitor.visitCatalog(self)
            else:
                return visitor.visitChildren(self)




    def catalog(self):

        localctx = connectStringsParser.CatalogContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_catalog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(connectStringsParser.C_keyword)
            self.state = 38
            self.match(connectStringsParser.T__2)
            self.state = 39
            self.match(connectStringsParser.C_description)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





