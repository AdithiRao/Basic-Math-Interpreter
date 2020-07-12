from dataclasses import dataclass

@dataclass
class Number:
    value: float

    def __repr__(self):
        return f"{self.value}"

@dataclass
class Add:
    el1: any
    el2: any

    def __repr__(self):
        return f"({self.el1}+{self.el2})"

@dataclass
class Subtract:
    el1: any
    el2: any

    def __repr__(self):
        return f"({self.el1}-{self.el2})"

@dataclass
class Multiply:
    el1: any
    el2: any

    def __repr__(self):
        return f"({self.el1}*{self.el2})"

@dataclass
class Divide:
    el1: any
    el2: any

    def __repr__(self):
        return f"({self.el1}/{self.el2})"

@dataclass
class Mod:
    el1: any
    el2: any

    def __repr__(self):
        return f"({self.el1}%{self.el2})"

@dataclass
class IntegerDivide:
    el1: any
    el2: any

    def __repr__(self):
        return f"({self.el1}//{self.el2})"

@dataclass
class Exponent:
    el1: any
    el2: any

    def __repr__(self):
        return f"({self.el1}^{self.el2})"


@dataclass
class Plus:
    exp: any

    def __repr__(self):
        return f"(+{self.exp})"

@dataclass
class Negate:
    exp: any

    def __repr__(self):
        return f"(-{self.exp})"
