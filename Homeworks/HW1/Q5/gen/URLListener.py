# Generated from E:/University/Term6/Compiler/HW1/Q5/grammer\URL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .URLParser import URLParser
else:
    from URLParser import URLParser

# This class defines a complete listener for a parse tree produced by URLParser.
class URLListener(ParseTreeListener):

    # Enter a parse tree produced by URLParser#url.
    def enterUrl(self, ctx:URLParser.UrlContext):
        pass

    # Exit a parse tree produced by URLParser#url.
    def exitUrl(self, ctx:URLParser.UrlContext):
        pass


    # Enter a parse tree produced by URLParser#pattern.
    def enterPattern(self, ctx:URLParser.PatternContext):
        pass

    # Exit a parse tree produced by URLParser#pattern.
    def exitPattern(self, ctx:URLParser.PatternContext):
        pass


    # Enter a parse tree produced by URLParser#scheme.
    def enterScheme(self, ctx:URLParser.SchemeContext):
        pass

    # Exit a parse tree produced by URLParser#scheme.
    def exitScheme(self, ctx:URLParser.SchemeContext):
        pass


    # Enter a parse tree produced by URLParser#host.
    def enterHost(self, ctx:URLParser.HostContext):
        pass

    # Exit a parse tree produced by URLParser#host.
    def exitHost(self, ctx:URLParser.HostContext):
        pass


    # Enter a parse tree produced by URLParser#port.
    def enterPort(self, ctx:URLParser.PortContext):
        pass

    # Exit a parse tree produced by URLParser#port.
    def exitPort(self, ctx:URLParser.PortContext):
        pass


    # Enter a parse tree produced by URLParser#path.
    def enterPath(self, ctx:URLParser.PathContext):
        pass

    # Exit a parse tree produced by URLParser#path.
    def exitPath(self, ctx:URLParser.PathContext):
        pass


    # Enter a parse tree produced by URLParser#frag.
    def enterFrag(self, ctx:URLParser.FragContext):
        pass

    # Exit a parse tree produced by URLParser#frag.
    def exitFrag(self, ctx:URLParser.FragContext):
        pass


    # Enter a parse tree produced by URLParser#query.
    def enterQuery(self, ctx:URLParser.QueryContext):
        pass

    # Exit a parse tree produced by URLParser#query.
    def exitQuery(self, ctx:URLParser.QueryContext):
        pass


    # Enter a parse tree produced by URLParser#search.
    def enterSearch(self, ctx:URLParser.SearchContext):
        pass

    # Exit a parse tree produced by URLParser#search.
    def exitSearch(self, ctx:URLParser.SearchContext):
        pass


    # Enter a parse tree produced by URLParser#searchparameter.
    def enterSearchparameter(self, ctx:URLParser.SearchparameterContext):
        pass

    # Exit a parse tree produced by URLParser#searchparameter.
    def exitSearchparameter(self, ctx:URLParser.SearchparameterContext):
        pass


    # Enter a parse tree produced by URLParser#string.
    def enterString(self, ctx:URLParser.StringContext):
        pass

    # Exit a parse tree produced by URLParser#string.
    def exitString(self, ctx:URLParser.StringContext):
        pass



del URLParser