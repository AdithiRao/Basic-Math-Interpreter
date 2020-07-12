from tokens import TokenType
from nodes import *

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

        # go by order of operations
        result = self.plusOrMinus()

        if self.currToken != None:
            raise Exception('Invalid character entered')

        return result

    def plusOrMinus(self):
        result = self.multiplyOrDivide()

        while self.currToken and self.currToken.type in (TokenType.PLUS, TokenType.MINUS):
            if self.currToken.type == TokenType.PLUS:
                self.getNextToken() #advance past the plus token
                result = AddNode(result, self.multiplyOrDivide())
            else:
                self.getNextToken() #advance past the minus token
                result = SubtractNode(result, self.multiplyOrDivide())
        return result

    def multiplyOrDivide(self):
        result = self.exponentiate()

        while self.currToken and self.currToken.type in \
        (TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.INTDIVIDE, TokenType.MOD):
            if self.currToken.type == TokenType.MULTIPLY:
                self.getNextToken() #advance past the plus token
                number2 = self.exponentiate()
                result = MultiplyNode(result, number2)
            elif self.currToken.type == TokenType.DIVIDE:
                self.getNextToken() #advance past the minus token
                number2 = self.exponentiate()
                result = DivideNode(result, number2)
            elif self.currToken.type == TokenType.INTDIVIDE:
                self.getNextToken() #advance past the int divide token
                number2 = self.exponentiate()
                result = IntegerDivideNode(result, number2)
            elif self.currToken.type == TokenType.MOD:
                self.getNextToken() #advance past the int divide token
                number2 = self.exponentiate()
                result = ModNode(result, number2)
        return result

    def exponentiate(self):
        result = self.base()
        while self.currToken and self.currToken.type == TokenType.EXPONENT:
            self.getNextToken()
            number2 = self.base()
            result = ExponentNode(result, number2)
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
        elif token.type == TokenType.FLOAT:
            self.getNextToken()
            return FloatNode(token.value)
        elif token.type == TokenType.INT:
            self.getNextToken()
            return IntNode(token.value)
        elif token.type == TokenType.PLUS:
            self.getNextToken()
            return PlusNode(self.base())
        elif token.type == TokenType.MINUS:
            self.getNextToken()
            return NegateNode(self.base())
        raise Exception('Invalid character entered')
