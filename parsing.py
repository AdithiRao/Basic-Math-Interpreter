from tokens import TokenType
from components import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.currPos = -1
        self.currToken = None
        self.getNextToken()

    def getNextToken(self):
        if self.currPos + 1 < len(self.tokens):
            self.currPos += 1
            self.currToken = self.tokens[self.currPos]
        else:
            self.currToken = None

    def parse(self):
        if self.currToken == None:
            return None

        result = self.plusOrMinus()

        if self.currToken != None:
            raise Exception('Invalid character entered')

        return result

    def plusOrMinus(self):
        result = self.multiplyOrDivide()

        while self.currToken and self.currToken.type in (TokenType.PLUS, TokenType.MINUS):
            if self.currToken.type == TokenType.PLUS:
                self.getNextToken() #advance past the plus token
                result = Add(result, self.multiplyOrDivide())
            else:
                self.getNextToken() #advance past the minus token
                result = Subtract(result, self.multiplyOrDivide())
        return result

    def multiplyOrDivide(self):
        result = self.base()

        while self.currToken and self.currToken.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if self.currToken.type == TokenType.MULTIPLY:
                self.getNextToken() #advance past the plus token
                number2 = self.base()
                result = Multiply(result, number2)
            else:
                self.getNextToken() #advance past the minus token
                number2 = self.base()
                result = Divide(result, number2)
        return result

    def base(self):
        token = self.currToken
        if token.type == TokenType.LPAREN:
            self.getNextToken()
            result = self.plusOrMinus()
            if self.currToken.type != TokenType.RPAREN:
                raise Exception("Unmatched left parenthesis")
            self.getNextToken()
            return result
        elif token.type == TokenType.NUMBER:
            self.getNextToken()
            return Number(token.value)
        elif token.type == TokenType.PLUS:
            self.getNextToken()
            return Plus(self.base())
        elif token.type == TokenType.MINUS:
            self.getNextToken()
            return Negate(self.base())
        raise Exception('Invalid character entered')
