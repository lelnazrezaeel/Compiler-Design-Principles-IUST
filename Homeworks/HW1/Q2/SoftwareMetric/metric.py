from gen.JavaParserLabeled import JavaParserLabeled
from gen.JavaParserLabeledListener import JavaParserLabeledListener

class DSCmetric(JavaParserLabeledListener):
    def __init__(self):
        self.__dsc = 0
        self.name = []

        @property
        def get_design_size(self):
            return self.__dsc

        @property
        def get_name(self):
            return self.name

        def enterClassDeclaration(self, ctx: JavaParserLabeled.ClassDeclarationContext):
            self.__dsc += 1

        def enterMethodDeclaration(self, ctx:JavaParserLabeled.MethodDeclarationContext):
            self.name.append(ctx.IDENTIFIER().getText())
