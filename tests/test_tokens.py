import unittest

from smolcalc.tokens import Token, TokenType, tokens_to_string


class TestToken(unittest.TestCase):
    def test_repr(self):
        token = Token(TokenType.NUMBER, -85.7)
        self.assertEqual(repr(token), "NUMBER:-85.7")
        token = Token(TokenType.PLUS)
        self.assertEqual(repr(token), "PLUS")

    def test_if_in_tokens_to_string_dict(self):  # tests if all TokenType enums are in the dict
        for tt in TokenType:
            self.assertEqual(True, tt in tokens_to_string)


if __name__ == '__main__':
    unittest.main()
