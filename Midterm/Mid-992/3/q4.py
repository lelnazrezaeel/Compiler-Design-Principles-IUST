from antlr4 import *
import os

from gen.JavaLexer import JavaLexer

def main(input_address, output_address, id):
    file_stream = FileStream(r""+input_address)

    if os.path.exists(output_address):
        os.remove(output_address)

    output_stream = open(r""+output_address, "a")
    lexer = JavaLexer(file_stream)

    token = lexer.nextToken()

    while token.type != Token.EOF:
        text = token.text
        if token.type == lexer.COMMENT:
            text = '/* by ' + id + ': ' + text[2:-2] + '*/'
        elif token.type == lexer.LINE_COMMENT:
            text = '// by ' + id + ': ' + text[2:]

        output_stream.write(text)
        token = lexer.nextToken()
    output_stream.close()



if __name__ == "__main__":
    id  = input('please input your studet id : ')
    main('test.java', 'result.java', id)

