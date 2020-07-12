from tokens import Token, TokenType

WHITESPACE = ' \n\t'
DIGITS = '0123456789'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.currPos = -1
        self.currChar = None
        self.getNextChar()

    def getNextChar(self):
        if self.currPos + 1 < len(self.text):
            self.currPos += 1
            self.currChar = self.text[self.currPos]
        else:
            self.currChar = None

    #generates the tokens so uses yield instead of return
    def generateTokens(self):
        while self.currChar:
            if self.currChar in WHITESPACE:
                self.getNextChar()
            elif self.currChar in DIGITS or self.currChar == ".":
                num = self.generateNumber()
                print(num)
                if num != None:
                    print("done")
                    yield num
            elif self.currChar == "+":
                self.getNextChar()
                yield Token(TokenType.PLUS)
            elif self.currChar == "-":
                self.getNextChar()
                yield Token(TokenType.MINUS)
            elif self.currChar == "/":
                self.getNextChar()
                if self.currChar == "/":
                    self.getNextChar()
                    yield Token(TokenType.INTDIVIDE)
                else:
                    yield Token(TokenType.DIVIDE)
            elif self.currChar == "*":
                self.getNextChar()
                if self.currChar == "*":
                    self.getNextChar()
                    yield Token(TokenType.EXPONENT)
                else:
                    yield Token(TokenType.MULTIPLY)
            elif self.currChar == "%":
                self.getNextChar()
                yield Token(TokenType.MOD)
            elif self.currChar == "(":
                self.getNextChar()
                yield Token(TokenType.LPAREN)
            elif self.currChar == ")":
                self.getNextChar()
                yield Token(TokenType.RPAREN)
            else:
                raise Exception(f"Illegal character '{self.currChar}'")


    def generateNumber(self):
        numberString = ""
        numDecimalPoints = 0
        floatNum = False
        while self.currChar and self.currChar in DIGITS or (self.currChar == "." and numDecimalPoints==0):
            if self.currChar == ".":
                floatNum = True
                numDecimalPoints+=1
                numberString += "."
            else:
                numberString += self.currChar
            self.getNextChar()
        if numberString == ".":
            return None
        if numberString.startswith('.'):
            numberString = "." + numberString
        if numberString.endswith('.'):
            numberString += '0'
        if floatNum:
            return Token(TokenType.FLOAT, float(numberString))
        else:
            return Token(TokenType.INT, int(numberString))
