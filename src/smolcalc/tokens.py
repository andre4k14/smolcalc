from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    LPARPEN = 5
    RPARPEN = 6
    FACTORIAL = 7
    EXPONENT = 8
    NLOG = 9
    LOG_10 = 10
    SQUAREROOT = 11


@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value != None else "")
