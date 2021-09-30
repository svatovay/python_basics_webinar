class Worker:
    name = None
    surname = None
    position = None
    _income = {"wage": None, "bonus": None}

    def __init__(self, n, s, p, iw, ib):
        self.name = n
        self.surname = s
        self.position = p
        self._income["wage"] = iw
        self._income["bonus"] = ib


class Position(Worker):

    def get_full_name(self):
        print(f'{self.surname} {self.name}')

    def get_total_income(self):
        print(f'Заработная плата сотрудника = {Worker._income["wage"] + Worker._income["bonus"]}')


first_worker = Position('Пётр', 'Петров', 'Начальник отдела', 60000, 20000)
print(first_worker.position)
first_worker.get_full_name()
first_worker.get_total_income()
