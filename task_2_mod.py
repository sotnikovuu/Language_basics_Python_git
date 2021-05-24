
def sum_digits_number(number):
    sum_digits = 0
    while number != 0:
        sum_digits = sum_digits + number % 10
        number = number // 10
    return sum_digits


def rrr (my_list_f, a):
    result = 0
    i = 1
    while i < len(my_list_f):
        my_list_f[i] = my_list_f[i] ** 3
        my_list_f[i] = my_list_f[i] + a
        my_list_f[i] = sum_digits_number(my_list_f[i])
        if my_list_f[i] % 7 != 0:
            my_list_f[i] = 0
        result = result + my_list_f[i]
        i += 1
    return result
    print(result)


variable = int(input('Введите 0, 17 или любое другое значение: '))
i = 1
my_list = list(range(i, 1001, 2))
my_list_f = my_list.copy()
# my_list = my_list
result = rrr(my_list_f, variable)
# print('Список возведенный в степень: ', my_list)
print('Сумма чисел:                  ', result)
