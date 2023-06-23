from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod

import math
import operator

from smolcalc.values import Number


def raise_error_complex_numbers() -> None:
    raise Exception("math domain error (complex numbers not supported)")


class Expression(ABC):
    @abstractmethod
    def evaluate(self, **x_para) -> Number:  # pragma: no cover
        raise NotImplementedError


@dataclass
class NumberNode(Expression):
    value: float

    def __repr__(self, ):
        return f"{self.value}"

    def evaluate(self, **x_para) -> Number:
        return Number(self.value)


@dataclass
class AddNode(Expression):
    node_a: Expression
    node_b: Expression

    def __repr__(self):
        return f"({self.node_a}+{self.node_b})"

    def evaluate(self, **x_para) -> Number:
        return Number(operator.add(self.node_a.evaluate().value, self.node_b.evaluate().value))


@dataclass
class SubtractNode(Expression):
    node_a: Expression
    node_b: Expression

    def __repr__(self):
        return f"({self.node_a}-{self.node_b})"

    def evaluate(self, **x_para) -> Number:
        return Number(operator.sub(self.node_a.evaluate(**x_para).value, self.node_b.evaluate(**x_para).value))


@dataclass
class MultiplyNode(Expression):
    node_a: Expression
    node_b: Expression

    def __repr__(self):
        return f"({self.node_a}*{self.node_b})"

    def evaluate(self, **x_para) -> Number:
        return Number(operator.mul(self.node_a.evaluate(**x_para).value, self.node_b.evaluate(**x_para).value))


@dataclass
class DivideNode(Expression):
    node_a: Expression
    node_b: Expression

    def __repr__(self):
        return f"({self.node_a}/{self.node_b})"

    def evaluate(self, **x_para) -> Number:
        try:
            return Number(operator.truediv(self.node_a.evaluate(**x_para).value, self.node_b.evaluate(**x_para).value))
        except ZeroDivisionError:
            raise Exception("runtime math error (Division by zero)")


@dataclass
class PlusNode(Expression):
    node: Expression

    def __repr__(self):
        return f"(+{self.node})"

    def evaluate(self, **x_para) -> Number:
        return Number(self.node.evaluate(**x_para).value)


@dataclass
class MinusNode(Expression):
    node: Expression

    def __repr__(self):
        return f"(-{self.node})"

    def evaluate(self, **x_para) -> Number:
        return Number(operator.neg(self.node.evaluate(**x_para).value))


@dataclass()
class ExponentNode(Expression):
    node_a: Expression
    node_b: Expression

    def __repr__(self):
        return f"(power({self.node_a},{self.node_b}))"

    def evaluate(self, **x_para) -> Number:
        value_a = self.node_a.evaluate(**x_para).value
        value_b = self.node_b.evaluate(**x_para).value

        if value_a == 0 and value_b == 0:
            raise Exception("0^0 is undefined.")
        return Number(math.pow(value_a, value_b))


@dataclass()
class SquareRootNode(Expression):
    node: Expression

    def __repr__(self):
        return f"(power({self.node},0.5))"

    def evaluate(self, **x_para) -> Number:
        value = self.node.evaluate(**x_para).value
        if value < 0:
            raise_error_complex_numbers()

        return Number(math.pow(value, 0.5))


@dataclass()
class LogarithmNode(Expression):
    node: Expression
    base: Expression

    def __repr__(self):
        return f"(log_{self.base}_({self.node}))"

    def evaluate(self, **x_para) -> Number:
        value = self.node.evaluate(**x_para).value
        base = self.base.evaluate(**x_para).value
        if base <= 0:
            raise_error_complex_numbers()
        if value <= 0:
            raise_error_complex_numbers()

        return Number(math.log(value, base))


@dataclass()
class NaturalLogarithmNode(Expression):
    node: Expression

    def __repr__(self):
        return f"(ln({self.node}))"

    def evaluate(self, **x_para) -> Number:
        value = self.node.evaluate(**x_para).value
        if value <= 0:
            raise_error_complex_numbers()

        return Number(math.log(value))


@dataclass()
class CommonLogarithmNode(Expression):
    node: Expression

    def __repr__(self):
        return f"(lg({self.node}))"

    def evaluate(self, **x_para) -> Number:
        value = self.node.evaluate(**x_para).value
        if value <= 0:
            raise_error_complex_numbers()

        return Number(math.log10(value))


@dataclass()
class FactorialNode(Expression):
    node: Expression

    def __repr__(self):
        return f"(factorial({self.node}))"

    def evaluate(self, **x_para) -> Number:
        value = self.node.evaluate(**x_para).value

        special: bool = x_para["special"] if "special" in x_para else False

        if not isinstance(value, int) and not value.is_integer() and not special:
            raise Exception("runtime math error (only whole numbers)")
        if value < 0 and not special:
            raise Exception("runtime math error (no negative numbers)")

        return Number(math.gamma(value + int(not special)))
