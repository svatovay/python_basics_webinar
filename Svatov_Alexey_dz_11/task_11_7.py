class ComplexNumber:
    def __init__(self, txt):
        self.txt = txt

        if self.txt.rfind('+') != -1:
            self.second_ar_op = '+'
            self.first_num = int(self.txt[:self.txt.rfind('+')])
            self.second_num = int(self.txt[self.txt.rfind('+'):-1])

        else:
            self.second_ar_op = '-'
            self.first_num = int(self.txt[:self.txt.rfind('-')])
            self.second_num = int(self.txt[self.txt.rfind('-'):-1])

    def __add__(self, other):
        if self.second_num + other.second_num >= 0:
            result = f'{self.first_num + other.first_num}+{self.second_num + other.second_num}i'
        else:
            result = f'{self.first_num + other.first_num}{self.second_num + other.second_num}i'
        return result

    def __mul__(self, other):
        if (self.second_num * other.first_num + self.first_num * other.second_num) >= 0:
            result = f'{self.first_num * other.first_num - self.second_num * other.second_num}+{self.second_num * other.first_num + self.first_num * other.second_num}i'
        else:
            result = f'{self.first_num * other.first_num - self.second_num * other.second_num}{self.second_num * other.first_num + self.first_num * other.second_num}i'
        return result


a = ComplexNumber('2+3i')
b = ComplexNumber('5-7i')
print(a + b)
print(a * b)
