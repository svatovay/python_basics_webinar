class Stationery:
    title = 'Заголовок'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка ручкой: \033[1m{self.title}\033[0m')


class Pensil(Stationery):
    def draw(self):
        print(f'Отрисовка карандашом: \033[3m{self.title}\033[0m')


class Handle(Stationery):
    def draw(self):
        print(f'Отрисовка маркером: \033[4m{self.title}\033[0m')


stationery = Stationery()
stationery.draw()
pen = Pen()
pen.draw()
pensil = Pensil()
pensil.draw()
handle = Handle()
handle.draw()
