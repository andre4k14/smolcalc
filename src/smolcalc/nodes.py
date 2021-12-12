from dataclasses import dataclass


@dataclass
class number_node:
    value: float

    def __repr__(self):
        return f"{self.value}"


@dataclass
class add_node:
    node_a: object
    node_b: object

    def __repr__(self):
        return f"({self.node_a}+{self.node_b})"


@dataclass
class subtract_node:
    node_a: object
    node_b: object

    def __repr__(self):
        return f"({self.node_a}-{self.node_b})"


@dataclass
class multiply_node:
    node_a: object
    node_b: object

    def __repr__(self):
        return f"({self.node_a}*{self.node_b})"


@dataclass
class divide_node:
    node_a: object
    node_b: object

    def __repr__(self):
        return f"({self.node_a}/{self.node_b})"


@dataclass
class plus_node:
    node: object

    def __repr__(self):
        return f"(+{self.node})"


@dataclass
class minus_node:
    node: object

    def __repr__(self):
        return f"(-{self.node})"


@dataclass()
class exponent_node:
    node_a: object
    node_b: object

    def __repr__(self):
        return f"(power({self.node_a},{self.node_b}))"


@dataclass()
class square_root_node:
    node: object

    def __repr__(self):
        return f"(power({self.node},0.5))"


@dataclass()
class nlog_node:
    node: object

    def __repr__(self):
        return f"(log({self.node}))"


@dataclass()
class log_10_node:
    node: object

    def __repr__(self):
        return f"(log10({self.node}))"


@dataclass()
class factorial_node:
    node: object

    def __repr__(self):
        return f"(factorial({self.node}))"
