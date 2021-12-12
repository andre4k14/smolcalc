import unittest

from smolcalc.nodes import add_node, subtract_node, multiply_node, divide_node, exponent_node, square_root_node, \
    nlog_node, log_10_node, factorial_node, number_node, plus_node, minus_node


class TestNodes(unittest.TestCase):
    def test_repr(self):
        node = number_node(34)
        self.assertEqual(repr(node), "34")

        node = add_node(34, 1)
        self.assertEqual(repr(node), "(34+1)")

        node = add_node(add_node(34, 1), 1)
        self.assertEqual(repr(node), "((34+1)+1)")

        node = subtract_node(34, 1)
        self.assertEqual(repr(node), "(34-1)")

        node = multiply_node(34, -1)
        self.assertEqual(repr(node), "(34*-1)")

        node = divide_node(34, -1)
        self.assertEqual(repr(node), "(34/-1)")

        node = exponent_node(34, -1)
        self.assertEqual(repr(node), "(power(34,-1))")

        node = square_root_node(34)
        self.assertEqual(repr(node), "(power(34,0.5))")

        node = nlog_node(34)
        self.assertEqual(repr(node), "(log(34))")

        node = log_10_node(34)
        self.assertEqual(repr(node), "(log10(34))")

        node = factorial_node(34)
        self.assertEqual(repr(node), "(factorial(34))")

        node = minus_node(34)
        self.assertEqual(repr(node), "(-34)")

        node = plus_node(34)
        self.assertEqual(repr(node), "(+34)")

        node = plus_node(number_node(34))
        self.assertEqual(repr(node), "(+34)")


if __name__ == '__main__':
    unittest.main()
