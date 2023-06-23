from typing import Optional

from enum import Enum, auto
from dataclasses import dataclass


class TokenType(Enum):
    NUMBER = auto()
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    L_BRACKET = auto()
    R_BRACKET = auto()
    FACTORIAL = auto()
    EXPONENT = auto()
    NLOG = auto()
    LOG_10 = auto()
    SQUARE_ROOT = auto()


tokens_to_string = {
    TokenType.NUMBER: "number",
    TokenType.PLUS: "+",
    TokenType.MINUS: "-",
    TokenType.MULTIPLY: "*",
    TokenType.DIVIDE: "/",
    TokenType.L_BRACKET: "(",
    TokenType.R_BRACKET: ")",
    TokenType.FACTORIAL: "!",
    TokenType.EXPONENT: "^",
    TokenType.NLOG: "ln(",
    TokenType.LOG_10: "lg(",
    TokenType.SQUARE_ROOT: "sqrt("
}


@dataclass
class Token:
    type: TokenType
    value: Optional[float] = None

    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value is not None else "")
