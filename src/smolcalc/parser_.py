from smolcalc.tokens import TokenType
from smolcalc.nodes import *


class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()

    def raise_error(self):
        raise Exception("Invalid syntax")

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        if self.current_token is None:
            return None

        result = self.expr()

        if self.current_token is not None:
            self.raise_error()
        return result

    def expr(self):
        result = self.term()

        while self.current_token is not None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                result = add_node(result, self.term())
            elif self.current_token.type == TokenType.MINUS:
                self.advance()
                result = subtract_node(result, self.term())

        return result

    def term(self):
        result = self.exponent()

        while self.current_token is not None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = multiply_node(result, self.exponent())
            elif self.current_token.type == TokenType.DIVIDE:
                self.advance()
                result = divide_node(result, self.exponent())

        return result

    def exponent(self):
        result = self.factor()

        while self.current_token is not None and self.current_token.type == TokenType.EXPONENT:
            self.advance()
            result = exponent_node(result, self.exponent())

        return result

    def factor(self):
        token = self.current_token

        if token is None:  # maybe that could be prettier in another version
            self.raise_error()

        if token.type == TokenType.SQUAREROOT:
            self.advance()
            result = self.expr()

            if self.current_token.type != TokenType.RPARPEN:
                self.raise_error()

            self.advance()
            return square_root_node(result)

        if token.type == TokenType.NLOG:
            self.advance()
            result = self.expr()

            if self.current_token.type != TokenType.RPARPEN:
                self.raise_error()

            self.advance()
            return nlog_node(result)

        if token.type == TokenType.LOG_10:
            self.advance()
            result = self.expr()

            if self.current_token.type != TokenType.RPARPEN:
                self.raise_error()

            self.advance()
            return log_10_node(result)

        if token.type == TokenType.LPARPEN:
            self.advance()
            result = self.expr()

            if self.current_token.type == TokenType.RPARPEN:
                self.advance()
                return result
            elif self.current_token.type == TokenType.FACTORIAL:
                self.advance()
                return factorial_node(result)

            self.raise_error()

        elif token.type == TokenType.NUMBER:
            self.advance()
            return number_node(token.value)

        elif token.type == TokenType.PLUS:
            self.advance()
            return plus_node(self.factor())

        elif token.type == TokenType.MINUS:
            self.advance()
            return minus_node(self.factor())

        self.raise_error()
