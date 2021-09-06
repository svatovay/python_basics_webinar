def num_translate(input_num):
    num_dict = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    output_num = num_dict[input_num]
    return output_num


print(num_translate(input('Введите числительное от 0 до 10, включительно, на английском языке: ')))
