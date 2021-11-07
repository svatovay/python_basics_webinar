class Road:
    _length = None
    _weight = None

    def __init__(self, l, w):
        self._length = l
        self._weight = w

    def calculation(self):
        m = self._length * self._weight * 0.025 * 5
        print(f'Масса асфальта, необходимого для покрытия всей дороги = {int(m)} т.')


little_road = Road(20, 5000)
little_road.calculation()
