class NumberEx(Exception):
    def __init__(self, text):
        self.text = text


init = True
numbers_list = []
while init:
    try:
        x = input('Введите число: ')
        if x.isalpha() and x != 'stop':
            raise NumberEx('Вы ввели строку! Будьте Внимательнее!')
    except (ValueError, NumberEx) as err:
        print(err)
    else:
        if x == 'stop':
            break
        else:
            numbers_list.append(x)

print(numbers_list)
