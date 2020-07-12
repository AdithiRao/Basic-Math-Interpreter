import unittest
from tokens import Token, TokenType
from lexer import Lexer
from parsing import Parser
from interpreter import Interpreter, NumberValue
from nodes import *

class TestLexer(unittest.TestCase):

    def test_empty(self):
        tokens = list(Lexer("").generateTokens())
        self.assertEqual(tokens, [])
        tokens = list(Lexer("\t\n  \t").generateTokens())
        self.assertEqual(tokens, [])

    def test_nums(self):
        tokens = list(Lexer("111 235 2.1").generateTokens())
        self.assertEqual(tokens,[
            Token(TokenType.INT, 111),
            Token(TokenType.INT, 235),
            Token(TokenType.FLOAT, 2.1)
        ])

    def test_ops(self):
        tokens = list(Lexer("*/ %** // -+)(").generateTokens())
        self.assertEqual(tokens, [
            Token(TokenType.MULTIPLY),
            Token(TokenType.DIVIDE),
            Token(TokenType.MOD),
            Token(TokenType.EXPONENT),
            Token(TokenType.INTDIVIDE),
            Token(TokenType.MINUS),
            Token(TokenType.PLUS),
            Token(TokenType.RPAREN),
            Token(TokenType.LPAREN)
        ])

    def test_all(self):
        tokens = list(Lexer("1*2%2+(3.0/10)-4//1**3").generateTokens())
        self.assertEqual(tokens, [
            Token(TokenType.INT, 1),
            Token(TokenType.MULTIPLY),
            Token(TokenType.INT, 2),
            Token(TokenType.MOD),
            Token(TokenType.INT, 2),
            Token(TokenType.PLUS),
            Token(TokenType.LPAREN),
            Token(TokenType.FLOAT, 3.0),
            Token(TokenType.DIVIDE),
            Token(TokenType.INT, 10),
            Token(TokenType.RPAREN),
            Token(TokenType.MINUS),
            Token(TokenType.INT, 4),
            Token(TokenType.INTDIVIDE),
            Token(TokenType.INT, 1),
            Token(TokenType.EXPONENT),
            Token(TokenType.INT, 3)
        ])

class TestParser(unittest.TestCase):

    def test_empty(self):
        tokens = []
        node = Parser(tokens).parse()
        self.assertEqual(node, None)

    def test_numbers(self):
        tokens = [Token(TokenType.INT, 4)]
        node = Parser(tokens).parse()
        self.assertEqual(node, IntNode(4))
        tokens = [Token(TokenType.FLOAT, 3.0)]
        node = Parser(tokens).parse()
        self.assertEqual(node, FloatNode(3.0))

    def test_ops(self):
        tokens = [Token(TokenType.INT, 4), Token(TokenType.PLUS), Token(TokenType.FLOAT, 3.0)]
        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(IntNode(4), FloatNode(3.0)))

        tokens = [Token(TokenType.INT, 4), Token(TokenType.MINUS), Token(TokenType.FLOAT, 3.0)]
        node = Parser(tokens).parse()
        self.assertEqual(node, SubtractNode(IntNode(4), FloatNode(3.0)))

        tokens = [Token(TokenType.INT, 4), Token(TokenType.DIVIDE), Token(TokenType.FLOAT, 3.0)]
        node = Parser(tokens).parse()
        self.assertEqual(node, DivideNode(IntNode(4), FloatNode(3.0)))

        tokens = [Token(TokenType.INT, 4), Token(TokenType.MULTIPLY), Token(TokenType.FLOAT, 3.0)]
        node = Parser(tokens).parse()
        self.assertEqual(node, MultiplyNode(IntNode(4), FloatNode(3.0)))

        tokens = [Token(TokenType.INT, 4), Token(TokenType.INTDIVIDE), Token(TokenType.FLOAT, 3.0)]
        node = Parser(tokens).parse()
        self.assertEqual(node, IntegerDivideNode(IntNode(4), FloatNode(3.0)))

        tokens = [Token(TokenType.INT, 4), Token(TokenType.EXPONENT), Token(TokenType.FLOAT, 3.0)]
        node = Parser(tokens).parse()
        self.assertEqual(node, ExponentNode(IntNode(4), FloatNode(3.0)))

        tokens = [Token(TokenType.INT, 4), Token(TokenType.MOD), Token(TokenType.FLOAT, 3.0)]
        node = Parser(tokens).parse()
        self.assertEqual(node, ModNode(IntNode(4), FloatNode(3.0)))


    def test_full_exp(self):
        tokens = [
            Token(TokenType.MINUS),
            Token(TokenType.INT, 1),
            Token(TokenType.MULTIPLY),
            Token(TokenType.INT, 2),
            Token(TokenType.MOD),
            Token(TokenType.INT, 2),
            Token(TokenType.PLUS),
            Token(TokenType.LPAREN),
            Token(TokenType.FLOAT, 3.0),
            Token(TokenType.DIVIDE),
            Token(TokenType.INT, 10),
            Token(TokenType.RPAREN),
            Token(TokenType.MINUS),
            Token(TokenType.INT, 4),
            Token(TokenType.INTDIVIDE),
            Token(TokenType.INT, 1),
            Token(TokenType.EXPONENT),
            Token(TokenType.INT, 3)
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node,
            SubtractNode(
                AddNode(ModNode(MultiplyNode(NegateNode(IntNode(1)),IntNode(2)),
                                             IntNode(2)),
                                DivideNode(FloatNode(3.0), IntNode(10))),
                        IntegerDivideNode(IntNode(4),
                                         ExponentNode(IntNode(1), IntNode(3))))
        )

