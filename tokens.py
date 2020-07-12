from enum import Enum
from dataclasses import dataclass
# Citation: https://www.youtube.com/watch?v=88lmIMHhYNs

class TokenType(Enum):
    NUMBER    = 0
    PLUS      = 1
    MINUS     = 2
    DIVIDE    = 3
    MULTIPLY  = 4
    MOD       = 5
    LPAREN    = 6
    RPAREN    = 7
    EXPONENT  = 8
    INTDIVIDE = 9


@dataclass
class Token():
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value != None else "")
