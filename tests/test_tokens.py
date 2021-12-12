import unittest

from smolcalc.tokens import Token, TokenType


class TestToken(unittest.TestCase):
    def test_repr(self):
        token = Token(TokenType.NUMBER, -85.7)
        self.assertEqual(repr(token), "NUMBER:-85.7")
        token = Token(TokenType.PLUS)
        self.assertEqual(repr(token), "PLUS")


if __name__ == '__main__':
    unittest.main()
