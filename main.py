from lexer import Lexer
from parsing import Parser
from interpreter import Interpreter
import sys

# TODO: Add fast exponentiation, modular arithmetic, integer division,
# sqrt, help command, gcd

while True:
    try:
        text = input('>>> ')
        if text.strip().lower() == 'quit':
            break
        lexer = Lexer(text)
        tokens = list(lexer.generateTokens())
        #print(tokens)
        parser = Parser(tokens)
        expression = parser.parse()
        #print(expression)
        interpreter = Interpreter()
        output = interpreter.evaluate(expression)
        #print(output)
    except EOFError:
        sys.stdout.write('\nExitted.\n')
        break
    except KeyboardInterrupt: #ctrl+c
        sys.stdout.write('\nKeyboardInterrupt\n')
        continue
    except Exception as e:
        print(e)
