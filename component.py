from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def get_price(self) -> float:
        pass

    def add(self, product: 'Component'):
        pass

    def remove(self, product: 'Component'):
        pass

    def __str__(self):
        pass
