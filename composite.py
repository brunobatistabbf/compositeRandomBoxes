from  component import  Component

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, product: 'Component'):
        self.children.append(product)

    def remove(self, product: 'Component'):
        self.children.remove(product)

    def get_price(self) -> float:
        return sum(child.get_price() for child in self.children)

    def __str__(self):
        return '\n'.join(str(child) for child in self.children)