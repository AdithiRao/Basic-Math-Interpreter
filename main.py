from lexer import Lexer
from parsing import Parser
from interpreter import Interpreter
import sys

while True:
    try:
        text = input('>>> ')
        if text.strip().lower() == 'quit':
            break
        lexer = Lexer(text)
        tokens = list(lexer.generateTokens())
        parser = Parser(tokens)
        expression = parser.parse()
        interpreter = Interpreter()
        interpreter.evaluate(expression)
    except EOFError:
        sys.stdout.write('\nExitted.\n')
        break
    except KeyboardInterrupt: #ctrl+c
        sys.stdout.write('\nExitted.\n')
        break
    except Exception as e:
        print(e)
