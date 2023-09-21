# Generated from E:/University/Term6/Compiler/HW1/Q6/grammer\connectStrings.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .connectStringsParser import connectStringsParser
else:
    from connectStringsParser import connectStringsParser

# This class defines a complete generic visitor for a parse tree produced by connectStringsParser.

class connectStringsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by connectStringsParser#start.
    def visitStart(self, ctx:connectStringsParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by connectStringsParser#connect_strings.
    def visitConnect_strings(self, ctx:connectStringsParser.Connect_stringsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by connectStringsParser#server.
    def visitServer(self, ctx:connectStringsParser.ServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by connectStringsParser#security.
    def visitSecurity(self, ctx:connectStringsParser.SecurityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by connectStringsParser#catalog.
    def visitCatalog(self, ctx:connectStringsParser.CatalogContext):
        return self.visitChildren(ctx)



del connectStringsParser