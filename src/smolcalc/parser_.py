from typing import Union, Optional, Generator

from smolcalc.tokens import TokenType, Token, tokens_to_string
from smolcalc.nodes import AddNode, SubtractNode, MultiplyNode, DivideNode, ExponentNode, SquareRootNode, \
    NaturalLogarithmNode, CommonLogarithmNode, FactorialNode, NumberNode, PlusNode, MinusNode

factor_types = Union[
    SquareRootNode, NaturalLogarithmNode, CommonLogarithmNode, FactorialNode, NumberNode, PlusNode, MinusNode]
exponent_types = Union[factor_types, ExponentNode]
terms_types = Union[exponent_types, MultiplyNode, DivideNode]
expr_types = Union[terms_types, AddNode, SubtractNode]


class Parser:
    def __init__(self, tokens: Generator[Optional[Token], None, None]) -> None:
        self.tokens = iter(tokens)
        self.advance()

    def raise_error(self, error_msg: Optional[str] = None) -> None:
        if error_msg is not None:
            raise Exception(f"Invalid syntax, ERROR: {error_msg}")
        else:
            raise Exception("Invalid syntax")

    def raise_r_bracket_error(self) -> None:
        self.raise_error(f"Expected {tokens_to_string[TokenType.R_BRACKET]} got {None}")

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
                result = AddNode(result, self.term())
            else:
                self.advance()
                result = SubtractNode(result, self.term())

        return result

    def term(self) -> expr_types:
        result = self.exponent()

        while self.current_token is not None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            if self.current_token.type == TokenType.MULTIPLY:
                self.advance()
                result = MultiplyNode(result, self.exponent())
            else:
                self.advance()
                result = DivideNode(result, self.exponent())

        return result

    def exponent(self) -> expr_types:
        result = self.factorial()

        while self.current_token is not None and self.current_token.type == TokenType.EXPONENT:
            self.advance()
            result = ExponentNode(result, self.exponent())

        return result

    def factorial(self) -> expr_types:
        result = self.factor()

        while self.current_token is not None and self.current_token.type == TokenType.FACTORIAL:
            self.advance()
            result = FactorialNode(result)

        return result

    def factor(self) -> expr_types:  # type: ignore
        token = self.current_token

        if token is None:  # maybe that could be prettier in another version
            self.raise_error()
        else:  # because mypy doesn't know that if token is None the rest of the code doesn't execute

            if token.type == TokenType.SQUARE_ROOT:
                self.advance()
                result = self.expr()

                if self.current_token is not None and self.current_token.type == TokenType.R_BRACKET:
                    self.advance()
                    return SquareRootNode(result)

                self.raise_r_bracket_error()

            if token.type == TokenType.NLOG:
                self.advance()
                result = self.expr()

                if self.current_token is not None and self.current_token.type == TokenType.R_BRACKET:
                    self.advance()
                    return NaturalLogarithmNode(result)

                self.raise_r_bracket_error()

            if token.type == TokenType.LOG_10:
                self.advance()
                result = self.expr()

                if self.current_token is not None and self.current_token.type == TokenType.R_BRACKET:
                    self.advance()
                    return CommonLogarithmNode(result)

                self.raise_r_bracket_error()

            if token.type == TokenType.L_BRACKET:
                self.advance()
                result = self.expr()

                if self.current_token is not None and self.current_token.type == TokenType.R_BRACKET:
                    self.advance()
                    return result

                self.raise_r_bracket_error()

            elif token.type == TokenType.NUMBER:
                self.advance()
                return NumberNode(token.value)  # type: ignore

            elif token.type == TokenType.PLUS:
                self.advance()
                return PlusNode(self.expr())

            elif token.type == TokenType.MINUS:
                self.advance()
                return MinusNode(self.expr())

            self.raise_error(f"Unexpected character '{tokens_to_string[token.type]}'")
