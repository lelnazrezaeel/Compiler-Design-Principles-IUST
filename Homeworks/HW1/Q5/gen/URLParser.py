# Generated from E:/University/Term6/Compiler/HW1/Q5/grammer\URL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3!\n\3\3\3\3\3\5\3%\n\3\5\3\'\n\3\3")
        buf.write("\3\5\3*\n\3\3\3\5\3-\n\3\3\3\5\3\60\n\3\3\4\3\4\3\5\3")
        buf.write("\5\3\5\7\5\67\n\5\f\5\16\5:\13\5\3\6\3\6\3\7\3\7\3\7\7")
        buf.write("\7A\n\7\f\7\16\7D\13\7\3\7\5\7G\n\7\3\b\3\b\3\b\5\bL\n")
        buf.write("\b\3\t\3\t\3\t\3\n\3\n\3\n\7\nT\n\n\f\n\16\nW\13\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13^\n\13\5\13`\n\13\3\f\3\f\3\f")
        buf.write("\2\2\r\2\4\6\b\n\f\16\20\22\24\26\2\3\4\2\13\13\r\r\2")
        buf.write("f\2\30\3\2\2\2\4\33\3\2\2\2\6\61\3\2\2\2\b\63\3\2\2\2")
        buf.write("\n;\3\2\2\2\f=\3\2\2\2\16H\3\2\2\2\20M\3\2\2\2\22P\3\2")
        buf.write("\2\2\24X\3\2\2\2\26a\3\2\2\2\30\31\5\4\3\2\31\32\7\2\2")
        buf.write("\3\32\3\3\2\2\2\33\34\5\6\4\2\34\35\7\3\2\2\35 \5\b\5")
        buf.write("\2\36\37\7\4\2\2\37!\5\n\6\2 \36\3\2\2\2 !\3\2\2\2!&\3")
        buf.write("\2\2\2\"$\7\5\2\2#%\5\f\7\2$#\3\2\2\2$%\3\2\2\2%\'\3\2")
        buf.write("\2\2&\"\3\2\2\2&\'\3\2\2\2\')\3\2\2\2(*\5\20\t\2)(\3\2")
        buf.write("\2\2)*\3\2\2\2*,\3\2\2\2+-\5\16\b\2,+\3\2\2\2,-\3\2\2")
        buf.write("\2-/\3\2\2\2.\60\7\16\2\2/.\3\2\2\2/\60\3\2\2\2\60\5\3")
        buf.write("\2\2\2\61\62\5\26\f\2\62\7\3\2\2\2\638\5\26\f\2\64\65")
        buf.write("\7\6\2\2\65\67\5\26\f\2\66\64\3\2\2\2\67:\3\2\2\28\66")
        buf.write("\3\2\2\289\3\2\2\29\t\3\2\2\2:8\3\2\2\2;<\7\13\2\2<\13")
        buf.write("\3\2\2\2=B\5\26\f\2>?\7\5\2\2?A\5\26\f\2@>\3\2\2\2AD\3")
        buf.write("\2\2\2B@\3\2\2\2BC\3\2\2\2CF\3\2\2\2DB\3\2\2\2EG\7\5\2")
        buf.write("\2FE\3\2\2\2FG\3\2\2\2G\r\3\2\2\2HK\7\7\2\2IL\5\26\f\2")
        buf.write("JL\7\13\2\2KI\3\2\2\2KJ\3\2\2\2L\17\3\2\2\2MN\7\b\2\2")
        buf.write("NO\5\22\n\2O\21\3\2\2\2PU\5\24\13\2QR\7\t\2\2RT\5\24\13")
        buf.write("\2SQ\3\2\2\2TW\3\2\2\2US\3\2\2\2UV\3\2\2\2V\23\3\2\2\2")
        buf.write("WU\3\2\2\2X_\5\26\f\2Y]\7\n\2\2Z^\5\26\f\2[^\7\13\2\2")
        buf.write("\\^\7\f\2\2]Z\3\2\2\2][\3\2\2\2]\\\3\2\2\2^`\3\2\2\2_")
        buf.write("Y\3\2\2\2_`\3\2\2\2`\25\3\2\2\2ab\t\2\2\2b\27\3\2\2\2")
        buf.write("\17 $&),/8BFKU]_")
        return buf.getvalue()


