from smolcalc.values import Number
from smolcalc.nodes import *
import math
class Interpreter:
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

    def raise_error_complex_numbers(self):
        return Exception("math domain error (complex numbers not supported)")


    def visit_NumberNode(self, node):
        return Number(node.value)

    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_SubtractNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def visit_DivideNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except:
            raise Exception("runtime math error (Division by zero)")

    def visit_PlusNode(self, node):
        return self.visit(node.node)

    def visit_MinusNode(self, node):
        return Number(-self.visit(node.node).value)

    def visit_ExponentNode(self, node):
        if self.visit(node.node_a).value == 0 and self.visit(node.node_a).value == 0:
            raise Exception("0^0 is undefined.")
        return Number(math.pow(self.visit(node.node_a).value,self.visit(node.node_b).value))

    def visit_SquarerootNode(self, node):
        if self.visit(node.node).value < 0:
            return self.raise_error_complex_numbers()

        return Number(math.pow(self.visit(node.node).value,0.5))

    def visit_NLOG_Node(self, node):
        if self.visit(node.node).value <= 0:
            return self.raise_error_complex_numbers()

        return Number(math.log(self.visit(node.node).value))

    def visit_LOG_10_Node(self, node):
        if self.visit(node.node).value <= 0:
            return self.raise_error_complex_numbers()

        return Number(math.log10(self.visit(node.node).value))

    def visit_FactorialNode(self,node):
        if not isinstance(self.visit(node.node).value, int) and not self.visit(node.node).value.is_integer():
            raise Exception("runtime math error (only whole numbers)")
        if self.visit(node.node).value < 0:
            raise Exception("runtime math error (no negative numbers)")

        return Number(math.factorial(int(self.visit(node.node).value)))

