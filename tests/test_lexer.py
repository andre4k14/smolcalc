import unittest

from smolcalc.lexer import Lexer
from smolcalc.tokens import Token, TokenType


class TestLexer(unittest.TestCase):

    def test_empty(self):
        tokens = list(Lexer("", decimal_separator=".").generate_tokens())
        self.assertEqual(tokens, [])

    def test_whitespace(self):
        tokens = list(Lexer("_ \n\t", decimal_separator=".").generate_tokens())
        self.assertEqual(tokens, [])

    def test_numbers(self):
        tokens = list(Lexer("9 9.5 .9 9. .", decimal_separator=".").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 9.0),
            Token(TokenType.NUMBER, 9.5),
            Token(TokenType.NUMBER, 0.9),
            Token(TokenType.NUMBER, 9.0),
            Token(TokenType.NUMBER, 0.0)
        ])

    def test_const(self):
        tokens = list(Lexer("pi e", decimal_separator=".").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 3.141592653589793),
            Token(TokenType.NUMBER, 2.718281828459045)
        ])

    def test_operators(self):
        tokens = list(Lexer("+ - * / ^ ln( lg( sqrt( )! ( )", decimal_separator=".").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.PLUS),
            Token(TokenType.MINUS),
            Token(TokenType.MULTIPLY),
            Token(TokenType.DIVIDE),
            Token(TokenType.EXPONENT),
            Token(TokenType.NLOG),
            Token(TokenType.LOG_10),
            Token(TokenType.SQUARE_ROOT),
            Token(TokenType.FACTORIAL),
            Token(TokenType.L_BRACKET),
            Token(TokenType.R_BRACKET)
        ])


if __name__ == '__main__':
    unittest.main()
