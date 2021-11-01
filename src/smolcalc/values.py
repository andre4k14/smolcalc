from dataclasses import dataclass


@dataclass
class Number:
    value: float

    def __repr__(self):
        return f"{self.value}"

    def __str__(self):
        if not isinstance(self.value, int) and self.value.is_integer() and str(self.value).find("e") == -1:
            return f"{int(self.value)}"
        return f"{self.value}"

@dataclass
class Factorial:
    value: int

    def __repr__(self):
        return f"{self.value}"

    def __str__(self):
        return f"{self.value}"
