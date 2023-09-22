# Generated from /home/loop/uni/compiler/q1/accept.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .acceptParser import acceptParser
else:
    from acceptParser import acceptParser

# This class defines a complete generic visitor for a parse tree produced by acceptParser.

class acceptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by acceptParser#compilationUnit.
    def visitCompilationUnit(self, ctx:acceptParser.CompilationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by acceptParser#a.
    def visitA(self, ctx:acceptParser.AContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by acceptParser#b.
    def visitB(self, ctx:acceptParser.BContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by acceptParser#c.
    def visitC(self, ctx:acceptParser.CContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by acceptParser#d.
    def visitD(self, ctx:acceptParser.DContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by acceptParser#e.
    def visitE(self, ctx:acceptParser.EContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by acceptParser#f.
    def visitF(self, ctx:acceptParser.FContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by acceptParser#g.
    def visitG(self, ctx:acceptParser.GContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by acceptParser#h.
    def visitH(self, ctx:acceptParser.HContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by acceptParser#i.
    def visitI(self, ctx:acceptParser.IContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by acceptParser#j.
    def visitJ(self, ctx:acceptParser.JContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by acceptParser#k.
    def visitK(self, ctx:acceptParser.KContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by acceptParser#l.
    def visitL(self, ctx:acceptParser.LContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by acceptParser#m.
    def visitM(self, ctx:acceptParser.MContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by acceptParser#n.
    def visitN(self, ctx:acceptParser.NContext):
        return self.visitChildren(ctx)



del acceptParser