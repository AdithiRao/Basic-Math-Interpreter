from enum import Enum
from dataclasses import dataclass
# Citation: https://www.youtube.com/watch?v=88lmIMHhYNs

class TokenType(Enum):
    INT       = 0
    FLOAT     = 1
    PLUS      = 2
    MINUS     = 3
    DIVIDE    = 4
    MULTIPLY  = 5
    MOD       = 6
    LPAREN    = 7
    RPAREN    = 8
    EXPONENT  = 9
    INTDIVIDE = 10


@dataclass
class Token():
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value != None else "")
