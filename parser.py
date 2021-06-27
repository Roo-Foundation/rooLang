from lexer import generator

from typing import List
from rply import ParserGenerator, Token


parser = ParserGenerator([l.name for l in generator.rules])


class rooBulli(SyntaxError):
    pass
  
  
@parser.production('string : STRING')
def string(p: List[...]) -> str:
    return p[0].getstr().strip("'").strip('"')

@parser.production("expr : rooPog string")
def rooPog(p: List[...]) -> None:
    ...
    

@parser.error
def rooBulli_error_handler(token):
    raise rooBulli(f"rooBulli: Unexpected {token.gettokentype()} in {token.getsourcepos()}\nvalue : '{token.getstr()}'")

