from dataclasses import dataclass
from components import *

@dataclass
class NumberValue:
    value: float

    def __repr__(self):
        return f"{self.value}"

class Interpreter:
    def evaluate(self, expr):
        if type(expr) == Number:
            return NumberValue(expr.value)
        elif type(expr) == Add:
            return NumberValue((self.evaluate(expr.el1)).value + (self.evaluate(expr.el2)).value)
        elif type(expr) == Subtract:
            return NumberValue((self.evaluate(expr.el1)).value - (self.evaluate(expr.el2)).value)
        elif type(expr) == Multiply:
            return NumberValue((self.evaluate(expr.el1)).value * (self.evaluate(expr.el2)).value)
        elif type(expr) == Divide:
            try:
                return NumberValue((self.evaluate(expr.el1)).value / (self.evaluate(expr.el2)).value)
            except:
                raise Exception("Error: Cannot divide by 0")
        elif type(expr) == Mod:
            print("here")
            return NumberValue((self.evaluate(expr.el1)).value % (self.evaluate(expr.el2)).value)
        elif type(expr) == IntegerDivide:
            try:
                return NumberValue((self.evaluate(expr.el1)).value // (self.evaluate(expr.el2)).value)
            except:
                raise Exception("Error: Cannot divide by 0")
        elif type(expr) == Exponent:
            return NumberValue(self.evaluate(expr.el1).value ** self.evaluate(expr.el2).value)
        elif type(expr) == Plus:
            return NumberValue(self.evaluate())
        elif type(expr) == Minus:
            return NumberValue(-(self.evaluate(expr.exp)).value)
