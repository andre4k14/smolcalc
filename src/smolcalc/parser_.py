from typing import Union

from smolcalc.tokens import TokenType
from smolcalc.nodes import add_node, subtract_node, multiply_node, divide_node, exponent_node, square_root_node, \
    nlog_node, log_10_node, factorial_node, number_node, plus_node, minus_node

factor_types = Union[square_root_node, nlog_node, log_10_node, factorial_node, number_node, plus_node, minus_node]
exponent_types = Union[factor_types, exponent_node]
terms_types = Union[exponent_types, multiply_node, divide_node]
expr_types = Union[terms_types, add_node, subtract_node]


class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = iter(tokens)
        self.advance()

    def raise_error(self) -> None:
        raise Exception("Invalid syntax")

    def advance(self) -> None:
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self) -> Union[expr_types, None]:
        if self.current_token is None:
            return None

        result = self.expr()

        if self.current_token is not None:
            self.raise_error()
        return result

    def expr(self) -> expr_types:
        result = self.term()

        while self.current_token is not None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            if self.current_token.type == TokenType.PLUS:
                self.advance()
                result = add_node(result, self.term())
            else:
                self.advance()
                result = subtract_node(result, self.term())

        return result

    def term(self) -> expr_types:
        result = self.exponent()

        while self.current_token is not None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = multiply_node(result, self.exponent())
            else:
                self.advance()
                result = divide_node(result, self.exponent())

        return result

    def exponent(self) -> expr_types:
        result = self.factor()

        while self.current_token is not None and self.current_token.type == TokenType.EXPONENT:
            self.advance()
            result = exponent_node(result, self.exponent())

        return result

    def factor(self) -> expr_types:  # type: ignore
        token = self.current_token

        if token is None:  # maybe that could be prettier in another version
            self.raise_error()

        if token.type == TokenType.SQUARE_ROOT:
            self.advance()
            result = self.expr()

            if self.current_token is not None and self.current_token.type == TokenType.R_BRACKET:
                self.advance()
                return square_root_node(result)

            self.raise_error()

        if token.type == TokenType.NLOG:
            self.advance()
            result = self.expr()

            if self.current_token is not None and self.current_token.type == TokenType.R_BRACKET:
                self.advance()
                return nlog_node(result)

            self.raise_error()

        if token.type == TokenType.LOG_10:
            self.advance()
            result = self.expr()

            if self.current_token is not None and self.current_token.type == TokenType.R_BRACKET:
                self.advance()
                return log_10_node(result)

            self.raise_error()

        if token.type == TokenType.L_BRACKET:
            self.advance()
            result = self.expr()

            if self.current_token is not None and self.current_token.type == TokenType.R_BRACKET:
                self.advance()
                return result
            elif self.current_token is not None and self.current_token.type == TokenType.FACTORIAL:
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
