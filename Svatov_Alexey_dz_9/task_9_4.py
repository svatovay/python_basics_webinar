class Car:
    speed = None
    color = None
    name = None
    is_police = False

    def go(self):
        print(f'{self.name} поехал(а) со скоростью {self.speed} км/ч')

    def stop(self):
        print(f'{self.name} остановилась(ся)')

    def turn(self, direction=None):
        if direction:
            print(f'{self.name} повернул(а) {direction}')
        else:
            print(f'{self.name} едет прямо')

    def show_speed(self):
        print(f'Текущая скорость автомобиля = {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            print(f'Текущая скорость автомобиля = {self.speed}')
        else:
            print(f'Превышение скорости на {self.speed - 60} км/ч!!! Текущая скорость автомобиля = {self.speed}')


class SportCar(Car):
    def show_speed(self):
        print(f'Я еду уже в три раза быстрее = {self.speed * 3} км/ч')


class WorkCar(Car):
    def show_speed(self):
        if self.speed <= 40:
            print(f'Текущая скорость автомобиля = {self.speed}')
        else:
            print(f'Превышение скорости на {self.speed - 40} км/ч!!! Текущая скорость автомобиля = {self.speed}')


class PoliceCar(Car):
    def __init__(self, ip):
        Car.is_police = ip

    def show_speed(self):
        if self.is_police:
            print(f'Ограничения не действуют!')


first_car = TownCar()
first_car.speed = 100
first_car.name = 'Subaru'
first_car.color = 'Black'
first_car.go()
first_car.turn()
first_car.show_speed()
first_car.stop()
print('-' * 100)
second_car = SportCar()
second_car.speed = 100
second_car.name = 'Bugatti'
second_car.color = 'Blue'
second_car.go()
second_car.turn()
second_car.show_speed()
second_car.stop()
print('-' * 100)
third_car = WorkCar()
third_car.speed = 50
third_car.name = 'Lada'
third_car.color = 'Red'
third_car.go()
third_car.turn('направо')
third_car.show_speed()
third_car.stop()
print('-' * 100)
fourth_car = PoliceCar(True)
fourth_car.speed = 200
fourth_car.name = 'Ford'
fourth_car.color = 'White'
fourth_car.go()
fourth_car.turn('налево')
fourth_car.show_speed()
fourth_car.stop()
