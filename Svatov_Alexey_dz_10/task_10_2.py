class Clothes:
    def __init__(self):
        self.summary_list = []

    def add_suit(self, X):
        __suit = Suit(X)
        self.summary_list.append(__suit.fabric_calculation())

    def add_coat(self, X):
        __coat = Coat(X)
        self.summary_list.append(__coat.fabric_calculation())

    @property
    def summary_calculation(self):
        summary = 0
        for el in self.summary_list:
            summary += el
        return summary


class Coat:
    def __init__(self, X):
        self.v = X

    def fabric_calculation(self):
        return self.v / 6.5 + 0.5


class Suit:
    def __init__(self, X):
        self.h = X

    def fabric_calculation(self):
        return 2 * self.h + 0.3


a = Clothes()
a.add_suit(2)
a.add_coat(50)
print(a.summary_calculation)
