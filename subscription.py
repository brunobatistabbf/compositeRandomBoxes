from composite import Composite
from leaf import Leaf
import random

class Subscription(Composite):
    items = [
        ("Quadrinhos", 15.00),
        ("Chaveiros", 5.00),
        ("Bustos", 10.00),
        ("Adesivos", 1.00),
        ("Posters", 25.00),
        ("Camisetas", 25.00),
        ("Canetas", 3.00),
        ("Miniaturas", 20.00),
    ]

    levels = {
        "Bronze": 3,
        "Prata": 5,
        "Ouro": 7,
        "Platina": 10,
    }

    def __init__(self, level: str):
        super().__init__()
        num_items = self.levels[level]
        for i in range(num_items):
            item = random.choice(self.items)
            self.add(Leaf(item[0], item[1]))

    def __str__(self):
        return f"Caixa {self.levels}:\n" + super().__str__() + f"\nValor Total: R${self.get_price()}"