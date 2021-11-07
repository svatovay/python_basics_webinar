duration = int(input('Введите время в секундах: '))
days = duration // (60 ** 2) // 24
hours = (duration - days * 24 * (60 ** 2)) // (60 ** 2)
minutes = (duration - (days * 24 + hours) * (60 ** 2)) // 60
seconds = duration % 60
print(f'{days} дн {hours} час {minutes} мин {seconds} сек')
