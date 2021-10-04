class Cell:
    def __init__(self, X):
        self.cell = '*'
        self.num = X

    def __str__(self):
        return self.cell * self.num

    def __add__(self, other):
        result = self.num + other.num
        return Cell(result)

    def __sub__(self, other):
        if self.num > other.num:
            result = self.num - other.num
            return Cell(result)
        else:
            return f'Клетки кончились!'

    def __mul__(self, other):
        result = self.num * other.num
        return Cell(result)

    def __floordiv__(self, other):
        result = self.num // other.num
        return Cell(result)

    def make_order(self, Y):
        self.order = Y
        self.cells = ''
        for i in range(1, self.num + 1):
            self.cells += '*'
            if not i % self.order:
                self.cells += f'\n'
        return self.cells


cell_1 = Cell(20)
cell_2 = Cell(5)
cell_3 = Cell(3)
print(cell_1 + cell_2 + cell_3)
print('-' * 150)
print(cell_1 - cell_2)
print('-' * 150)
print(cell_2 - cell_1)
print('-' * 150)
print((cell_2 * cell_3).make_order(5))
print('-' * 150)
print((cell_1 // cell_2).make_order(5))
print('-' * 150)
