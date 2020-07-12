from lexer import Lexer
from parsing import Parser
from interpreter import Interpreter
import sys

# TODO: Add fast exponentiation, modular arithmetic,
# sqrt, gcd

print('Type "help" to learn about what options are available.')
while True:
    try:
        text = input('>>> ')
        if text.strip().lower() == 'quit':
            sys.stdout.write('\n')
            break
        elif text.strip().lower() == 'help':
            print("This shell can handle the following operations:")
            print("+, -, *, /, //, %, **")
        else:
            lexer = Lexer(text)
            tokens = list(lexer.generateTokens())
            parser = Parser(tokens)
            expression = parser.parse()
            interpreter = Interpreter()
            answer = interpreter.evaluate(expression)
            if answer:
                print(answer)
    except EOFError:
        sys.stdout.write('\n')
        break
    except KeyboardInterrupt: #ctrl+c
        sys.stdout.write('\nKeyboardInterrupt\n')
        continue
    except Exception as e:
        print(e)
