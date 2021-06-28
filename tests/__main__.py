import roolang

def main(thing: str):
    roolang.parser.build().parse(roolang.generator.build().lex('1 + 1')).eval()

if __name__ == '__main__':
    while True:
        try:
            i = input("rooPog: ")
            main(i)
        except KeyboardInterrupt:
            exit()
