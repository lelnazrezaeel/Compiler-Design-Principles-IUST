from antlr4 import *
from gen.JavaLexer import JavaLexer
from gen.JavaParserLabeled import JavaParserLabeled
from metric import DSCmetric
import argparse
import os

def main(args):
    print(args.file)
    packagesMethods = []
    for root, dirs, files in os.walk(args.file):
        for file in files:
            print(root)
            stream = FileStream(os.path.join(root, file), encoding='utf8')
            lexer = JavaLexer(stream)
            token_stream = CommonTokenStream(lexer)
            parser = JavaParserLabeled(token_stream)
            parse_tree = parser.compilationUnit()

            my_listener = DSCmetric()

            walker = ParseTreeWalker()
            walker.walk(t=parse_tree, listener=my_listener)

            print('compiler result : ')

            packagesMethods.append({"package_name" : my_listener.packageName , "attributes" : my_listener.attributesNameAndCount()})
    print(packagesMethods)

if __name__ == '__main__':

    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'A.java')
    args = argparser.parse_args()
    main(args)