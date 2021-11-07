from smolcalc.values import Number

import math
import operator


class Interpreter:

    def __init__(self, special):
        self.special: bool = special

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

    def raise_error_complex_numbers(self):
        return Exception("math domain error (complex numbers not supported)")

    def visit_number_node(self, node):
        return Number(node.value)

    def visit_add_node(self, node):
        return Number(operator.add(self.visit(node.node_a).value, self.visit(node.node_b).value))

    def visit_subtract_node(self, node):
        return Number(operator.sub(self.visit(node.node_a).value, self.visit(node.node_b).value))

    def visit_multiply_node(self, node):
        return Number(operator.mul(self.visit(node.node_a).value, self.visit(node.node_b).value))

    def visit_divide_node(self, node):
        try:
            return Number(operator.truediv(self.visit(node.node_a).value, self.visit(node.node_b).value))
        except ZeroDivisionError:
            raise Exception("runtime math error (Division by zero)")

    def visit_plus_node(self, node):
        return self.visit(node.node)

    def visit_minus_node(self, node):
        return Number(operator.neg(self.visit(node.node).value))

    def visit_exponent_node(self, node):
        value_a = self.visit(node.node_a).value
        value_b = self.visit(node.node_b).value

        if value_a == 0 and value_b == 0:
            raise Exception("0^0 is undefined.")
        return Number(math.pow(value_a, value_b))

    def visit_square_root_node(self, node):
        value = self.visit(node.node).value
        if value < 0:
            return self.raise_error_complex_numbers()

        return Number(math.pow(value, 0.5))

    def visit_nlog_node(self, node):
        value = self.visit(node.node).value
        if value <= 0:
            return self.raise_error_complex_numbers()

        return Number(math.log(value))

    def visit_log_10_node(self, node):
        value = self.visit(node.node).value
        if value <= 0:
            return self.raise_error_complex_numbers()

        return Number(math.log10(value))

    def visit_factorial_node(self, node):
        value = self.visit(node.node).value
        if not isinstance(value, int) and not value.is_integer() and not self.special:
            raise Exception("runtime math error (only whole numbers)")
        if value < 0 and not self.special:
            raise Exception("runtime math error (no negative numbers)")

        return Number(math.gamma(value + 1))
