import unittest

from smolcalc.tokens import Token, TokenType
from smolcalc.parser_ import Parser
from smolcalc.nodes import *


class TestParser(unittest.TestCase):
    def test_empty(self):
        tokens = []
        node = Parser(tokens).parse()
        self.assertEqual(node, None)

    def test_numbers(self):
        tokens = [Token(TokenType.NUMBER, 123.456)]
        node = Parser(tokens).parse()
        self.assertEqual(node, number_node(123.456))


if __name__ == '__main__':
    unittest.main()
