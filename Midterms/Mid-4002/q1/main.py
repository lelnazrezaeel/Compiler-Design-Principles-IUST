from antlr4 import *
from gen.acceptLexer import acceptLexer
from gen.acceptParser import acceptParser
from gen.acceptListener import acceptListener


class MyCustomListener(acceptListener):
    def __init__(self):
        self.flag = False

if __name__ == '__main__':
    input_stream = InputStream("F1:433,122,344")
    lexer = acceptLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = acceptParser(stream)
    tree = parser.compilationUnit()
    walker = ParseTreeWalker()
    listener = MyCustomListener()
    walker.walk(listener, tree)
    print(listener.flag)
