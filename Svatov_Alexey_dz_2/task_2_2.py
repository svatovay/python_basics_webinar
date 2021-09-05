my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_str = ''
for value in my_list:
    if value.isdigit():
        value = '"' + value.zfill(2) + '"'
    elif value[1::].isdigit():
        value = '"' + value[0] + value[1::].zfill(2) + '"'
    my_str += value
    my_str += ' '
print(my_str)