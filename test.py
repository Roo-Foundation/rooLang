from roolang import generator
from roolang import parser
lexer = generator.build()
parser = parser.build()
string = 'rooPog "Hello"'
parser.parse(lexer.lex(string))
