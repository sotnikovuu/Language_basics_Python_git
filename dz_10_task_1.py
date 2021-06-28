# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.

class Matrix:
    def __init__(self, incom):
        self.incom = incom

    def __str__(self):
        lines = str()
        for line in self.incom:
            lines += ' '.join(map(str, line)) + '\n'
        return lines

    def __add__(self, other):
        output = ''
        if len(self.incom) == len(other.incom):
            for line_1, line_2 in zip(self.incom, other.incom):
                if len(line_1) != len(line_2):
                    return 'Проблема с размерами матрицы'
                summed_l = []
                for x, y in zip(line_1, line_2):
                    summed_l.append(x + y)
                output += ' '.join(map(str, summed_l)) + '\n'
        else:
            return 'Проблема с размерами матрицы'
        return output


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix_2 = Matrix([[11, 7], [4, 5], [6, 7], [10, 20]])
# print(matrix_1)
print()
print(matrix_1 + matrix_2)
