for percent in range(1, 101):
    if (1 < percent % 10 < 5) and (percent < 5 or percent > 20):
        print(f'{percent} процента')
    elif (percent % 10 == 1) and (percent < 5 or percent > 20):
        print(f'{percent} процент')
    else:
        print(f'{percent} процентов')
