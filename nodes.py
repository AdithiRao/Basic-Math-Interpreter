from dataclasses import dataclass

@dataclass
class IntNode:
    value: int

    def __repr__(self):
        return f"{self.value}"

@dataclass
class FloatNode:
    value: float

    def __repr__(self):
        return f"{self.value}"

@dataclass
class AddNode:
    el1: any
    el2: any

    def __repr__(self):
        return f"({self.el1}+{self.el2})"

@dataclass
class SubtractNode:
    el1: any
    el2: any

    def __repr__(self):
        return f"({self.el1}-{self.el2})"

@dataclass
class MultiplyNode:
    el1: any
    el2: any

    def __repr__(self):
        return f"({self.el1}*{self.el2})"

@dataclass
class DivideNode:
    el1: any
    el2: any

    def __repr__(self):
        return f"({self.el1}/{self.el2})"

@dataclass
class ModNode:
    el1: any
    el2: any

    def __repr__(self):
        return f"({self.el1}%{self.el2})"

@dataclass
class IntegerDivideNode:
    el1: any
    el2: any

    def __repr__(self):
        return f"({self.el1}//{self.el2})"

@dataclass
class ExponentNode:
    el1: any
    el2: any

    def __repr__(self):
        return f"({self.el1}^{self.el2})"


@dataclass
class PlusNode:
    exp: any

    def __repr__(self):
        return f"(+{self.exp})"

@dataclass
class NegateNode:
    exp: any

    def __repr__(self):
        return f"(-{self.exp})"
