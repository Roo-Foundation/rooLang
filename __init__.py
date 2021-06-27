from lexer import lexer

from parser import parser

def test(thing: str):
    print(parser.parse(lexer.lex(thing)).eval())