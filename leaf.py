from component import Component


class Leaf(Component):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price

    def __str__(self):
        return f"{self.name}: R$ {self.price}"
