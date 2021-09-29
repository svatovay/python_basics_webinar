import time


class TrafficLight:
    __color = None

    def running(self):
        variants = ['red', 'yellow', 'green']
        for __color in variants:
            if __color == 'red':
                print(f'\033[31m{__color.upper()}\033[0m')
                time.sleep(7)
            elif __color == 'yellow':
                print(f'\033[33m{__color.upper()}\033[0m')
                time.sleep(2)
            elif __color == 'green':
                print(f'\033[32m{__color.upper()}\033[0m')
                time.sleep(7)


lightning = TrafficLight()

lightning.running()
