class NullEx(Exception):
    def __init__(self, text):
        self.text = text


num_1 = 1
num_2 = 1
try:
    if num_2 == 0:
        raise NullEx('Делитель не должен быть равен нулю!')
    div = num_1 / num_2
except (ValueError, NullEx) as err:
    print(err)
else:
    print(num_1 / num_2)
