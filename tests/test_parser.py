# flake8: noqa
import unittest

from smolcalc.tokens import Token, TokenType
from smolcalc.lexer import Lexer
from smolcalc.parser_ import Parser
from smolcalc.nodes import *


class TestParser(unittest.TestCase):
    def test_empty(self):
        tokens = list(Lexer("", decimal_separator=".", tab_size=5).generate_tokens())
        node = Parser(tokens).parse()
        self.assertEqual(None, node)

    def test_numbers(self):
        tokens = list(Lexer("123.456", decimal_separator=".", tab_size=5).generate_tokens())
        node = Parser(tokens).parse()
        self.assertEqual(NumberNode(123.456), node)

    def test_expr(self):
        tokens = list(Lexer("123+12-34", decimal_separator=".", tab_size=5).generate_tokens())
        node = Parser(tokens).parse()
        self.assertEqual(SubtractNode(AddNode(NumberNode(123), NumberNode(12)), NumberNode(34)), node)

    def test_term(self):
        tokens = list(Lexer("69*45.03/0", decimal_separator=".", tab_size=5).generate_tokens())
        node = Parser(tokens).parse()
        self.assertEqual(DivideNode(MultiplyNode(NumberNode(69), NumberNode(45.03)), NumberNode(0)), node)

    def test_exponent(self):
        tokens = list(Lexer("2.3^34^0", decimal_separator=".", tab_size=5).generate_tokens())
        node = Parser(tokens).parse()
        self.assertEqual(ExponentNode(NumberNode(2.3), ExponentNode(NumberNode(34), NumberNode(0))), node)

    def test_factorial(self):
        tokens = list(Lexer("23!!", decimal_separator=".", tab_size=5).generate_tokens())
        node = Parser(tokens).parse()
        self.assertEqual(FactorialNode(FactorialNode(NumberNode(23))), node)

    def test_factor(self):
        tokens = list(Lexer("+23.1", decimal_separator=".", tab_size=5).generate_tokens())
        node = Parser(tokens).parse()
        self.assertEqual(PlusNode(NumberNode(23.1)), node)

        tokens = list(Lexer("-23", decimal_separator=".", tab_size=5).generate_tokens())
        node = Parser(tokens).parse()
        self.assertEqual(MinusNode(NumberNode(23)), node)

        tokens = list(Lexer("((23.8))", decimal_separator=".", tab_size=5).generate_tokens())
        node = Parser(tokens).parse()
        self.assertEqual((NumberNode(23.8)), node)

        tokens = list(Lexer("ln(ln(23.8))", decimal_separator=".", tab_size=5).generate_tokens())
        node = Parser(tokens).parse()
        self.assertEqual(NaturalLogarithmNode(NaturalLogarithmNode(NumberNode(23.8))), node)

        tokens = list(Lexer("lg(lg(23.8))", decimal_separator=".", tab_size=5).generate_tokens())
        node = Parser(tokens).parse()
        self.assertEqual(CommonLogarithmNode(CommonLogarithmNode(NumberNode(23.8))), node)

        tokens = list(Lexer("sqrt(sqrt(0234.08))", decimal_separator=".", tab_size=5).generate_tokens())
        node = Parser(tokens).parse()
        self.assertEqual(SquareRootNode(SquareRootNode(NumberNode(234.08))), node)

        with self.assertRaises(Exception):
            tokens = list(Lexer(")", decimal_separator=".", tab_size=5).generate_tokens())
            node = Parser(tokens).parse()

        with self.assertRaises(Exception):
            tokens = list(Lexer("()", decimal_separator=".", tab_size=5).generate_tokens())
            node = Parser(tokens).parse()

        with self.assertRaises(Exception):
            tokens = list(Lexer("(", decimal_separator=".", tab_size=5).generate_tokens())
            node = Parser(tokens).parse()

        with self.assertRaises(Exception):
            tokens = list(Lexer("ln(", decimal_separator=".", tab_size=5).generate_tokens())
            node = Parser(tokens).parse()

        with self.assertRaises(Exception):
            tokens = list(Lexer("lg(", decimal_separator=".", tab_size=5).generate_tokens())
            node = Parser(tokens).parse()

        with self.assertRaises(Exception):
            tokens = list(Lexer("sqrt(", decimal_separator=".", tab_size=5).generate_tokens())
            node = Parser(tokens).parse()

        with self.assertRaises(Exception):
            tokens = list(Lexer("+*/-", decimal_separator=".", tab_size=5).generate_tokens())
            node = Parser(tokens).parse()


if __name__ == '__main__':
    unittest.main()
