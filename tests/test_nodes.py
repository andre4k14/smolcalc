import unittest

from smolcalc.nodes import AddNode, SubtractNode, MultiplyNode, DivideNode, ExponentNode, SquareRootNode, \
    NaturalLogarithmNode, CommonLogarithmNode, FactorialNode, NumberNode, PlusNode, MinusNode


class TestNodes(unittest.TestCase):
    def test_repr(self):
        node = NumberNode(34)
        self.assertEqual("34", repr(node))

        node = AddNode(NumberNode(34), NumberNode(1))
        self.assertEqual("(34+1)", repr(node))

        node = AddNode(AddNode(NumberNode(34), NumberNode(1)), NumberNode(1))
        self.assertEqual("((34+1)+1)", repr(node))

        node = SubtractNode(NumberNode(34), NumberNode(1))
        self.assertEqual("(34-1)", repr(node))

        node = MultiplyNode(NumberNode(34), NumberNode(-1))
        self.assertEqual("(34*-1)", repr(node))

        node = DivideNode(NumberNode(34), NumberNode(-1))
        self.assertEqual("(34/-1)", repr(node))

        node = ExponentNode(NumberNode(34), NumberNode(-1))
        self.assertEqual("(power(34,-1))", repr(node))

        node = SquareRootNode(NumberNode(34))
        self.assertEqual("(power(34,0.5))", repr(node))

        node = NaturalLogarithmNode(NumberNode(34))
        self.assertEqual("(ln(34))", repr(node))

        node = CommonLogarithmNode(NumberNode(34))
        self.assertEqual("(lg(34))", repr(node))

        node = FactorialNode(NumberNode(34))
        self.assertEqual("(factorial(34))", repr(node))

        node = MinusNode(NumberNode(34))
        self.assertEqual("(-34)", repr(node))

        node = PlusNode(NumberNode(34))
        self.assertEqual("(+34)", repr(node))


if __name__ == '__main__':
    unittest.main()
