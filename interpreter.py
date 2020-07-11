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
            return Number(expr.value)
        elif type(expr) == Add:
            Number((self.evaluate(expr.el1)).value + (self.evaluate(expr.el2)).value)
        elif type(expr) == Subtract:
            Number((self.evaluate(expr.el1)).value - (self.evaluate(expr.el2)).value)
        elif type(expr) == Multiply:
            Number((self.evaluate(expr.el1)).value * (self.evaluate(expr.el2)).value)
        elif type(expr) == Divide:
            try:
                Number((self.evaluate(expr.el1)).value / (self.evaluate(expr.el2)).value)
            except:
                raise Exception("Error: Cannot divide by 0")
        elif type(expr) == Plus:
            Number(self.evaluate())
        elif type(expr) == Minus:
            Number(-(self.evaluate(expr.exp)).value)
