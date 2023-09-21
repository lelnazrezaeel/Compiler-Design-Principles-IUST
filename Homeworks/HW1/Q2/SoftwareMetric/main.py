from antlr4 import *
from gen.JavaLexer import JavaLexer
from gen.JavaParserLabeled import JavaParserLabeled
from metric import DSCmetric
import argparse

def main(args):
    stream = FileStream(args.file, encoding='utf8')
    lexer = JavaLexer(stream)
    token_stream = commonTokenStream(lexer)
    parser = JavaParserLabeled(token_stream)
    parse_tree = parser.compilationUnit()

    my_listener = DSCmetric()

    walker = ParseTreeWalker()
    walker.walk(t=parse_tree, listener=my_listener)

    print('compiler result : ')

    print(f'Method Name = {my_listener.get_name}')


if __name__ == '__main__':

    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'A.java')
    args = argparser.parse_args()
    main(args)