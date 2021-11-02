from smolcalc.tokens import Token, TokenType

IGNORE = "_"
WHITESPACE = " \n\t" + IGNORE
DIGITS = "0123456789"
OPERATORS = "+-*/^!()"


class Lexer:
    def __init__(self, text, decimal_separator):
        self.decimal_separator = decimal_separator
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def raise_errors(self):
        if self.current_char is None or  self.current_char in OPERATORS:
            raise Exception("Invalid syntax")
        raise Exception(f"Illegal character '{self.current_char}'")

    def generate_tokens(self):
        while self.current_char is not None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char == self.decimal_separator or self.current_char in DIGITS:
                num = self.generate_number()
                if self.current_char == '!':
                    self.advance()
                    yield Token(TokenType.LPARPEN)
                    yield num
                    yield Token(TokenType.FACTORIAL)
                else:
                    yield num
            elif self.current_char.lower() == "p":
                yield self.generate_pi()
            elif self.current_char.lower() == "l":
                yield self.generate_log()
            elif self.current_char.lower() == "s":
                yield self.generate_sqrt()
            elif self.current_char.lower() == "e":
                self.advance()
                yield Token(TokenType.NUMBER, float("2.718281828459045"))
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
                yield Token(TokenType.LPARPEN)
            elif self.current_char == ')':
                self.advance()
                if self.current_char == '!':
                    self.advance()
                    yield Token(TokenType.FACTORIAL)
                else:
                    yield Token(TokenType.RPARPEN)
            else:
                self.raise_errors()

    def generate_number(self):
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

    def generate_pi(self):
        pi_str = self.current_char
        self.advance()
        if self.current_char == 'i' or self.current_char == 'I':
            pi_str += self.current_char
            self.advance()
        else:
            self.raise_errors()

        if str(pi_str).lower() == 'pi':
            return Token(TokenType.NUMBER, float("3.141592653589793"))

    def generate_log(self):
        log_str = self.current_char
        self.advance()
        if self.current_char.lower() == "g":
            log_str += self.current_char
            self.advance()
        elif self.current_char.lower() == "n":
            log_str += self.current_char
            self.advance()

        else:
            self.raise_errors()

        if self.current_char == '(':
            log_str += self.current_char
            if str(log_str).lower() == 'ln(':
                self.advance()
                return Token(TokenType.NLOG)
            elif str(log_str).lower() == 'lg(':
                self.advance()
                return Token(TokenType.LOG_10)
        else:
            self.raise_errors()

    def generate_sqrt(self):
        sqrt_str = self.current_char
        self.advance()
        chars = ['q', 'r', 't', '(']
        for x in range(len(chars)):
            if self.current_char is not None and self.current_char.lower() == chars[x]:
                sqrt_str += self.current_char
                self.advance()
            else:
                self.raise_errors()

        if str(sqrt_str).lower() == 'sqrt(':
            return Token(TokenType.SQUAREROOT)