class TestInterpreter(unittest.TestCase):

    def test_none(self):
        number = Interpreter().evaluate(None)
        self.assertEqual(number, None)

    def test_numbers(self):
        number = Interpreter().evaluate(IntNode(2))
        self.assertEqual(number, NumberValue(2))
        number = Interpreter().evaluate(FloatNode(2.0))
        self.assertEqual(number, NumberValue(2.0))

    def test_ops(self):
        interpreter = Interpreter()
        number = interpreter.evaluate(AddNode(IntNode(4), FloatNode(3.0)))
        self.assertEqual(number, NumberValue(7.0))

        number = interpreter.evaluate(SubtractNode(IntNode(4), FloatNode(3.0)))
        self.assertEqual(number, NumberValue(1.0))

        number = interpreter.evaluate(MultiplyNode(IntNode(4), IntNode(3.0)))
        self.assertEqual(number, NumberValue(12.0))

        number = interpreter.evaluate(DivideNode(IntNode(4), IntNode(3.0)))
        self.assertAlmostEqual(number.value, NumberValue(1.33333).value, 5)

        number = interpreter.evaluate(ModNode(IntNode(4), IntNode(3.0)))
        self.assertEqual(number, NumberValue(1.0))

        number = interpreter.evaluate(IntegerDivideNode(IntNode(4), IntNode(3.0)))
        self.assertEqual(number, NumberValue(1.0))

        number = interpreter.evaluate(ExponentNode(IntNode(4), IntNode(3.0)))
        self.assertEqual(number, NumberValue(64.0))

        number = interpreter.evaluate(NegateNode(IntNode(4)))
        self.assertEqual(number, NumberValue(-4))

        number = interpreter.evaluate(PlusNode(IntNode(4)))
        self.assertEqual(number, NumberValue(4))

    def test_all(self):
        number = Interpreter().evaluate(SubtractNode(
            AddNode(ModNode(MultiplyNode(NegateNode(IntNode(1)),IntNode(2)),
                                         IntNode(2)),
                            DivideNode(FloatNode(3.0), IntNode(10))),
                    IntegerDivideNode(IntNode(4),
                                     ExponentNode(IntNode(1), IntNode(3)))))
        self.assertEqual(number, NumberValue(-3.7))
