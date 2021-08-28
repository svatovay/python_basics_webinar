duration = int(input('Введите время в секундах: '))
if not duration // 60:
    print(f'{duration} сек')
else:
    seconds = duration % 60
    minutes = duration // 60
    if not minutes // 60:
        print(f'{minutes} мин {seconds} сек')
    else:
        hours = minutes // 60
        minutes = (duration - hours * 60 * 60) // 60
        if not hours // 24:
            print(f'{hours} час {minutes} мин {seconds} сек')
        else:
            days = hours // 24
            hours = ((duration - days*24*60*60) // 60) // 60
            print(f'{days} дн {hours} час {minutes} мин {seconds} сек')
