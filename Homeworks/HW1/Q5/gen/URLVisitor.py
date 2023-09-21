# Generated from E:/University/Term6/Compiler/HW1/Q5/grammer\URL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .URLParser import URLParser
else:
    from URLParser import URLParser

# This class defines a complete generic visitor for a parse tree produced by URLParser.

class URLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by URLParser#url.
    def visitUrl(self, ctx:URLParser.UrlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by URLParser#pattern.
    def visitPattern(self, ctx:URLParser.PatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by URLParser#scheme.
    def visitScheme(self, ctx:URLParser.SchemeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by URLParser#host.
    def visitHost(self, ctx:URLParser.HostContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by URLParser#port.
    def visitPort(self, ctx:URLParser.PortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by URLParser#path.
    def visitPath(self, ctx:URLParser.PathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by URLParser#frag.
    def visitFrag(self, ctx:URLParser.FragContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by URLParser#query.
    def visitQuery(self, ctx:URLParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by URLParser#search.
    def visitSearch(self, ctx:URLParser.SearchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by URLParser#searchparameter.
    def visitSearchparameter(self, ctx:URLParser.SearchparameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by URLParser#string.
    def visitString(self, ctx:URLParser.StringContext):
        return self.visitChildren(ctx)



del URLParser