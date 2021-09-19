from smolcalc.values import Number
from smolcalc.nodes import *
import math
class Interpreter:
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

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
            raise Exception("Runtime math error")

    def visit_PlusNode(self, node):
        return self.visit(node.node)

    def visit_MinusNode(self, node):
        return Number(-self.visit(node.node).value)

    def visit_ExponentNode(self, node):
        if node.node_a == 0 and node.node_b == 0:
            raise Exception("0^0 ist Undefiniert.")
        return Number(math.pow(self.visit(node.node_a).value,self.visit(node.node_b).value))

    def visit_SquarerootNode(self, node):
        return Number(math.pow(self.visit(node.node).value,0.5))

    def visit_NLOG_Node(self, node):
        return Number(math.log(self.visit(node.node).value))

    def visit_LOG_10_Node(self, node):
        return Number(math.log10(self.visit(node.node).value))

    def visit_FactorialNode(self,node):
        if not self.visit(node.node).value.is_integer():
            raise Exception("Man kann nur ganze Zahl bei Factorial einsetzen")
        return Number(math.factorial(int(self.visit(node.node).value)))

