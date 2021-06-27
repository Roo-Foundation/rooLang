from rply import LexerGenerator

generator = LexerGenerator()

generator.ignore(r'\s+')  # ignore all whitespace
generator.ignore(r"rooWhisper.*") # Ignore single line comment

generator.add("STRING", r'''("[^"\\]*(\\.[^"\\]*)*"|'[^'\\]*(\\.[^'\\]*)*')''')

generator.add("rooPog", r"rooPog")