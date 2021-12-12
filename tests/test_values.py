import unittest

from smolcalc.values import Number


class TestValues(unittest.TestCase):
    def test_repr(self):
        number = Number(-85.7)
        self.assertEqual(repr(number), "-85.7")

    def test_str(self):
        number = Number(-85.7)
        self.assertEqual(str(number), "-85.7")
        number = Number(765878769.0)
        self.assertEqual(str(number), "765878769")
        number = Number(12e10)
        self.assertEqual(str(number), "120000000000")


if __name__ == '__main__':
    unittest.main()
