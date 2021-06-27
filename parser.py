from .lexer import generator

from rply import ParserGenerator, Token

parser = ParserGenerator([l.name for l in generator.rules])

@parser.production('string : STRING')
def string(p: list) -> str:
    return p[0].getstr().strip("'").strip('"')

@parser.production("expr: rooPog string")
def rooPog(p: list) -> None:
    