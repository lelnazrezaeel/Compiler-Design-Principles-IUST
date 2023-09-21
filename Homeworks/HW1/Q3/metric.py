from gen.JavaParserLabeled import JavaParserLabeled
from gen.JavaParserLabeledListener import JavaParserLabeledListener

class DSCmetric(JavaParserLabeledListener):
    def __init__(self):
        self.methodNames = []
        self.packageName = ""

    def enterMethodDeclaration(self, ctx: JavaParserLabeled.MethodDeclarationContext):
        self.methodNames.append(ctx.IDENTIFIER().getText())

    def enterPackageDeclaration(self, ctx: JavaParserLabeled.PackageDeclarationContext):
        output = "";
        for name in ctx.qualifiedName().IDENTIFIER():
            output += name.getText() + '.'
        self.packageName = output[0:-1]
        print(self.packageName)