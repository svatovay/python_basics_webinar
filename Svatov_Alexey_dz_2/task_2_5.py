list_prices = [57.8, 46.51, 97, 100.0, 21, 64.22, 11, 36.5, 17.01, 11.17, 96.4, 7.0, 13.13, 140, 51.0]
for price in list_prices:
    if isinstance(price, int):
        price = float(price)
    print(f'{(int(price))} руб {str(int(price * 100))[-2::]} коп', end=', ')

print(end='\n')
print(f' id исходого списка до сортировки по возрастанию: {id(list_prices)}')
list_prices.sort()
print(list_prices)
print(f' id исходого списка после сортировки по возрастанию: {id(list_prices)}')
list_prices_2 = sorted(list_prices, reverse=True)
print(list_prices_2)
print(f' id нового списка после создания и сортировки по убыванию: {id(list_prices_2)}')
print(f'Цены пяти самых дорогих товаров: {sorted(list_prices, reverse=True)[:5]}')
