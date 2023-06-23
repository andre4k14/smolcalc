from typing import Generator, Optional

from smolcalc.tokens import Token, TokenType

IGNORE = "_"
WHITESPACE = " \n\t" + IGNORE
DIGITS = "0123456789"
OPERATORS = "+-*/^!()"


class Lexer:
    def __init__(self, text: str, decimal_separator: str, tab_size: int) -> None:
        self.decimal_separator: str = decimal_separator
        self.tab_size = tab_size
        self.text = iter(text)
        self.position_char: int = 0
        self.count_columns: int = 0
        self.count_lines: int = 1
        self.advance()

    def advance(self) -> None:
        try:
            self.current_char: str = next(self.text)
            self.position_char += 1
            self.count_columns += 1
            if self.current_char in WHITESPACE:
                if self.current_char == "\n":
                    self.count_columns = 0
                    self.count_lines += 1

                if self.current_char == "\t":
                    self.count_columns += (self.tab_size - 1)

        except StopIteration:
            self.current_char = None  # type: ignore

    def raise_errors(self, error_msg: Optional[str] = None) -> None:
        if (self.current_char is None or self.current_char in OPERATORS) and error_msg is not None:
            raise Exception(f"Invalid syntax, ERROR: {error_msg}")
        raise Exception(
            f"Illegal character at position (Ln:{self.count_lines}, Col:{self.count_columns}, Pos:{self.position_char}) '{self.current_char}'")

    def generate_tokens(self) -> Generator[Optional[Token], None, None]:
        while self.current_char is not None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char == self.decimal_separator or self.current_char in DIGITS:
                yield self.generate_number()
            elif self.current_char.lower() == "p":
                yield self.generate_pi()
            elif self.current_char.lower() == "l":
                yield self.generate_log()
            elif self.current_char.lower() == "s":
                yield self.generate_sqrt()
            elif self.current_char.lower() == "e":
                self.advance()
                yield Token(TokenType.NUMBER, float("2.718281828459045"))
            elif self.current_char == "!":
                self.advance()
                yield Token(TokenType.FACTORIAL)
            elif self.current_char == '^':
                self.advance()
                yield Token(TokenType.EXPONENT)
            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.L_BRACKET)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.R_BRACKET)
            else:
                self.raise_errors()

    def generate_number(self) -> Token:
        number_str = "." if self.current_char == self.decimal_separator else self.current_char
        decimal_separator_count = 0
        if number_str == self.decimal_separator:
            decimal_separator_count = 1
        self.advance()
        while self.current_char is not None and (
                self.current_char == self.decimal_separator or self.current_char in DIGITS or self.current_char in IGNORE):
            if self.current_char not in IGNORE:
                if self.current_char == self.decimal_separator:
                    decimal_separator_count += 1
                    if decimal_separator_count > 1:
                        break
                number_str += "." if self.current_char == self.decimal_separator else self.current_char
                self.advance()
            else:
                self.advance()

        if number_str.startswith('.'):
            number_str = '0' + number_str
        if number_str.endswith('.'):
            number_str += '0'

        return Token(TokenType.NUMBER, float(number_str))

    def generate_pi(self) -> Token:
        self.advance()
        if self.current_char == 'i' or self.current_char == 'I':
            self.advance()
        else:
            self.raise_errors(f"Illegal character at position (Ln:{self.count_lines}, Col:{self.count_columns},"
                              f" Pos:{self.position_char}) '{self.current_char}'\nExpected I or i got {self.current_char}")

        return Token(TokenType.NUMBER, float("3.141592653589793"))

    def generate_log(self) -> Token:  # type: ignore
        log_str = self.current_char
        self.advance()

        if self.current_char is not None and self.current_char.lower() == "g":
            log_str += self.current_char
            self.advance()
        elif self.current_char is not None and self.current_char.lower() == "n":
            log_str += self.current_char
            self.advance()
        else:
            self.raise_errors(f"Illegal character at position (Ln:{self.count_lines}, Col:{self.count_columns},"
                              f" Pos:{self.position_char}) '{self.current_char}'\nExpected g or n got {self.current_char}")

        if self.current_char == '(':
            log_str += self.current_char
        else:
            self.raise_errors(f"Illegal character at position (Ln:{self.count_lines}, Col:{self.count_columns},"
                              f" Pos:{self.position_char}) '{self.current_char}'\nExpected ( got {self.current_char}")

        if str(log_str).lower() == 'ln(':
            self.advance()
            return Token(TokenType.NLOG)
        else:
            self.advance()
            return Token(TokenType.LOG_10)

    def generate_sqrt(self) -> Token:
        self.advance()
        chars = ['q', 'r', 't', '(']
        for x in range(len(chars)):
            if self.current_char is not None and self.current_char.lower() == chars[x]:
                self.advance()
            else:
                self.raise_errors(f"Illegal character at position (Ln:{self.count_lines}, Col:{self.count_columns},"
                                  f" Pos:{self.position_char}) '{self.current_char}'\nExpected {chars[x]} got {self.current_char}")

        return Token(TokenType.SQUARE_ROOT)
