from enum import Enum
from dataclasses import dataclass
from nodes import *

class NumberType(Enum):
    float
    int

@dataclass
class NumberValue:
    value: NumberType

    def __repr__(self):
        return f"{self.value}"

class Interpreter:
    def evaluate(self, expr):
        if type(expr) == FloatNode or type(expr) == IntNode:
            return NumberValue(expr.value)
        elif type(expr) == AddNode:
            return NumberValue((self.evaluate(expr.el1)).value + (self.evaluate(expr.el2)).value)
        elif type(expr) == SubtractNode:
            return NumberValue((self.evaluate(expr.el1)).value - (self.evaluate(expr.el2)).value)
        elif type(expr) == MultiplyNode:
            return NumberValue((self.evaluate(expr.el1)).value * (self.evaluate(expr.el2)).value)
        elif type(expr) == DivideNode:
            try:
                return NumberValue((self.evaluate(expr.el1)).value / (self.evaluate(expr.el2)).value)
            except:
                raise Exception("Error: Cannot divide by 0")
        elif type(expr) == ModNode:
            print("here")
            return NumberValue((self.evaluate(expr.el1)).value % (self.evaluate(expr.el2)).value)
        elif type(expr) == IntegerDivideNode:
            try:
                return NumberValue((self.evaluate(expr.el1)).value // (self.evaluate(expr.el2)).value)
            except:
                raise Exception("Error: Cannot divide by 0")
        elif type(expr) == ExponentNode:
            return NumberValue(self.evaluate(expr.el1).value ** self.evaluate(expr.el2).value)
        elif type(expr) == PlusNode:
            return NumberValue(self.evaluate(expr.exp).value)
        elif type(expr) == NegateNode:
            return NumberValue(-(self.evaluate(expr.exp)).value)
