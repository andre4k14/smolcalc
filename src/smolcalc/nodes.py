from dataclasses import dataclass


@dataclass
class NumberNode:
    value: float

    def __repr__(self):
        return f"{self.value}"


@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}+{self.node_b})"


@dataclass
class SubtractNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}-{self.node_b})"


@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}*{self.node_b})"


@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}/{self.node_b})"


@dataclass
class PlusNode:
    node: any

    def __repr__(self):
        return f"(+{self.node})"


@dataclass
class MinusNode:
    node: any

    def __repr__(self):
        return f"(-{self.node})"


@dataclass()
class ExponentNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"(power({self.node_a},{self.node_b}))"


@dataclass()
class SquarerootNode:
    node: any

    def __repr__(self):
        return f"(power({self.node},0,5))"


@dataclass()
class NLOG_Node:
    node: any

    def __repr__(self):
        return f"(log({self.node}))"


@dataclass()
class LOG_10_Node:
    node: any

    def __repr__(self):
        return f"(log10({self.node}))"


@dataclass()
class FactorialNode:
    node: any

    def __repr__(self):
        return f"(factorial({self.node}))"
