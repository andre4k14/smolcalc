from dataclasses import dataclass

@dataclass
class Number:
    value: float

    def __repr__(self):
        return f"{self.value}"

    def __str__(self):
        if self.value.is_integer():
            return f"{int(self.value)}"
        return f"{self.value}"
