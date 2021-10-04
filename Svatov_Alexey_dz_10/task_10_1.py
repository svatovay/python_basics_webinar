class Matrix:
    def __init__(self, il):
        self.input_list = il

    def __str__(self):
        __str = ''
        for el in self.input_list:
            for value in el:
                __str += f'{str(value).center(3)}   '
            __str += f'\n'
        return __str

    def __add__(self, other):
        __summary = []
        if len(self.input_list) >= len(other.input_list):
            for i in range(len(self.input_list)):
                __summary.append([])
                if len(self.input_list[0]) >= len(other.input_list[0]):
                    for j in range(len(self.input_list[0])):
                        try:
                            __summary[i].append(self.input_list[i][j] + other.input_list[i][j])
                        except IndexError:
                            try:
                                __summary[i].append(other.input_list[i][j])
                            except IndexError:
                                try:
                                    __summary[i].append(self.input_list[i][j])
                                except IndexError:
                                    __summary[i].append(0)
                else:
                    for j in range(len(other.input_list[0])):
                        try:
                            __summary[i].append(self.input_list[i][j] + other.input_list[i][j])
                        except IndexError:
                            try:
                                __summary[i].append(other.input_list[i][j])
                            except IndexError:
                                try:
                                    __summary[i].append(self.input_list[i][j])
                                except IndexError:
                                    __summary[i].append(0)
        else:
            for i in range(len(other.input_list)):
                __summary.append([])
                if len(self.input_list[0]) >= len(other.input_list[0]):
                    for j in range(len(self.input_list[0])):
                        try:
                            __summary[i].append(self.input_list[i][j] + other.input_list[i][j])
                        except IndexError:
                            try:
                                __summary[i].append(other.input_list[i][j])
                            except IndexError:
                                try:
                                    __summary[i].append(self.input_list[i][j])
                                except IndexError:
                                    __summary[i].append(0)
                else:
                    for j in range(len(other.input_list[0])):
                        try:
                            __summary[i].append(self.input_list[i][j] + other.input_list[i][j])
                        except IndexError:
                            try:
                                __summary[i].append(other.input_list[i][j])
                            except IndexError:
                                try:
                                    __summary[i].append(self.input_list[i][j])
                                except IndexError:
                                    __summary[i].append(0)
        return Matrix(__summary)


m_1 = Matrix([[31, 22], [37, 43], [51, 86]])
print(m_1)

m_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(m_2)

m_3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
print(m_3)

print(m_3 + m_2)
