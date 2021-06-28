from lexer import generator
from parser import parser # type: ignore
generator.build()
parser.build()
string = 'rooPog "Hello'
print(generator.lex(string))

