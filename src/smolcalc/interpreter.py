from smolcalc.values import Number
from smolcalc.nodes import Expression


class Interpreter:

    def __init__(self, special) -> None:
        self.special: bool = special

    def evaluate(self, node: Expression) -> Number:
        return node.evaluate(special=self.special)
