from .roolexer import generator

from typing import List
from rply import ParserGenerator, Token


parser = ParserGenerator([l.name for l in generator.rules])


class rooBulli(SyntaxError):
    pass

@parser.production("main : expr")
def main(p: List[str]) -> str:
    return p[0]

@parser.production('string : STRING')
def string(p: List[str]) -> str:
    return p[0].getstr().strip("'").strip('"')

@parser.production("expr : rooPog string")
def rooPog(p: List[str]) -> None:
    print(p[-1])
    

@parser.error
def rooBulli_error_handler(token):
    raise rooBulli(f"rooBulli: Unexpected {token.gettokentype()} in {token.getsourcepos()}\nvalue : '{token.getstr()}'")
