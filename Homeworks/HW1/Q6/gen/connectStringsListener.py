# Generated from E:/University/Term6/Compiler/HW1/Q6/grammer\connectStrings.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .connectStringsParser import connectStringsParser
else:
    from connectStringsParser import connectStringsParser

# This class defines a complete listener for a parse tree produced by connectStringsParser.
class connectStringsListener(ParseTreeListener):

    # Enter a parse tree produced by connectStringsParser#start.
    def enterStart(self, ctx:connectStringsParser.StartContext):
        pass

    # Exit a parse tree produced by connectStringsParser#start.
    def exitStart(self, ctx:connectStringsParser.StartContext):
        pass


    # Enter a parse tree produced by connectStringsParser#connect_strings.
    def enterConnect_strings(self, ctx:connectStringsParser.Connect_stringsContext):
        pass

    # Exit a parse tree produced by connectStringsParser#connect_strings.
    def exitConnect_strings(self, ctx:connectStringsParser.Connect_stringsContext):
        pass


    # Enter a parse tree produced by connectStringsParser#server.
    def enterServer(self, ctx:connectStringsParser.ServerContext):
        pass

    # Exit a parse tree produced by connectStringsParser#server.
    def exitServer(self, ctx:connectStringsParser.ServerContext):
        pass


    # Enter a parse tree produced by connectStringsParser#security.
    def enterSecurity(self, ctx:connectStringsParser.SecurityContext):
        pass

    # Exit a parse tree produced by connectStringsParser#security.
    def exitSecurity(self, ctx:connectStringsParser.SecurityContext):
        pass


    # Enter a parse tree produced by connectStringsParser#catalog.
    def enterCatalog(self, ctx:connectStringsParser.CatalogContext):
        pass

    # Exit a parse tree produced by connectStringsParser#catalog.
    def exitCatalog(self, ctx:connectStringsParser.CatalogContext):
        pass



del connectStringsParser