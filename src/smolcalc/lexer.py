from smolcalc.tokens import Token, TokenType

WHITESPACE = ' \n\t'
DIGITS = '0123456789'


class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def raise_errors(self):
        raise Exception(f"Illegal character '{self.current_char}'")

    def generate_tokens(self):
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char == '.' or self.current_char in DIGITS:
                yield self.generate_number()
            elif self.current_char == 'p' or self.current_char == 'P':
                yield self.generate_pi()
            elif self.current_char == 'l' or self.current_char == 'L':
                yield self.generate_log()
            elif self.current_char == 's' or self.current_char == 'S':
                yield self.generate_sqrt()
            elif self.current_char == '!':
                yield self.generate_factorial()
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
                yield Token(TokenType.RPARPEN)
            else:
                self.raise_errors()

    def generate_number(self):
        number_str = self.current_char
        decimal_point_count = 0
        if number_str == '.':
            decimal_point_count = 1
        self.advance()
        while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
            if self.current_char == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break

            number_str += self.current_char
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
            return Token(TokenType.NUMBER, float('3.141592653589793'))

    def generate_log(self):
        log_str = self.current_char
        self.advance()
        if self.current_char == 'g' or self.current_char == 'G':
            log_str += self.current_char
            self.advance()
        elif self.current_char == 'n' or self.current_char == 'N':
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
        Lib_S = ['q', 'r', 't', '(']
        Lib_B = ['Q', 'R', 'T', '(']
        for x in range(len(Lib_S)):
            if self.current_char == Lib_S[x] or self.current_char == Lib_B[x]:
                sqrt_str += self.current_char
                self.advance()
            else:
                self.raise_errors()

        if str(sqrt_str).lower() == 'sqrt(':
            return Token(TokenType.SQUAREROOT)

    def generate_factorial(self):
        fac_str = self.current_char
        self.advance()
        if self.current_char == '(':
            fac_str += self.current_char
            self.advance()
        else:
            self.raise_errors()

        if str(fac_str) == '!(':
            return Token(TokenType.FACTORIAL)
