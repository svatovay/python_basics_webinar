my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_str = ''
for value in my_list:
    if value.isdigit():
        value = '"' + value.zfill(2) + '"'
    else:
        for element in value:
            if element.isdigit():
                value = '"' + value[0] + element.zfill(2) + '"'
    my_str += value
    my_str += ' '
print(my_str)
