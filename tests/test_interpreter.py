# flake8: noqa
import unittest

from smolcalc.nodes import *
from smolcalc.interpreter import Interpreter
from smolcalc.values import Number
from smolcalc.constants import PI, euler_s_number


class TestInterpreter(unittest.TestCase):

    def test_numbers(self):
        value = Interpreter(False).evaluate(NumberNode(123.456))
        self.assertEqual(value, Number(123.456))

    def test_binary_operations(self):
        result = Interpreter(False).evaluate(AddNode(NumberNode(120), NumberNode(4.5)))
        self.assertEqual(result.value, 124.5)
        result = Interpreter(False).evaluate(AddNode(NumberNode(120), NumberNode(0)))
        self.assertEqual(result.value, 120)

        result = Interpreter(False).evaluate(SubtractNode(NumberNode(20), NumberNode(24.5)))
        self.assertEqual(result.value, -4.5)

        result = Interpreter(False).evaluate(MultiplyNode(NumberNode(13), NumberNode(4.5)))
        self.assertEqual(result.value, 58.5)
        result = Interpreter(False).evaluate(MultiplyNode(NumberNode(13), NumberNode(-4.5)))
        self.assertEqual(result.value, -58.5)
        result = Interpreter(False).evaluate(MultiplyNode(NumberNode(-13), NumberNode(4.5)))
        self.assertEqual(result.value, -58.5)
        result = Interpreter(False).evaluate(MultiplyNode(NumberNode(-13), NumberNode(-4.5)))
        self.assertEqual(result.value, 58.5)
        result = Interpreter(False).evaluate(MultiplyNode(NumberNode(1123), NumberNode(1.0)))
        self.assertEqual(result.value, 1123)

        result = Interpreter(False).evaluate(DivideNode(NumberNode(10), NumberNode(4.5)))
        self.assertAlmostEqual(result.value, 2.22222, 5)
        result = Interpreter(False).evaluate(DivideNode(NumberNode(10), NumberNode(-4.5)))
        self.assertAlmostEqual(result.value, -2.22222, 5)
        result = Interpreter(False).evaluate(DivideNode(NumberNode(-10), NumberNode(4.5)))
        self.assertAlmostEqual(result.value, -2.22222, 5)
        result = Interpreter(False).evaluate(DivideNode(NumberNode(-10), NumberNode(-4.5)))
        self.assertAlmostEqual(result.value, 2.22222, 5)

        with self.assertRaises(Exception):
            Interpreter(False).evaluate(DivideNode(NumberNode(10), NumberNode(0)))

        result = Interpreter(False).evaluate(ExponentNode(NumberNode(13), NumberNode(1.0)))
        self.assertEqual(result.value, 13)
        result = Interpreter(False).evaluate(ExponentNode(NumberNode(-231.3), NumberNode(0.0)))
        self.assertEqual(result.value, 1)
        result = Interpreter(False).evaluate(ExponentNode(NumberNode(1123), NumberNode(1.0)))
        self.assertEqual(result.value, 1123)

        with self.assertRaises(Exception):
            Interpreter(False).evaluate(ExponentNode(NumberNode(0), NumberNode(0)))

    def test_unary_operations(self):
        result = Interpreter(False).evaluate(MinusNode(NumberNode(4.53)))
        self.assertEqual(result.value, -4.53)
        result = Interpreter(False).evaluate(MinusNode(NumberNode(-4.53)))
        self.assertEqual(result.value, 4.53)

        result = Interpreter(False).evaluate(PlusNode(NumberNode(-4.53)))
        self.assertEqual(result.value, -4.53)
        result = Interpreter(False).evaluate(PlusNode(NumberNode(4.53)))
        self.assertEqual(result.value, 4.53)

        result = Interpreter(False).evaluate(SquareRootNode(NumberNode(16)))
        self.assertEqual(result.value, 4)
        result = Interpreter(False).evaluate(SquareRootNode(NumberNode(1)))
        self.assertEqual(result.value, 1)
        result = Interpreter(False).evaluate(SquareRootNode(NumberNode(0)))
        self.assertEqual(result.value, 0)

        with self.assertRaises(Exception):
            Interpreter(False).evaluate(SquareRootNode(NumberNode(-10)))

        result = Interpreter(False).evaluate(NaturalLogarithmNode(NumberNode(euler_s_number)))
        self.assertEqual(result.value, 1)
        result = Interpreter(False).evaluate(NaturalLogarithmNode(NumberNode(123424)))
        self.assertAlmostEqual(result.value, 11.72338086)

        with self.assertRaises(Exception):
            Interpreter(False).evaluate(NaturalLogarithmNode(NumberNode(0)))
        with self.assertRaises(Exception):
            Interpreter(False).evaluate(NaturalLogarithmNode(NumberNode(-10)))

        result = Interpreter(False).evaluate(CommonLogarithmNode(NumberNode(10)))
        self.assertEqual(result.value, 1)
        result = Interpreter(False).evaluate(CommonLogarithmNode(NumberNode(100)))
        self.assertEqual(result.value, 2)

        with self.assertRaises(Exception):
            Interpreter(False).evaluate(CommonLogarithmNode(NumberNode(0)))
        with self.assertRaises(Exception):
            Interpreter(False).evaluate(CommonLogarithmNode(NumberNode(-10)))

        result = Interpreter(False).evaluate(FactorialNode(NumberNode(5)))
        self.assertEqual(result.value, 120)
        result = Interpreter(False).evaluate(FactorialNode(NumberNode(0)))
        self.assertEqual(result.value, 1)
        result = Interpreter(True).evaluate(FactorialNode(NumberNode(PI)))
        self.assertAlmostEqual(result.value, 2.288037795340032)

        with self.assertRaises(Exception):
            Interpreter(False).evaluate(FactorialNode(NumberNode(-10)))


if __name__ == '__main__':
    unittest.main()
