from lexer import Lexer
from parsing import Parser
import sys

while True:
    try:
        text = input('>>> ')
        if text.strip().lower() == 'quit':
            break
        lexer = Lexer(text)
        tokens = list(lexer.generateTokens())
        print(list(tokens))
        parser = Parser(tokens)
        expression = parser.parse()
        print(expression)
    except EOFError:
        sys.stdout.write('\nExitted.\n')
        break
    except KeyboardInterrupt: #ctrl+c
        sys.stdout.write('\nExitted.\n')
        break