class URLParser ( Parser ):

    grammarFileName = "URL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'://'", "':'", "'/'", "'.'", "'#'", "'?'", 
                     "'&'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "DIGITS", "HEX", "STRING", "WS" ]

    RULE_url = 0
    RULE_pattern = 1
    RULE_scheme = 2
    RULE_host = 3
    RULE_port = 4
    RULE_path = 5
    RULE_frag = 6
    RULE_query = 7
    RULE_search = 8
    RULE_searchparameter = 9
    RULE_string = 10

    ruleNames =  [ "url", "pattern", "scheme", "host", "port", "path", "frag", 
                   "query", "search", "searchparameter", "string" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    DIGITS=9
    HEX=10
    STRING=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class UrlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pattern(self):
            return self.getTypedRuleContext(URLParser.PatternContext,0)


        def EOF(self):
            return self.getToken(URLParser.EOF, 0)

        def getRuleIndex(self):
            return URLParser.RULE_url

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUrl" ):
                listener.enterUrl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUrl" ):
                listener.exitUrl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUrl" ):
                return visitor.visitUrl(self)
            else:
                return visitor.visitChildren(self)




    def url(self):

        localctx = URLParser.UrlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_url)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.pattern()
            self.state = 23
            self.match(URLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scheme(self):
            return self.getTypedRuleContext(URLParser.SchemeContext,0)


        def host(self):
            return self.getTypedRuleContext(URLParser.HostContext,0)


        def port(self):
            return self.getTypedRuleContext(URLParser.PortContext,0)


        def query(self):
            return self.getTypedRuleContext(URLParser.QueryContext,0)


        def frag(self):
            return self.getTypedRuleContext(URLParser.FragContext,0)


        def WS(self):
            return self.getToken(URLParser.WS, 0)

        def path(self):
            return self.getTypedRuleContext(URLParser.PathContext,0)


        def getRuleIndex(self):
            return URLParser.RULE_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPattern" ):
                listener.enterPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPattern" ):
                listener.exitPattern(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPattern" ):
                return visitor.visitPattern(self)
            else:
                return visitor.visitChildren(self)




    def pattern(self):

        localctx = URLParser.PatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pattern)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.scheme()
            self.state = 26
            self.match(URLParser.T__0)
            self.state = 27
            self.host()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==URLParser.T__1:
                self.state = 28
                self.match(URLParser.T__1)
                self.state = 29
                self.port()


            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==URLParser.T__2:
                self.state = 32
                self.match(URLParser.T__2)
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==URLParser.DIGITS or _la==URLParser.STRING:
                    self.state = 33
                    self.path()




            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==URLParser.T__5:
                self.state = 38
                self.query()


            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==URLParser.T__4:
                self.state = 41
                self.frag()


            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==URLParser.WS:
                self.state = 44
                self.match(URLParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SchemeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(URLParser.StringContext,0)


        def getRuleIndex(self):
            return URLParser.RULE_scheme

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScheme" ):
                listener.enterScheme(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScheme" ):
                listener.exitScheme(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScheme" ):
                return visitor.visitScheme(self)
            else:
                return visitor.visitChildren(self)




    def scheme(self):

        localctx = URLParser.SchemeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_scheme)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HostContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(URLParser.StringContext)
            else:
                return self.getTypedRuleContext(URLParser.StringContext,i)


        def getRuleIndex(self):
            return URLParser.RULE_host

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHost" ):
                listener.enterHost(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHost" ):
                listener.exitHost(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHost" ):
                return visitor.visitHost(self)
            else:
                return visitor.visitChildren(self)




    def host(self):

        localctx = URLParser.HostContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_host)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.string()
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==URLParser.T__3:
                self.state = 50
                self.match(URLParser.T__3)
                self.state = 51
                self.string()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PortContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGITS(self):
            return self.getToken(URLParser.DIGITS, 0)

        def getRuleIndex(self):
            return URLParser.RULE_port

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPort" ):
                listener.enterPort(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPort" ):
                listener.exitPort(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPort" ):
                return visitor.visitPort(self)
            else:
                return visitor.visitChildren(self)




    def port(self):

        localctx = URLParser.PortContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_port)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(URLParser.DIGITS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(URLParser.StringContext)
            else:
                return self.getTypedRuleContext(URLParser.StringContext,i)


        def getRuleIndex(self):
            return URLParser.RULE_path

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPath" ):
                listener.enterPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPath" ):
                listener.exitPath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPath" ):
                return visitor.visitPath(self)
            else:
                return visitor.visitChildren(self)




    def path(self):

        localctx = URLParser.PathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_path)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.string()
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 60
                    self.match(URLParser.T__2)
                    self.state = 61
                    self.string() 
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==URLParser.T__2:
                self.state = 67
                self.match(URLParser.T__2)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FragContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(URLParser.StringContext,0)


        def DIGITS(self):
            return self.getToken(URLParser.DIGITS, 0)

        def getRuleIndex(self):
            return URLParser.RULE_frag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrag" ):
                listener.enterFrag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrag" ):
                listener.exitFrag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFrag" ):
                return visitor.visitFrag(self)
            else:
                return visitor.visitChildren(self)




    def frag(self):

        localctx = URLParser.FragContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_frag)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(URLParser.T__4)
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 71
                self.string()
                pass

            elif la_ == 2:
                self.state = 72
                self.match(URLParser.DIGITS)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def search(self):
            return self.getTypedRuleContext(URLParser.SearchContext,0)


        def getRuleIndex(self):
            return URLParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = URLParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(URLParser.T__5)
            self.state = 76
            self.search()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SearchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def searchparameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(URLParser.SearchparameterContext)
            else:
                return self.getTypedRuleContext(URLParser.SearchparameterContext,i)


        def getRuleIndex(self):
            return URLParser.RULE_search

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSearch" ):
                listener.enterSearch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSearch" ):
                listener.exitSearch(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSearch" ):
                return visitor.visitSearch(self)
            else:
                return visitor.visitChildren(self)




    def search(self):

        localctx = URLParser.SearchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_search)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.searchparameter()
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==URLParser.T__6:
                self.state = 79
                self.match(URLParser.T__6)
                self.state = 80
                self.searchparameter()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SearchparameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(URLParser.StringContext)
            else:
                return self.getTypedRuleContext(URLParser.StringContext,i)


        def DIGITS(self):
            return self.getToken(URLParser.DIGITS, 0)

        def HEX(self):
            return self.getToken(URLParser.HEX, 0)

        def getRuleIndex(self):
            return URLParser.RULE_searchparameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSearchparameter" ):
                listener.enterSearchparameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSearchparameter" ):
                listener.exitSearchparameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSearchparameter" ):
                return visitor.visitSearchparameter(self)
            else:
                return visitor.visitChildren(self)




    def searchparameter(self):

        localctx = URLParser.SearchparameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_searchparameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.string()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==URLParser.T__7:
                self.state = 87
                self.match(URLParser.T__7)
                self.state = 91
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                if la_ == 1:
                    self.state = 88
                    self.string()
                    pass

                elif la_ == 2:
                    self.state = 89
                    self.match(URLParser.DIGITS)
                    pass

                elif la_ == 3:
                    self.state = 90
                    self.match(URLParser.HEX)
                    pass




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(URLParser.STRING, 0)

        def DIGITS(self):
            return self.getToken(URLParser.DIGITS, 0)

        def getRuleIndex(self):
            return URLParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = URLParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not(_la==URLParser.DIGITS or _la==URLParser.STRING):
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





