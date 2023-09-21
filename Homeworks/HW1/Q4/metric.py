from gen.JavaParserLabeled import JavaParserLabeled
from gen.JavaParserLabeledListener import JavaParserLabeledListener

class DSCmetric(JavaParserLabeledListener):
    def __init__(self):
        self.className = ""
        self.packageName = ""
        self.attributes = {}

    def enterClassDeclaration(self, ctx: JavaParserLabeled.ClassDeclarationContext):
        self.className = ctx.IDENTIFIER().getText()
        self.attributes[self.className] = 0

    def enterFieldDeclaration(self, ctx: JavaParserLabeled.FieldDeclarationContext):
        self.attributes[self.className] += 1

    def attributesNameAndCount(self):
        return self.attributes

    def enterPackageDeclaration(self, ctx: JavaParserLabeled.PackageDeclarationContext):
        output = "";
        for name in ctx.qualifiedName().IDENTIFIER():
            output += name.getText() + '.'
        self.packageName = output[0:-1]
        print(self.packageName)