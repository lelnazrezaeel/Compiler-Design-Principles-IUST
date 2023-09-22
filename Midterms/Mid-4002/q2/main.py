from antlr4 import *
from gen.JavaLexer import JavaLexer
from gen.JavaParserLabeled import JavaParserLabeled
from gen.JavaParserLabeledListener import JavaParserLabeledListener


class CustomListener(JavaParserLabeledListener):
    def __init__(self, m: int = 3):
        self.m = m
        self.result = {}
        self.modifier = None
        self.current_class = None
        if self.m == 0:
            self.text = "public void"
        elif self.m == 1:
            self.text = "private void"
        elif self.m == 2:
            self.text = "protected void"
        elif self.m == 3:
            self.text = "public int"

    def enterClassDeclaration(self, ctx: JavaParserLabeled.ClassDeclarationContext):
        self.current_class = ctx.IDENTIFIER().getText()
        self.result[self.current_class] = []

    def enterClassOrInterfaceModifier(self, ctx: JavaParserLabeled.ClassOrInterfaceModifierContext):
        self.modifier = ctx.getText()

    def enterMethodDeclaration(self, ctx: JavaParserLabeled.MethodDeclarationContext):
        return_type = ctx.typeTypeOrVoid().getText()
        method_name = ctx.IDENTIFIER().getText()
        if self.text == f"{self.modifier} {return_type}":
            self.result[self.current_class].append(method_name)


if __name__ == '__main__':
    input_stream = FileStream("sample.java")
    lexer = JavaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JavaParserLabeled(stream)
    tree = parser.compilationUnit()
    walker = ParseTreeWalker()
    listener = CustomListener(3)
    walker.walk(listener, tree)

    print(listener.result)
