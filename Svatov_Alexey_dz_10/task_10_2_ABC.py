from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric_calculation(self):
        pass


class Coat(Clothes):
    def __init__(self, X):
        self.v = X

    @property
    def fabric_calculation(self):
        __calc = self.v / 6.5 + 0.5
        return __calc


class Suit(Clothes):
    def __init__(self, X):
        self.h = X

    @property
    def fabric_calculation(self):
        __calc = 2 * self.h + 0.3
        return __calc


a = Suit(2)
b = Suit(1.8)
c = Suit(1.6)
d = Coat(50)
e = Coat(40)
f = Coat(32)
print(a.fabric_calculation + b.fabric_calculation + c.fabric_calculation)
print(c.fabric_calculation + d.fabric_calculation + f.fabric_calculation)
