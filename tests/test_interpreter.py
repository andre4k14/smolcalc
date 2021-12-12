# flake8: noqa
import unittest

from smolcalc.nodes import *
from smolcalc.interpreter import Interpreter
from smolcalc.values import Number


class TestInterpreter(unittest.TestCase):

    def test_numbers(self):
        value = Interpreter(False).visit(number_node(123.456))
        self.assertEqual(value, Number(123.456))

    def test_single_operations(self):
        result = Interpreter(False).visit(add_node(number_node(10), number_node(4.5)))
        self.assertEqual(result.value, 14.5)

        result = Interpreter(False).visit(subtract_node(number_node(10), number_node(4.5)))
        self.assertEqual(result.value, 5.5)

        result = Interpreter(False).visit(multiply_node(number_node(10), number_node(4.5)))
        self.assertEqual(result.value, 45)

        result = Interpreter(False).visit(divide_node(number_node(10), number_node(4.5)))
        self.assertAlmostEqual(result.value, 2.22222, 5)

        with self.assertRaises(Exception):
            Interpreter(False).visit(divide_node(number_node(10), number_node(0)))


if __name__ == '__main__':
    unittest.main()
