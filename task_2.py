print('Задание 2a')


def sum_digits_number(number):
    sum_digits = 0
    while number != 0:
        sum_digits = sum_digits + number % 10
        number = number // 10
    return sum_digits


def rrr(my_list_f, a):
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


i = 1
my_list = list(range(i, 1001, 2))
my_list_f = my_list.copy()
print('Список из нечетных чисел:     ', my_list)
result = rrr(my_list_f, 0)
# print('Список возведенный в степень: ', my_list)
print('Сумма чисел кратных 7:        ', my_list)
print('Сумма чисел:                  ', result)


print('Задание 2b')
print('Список из нечетных чисел:     ', my_list)
i = 1
result = rrr(my_list, 17)
print('Сумма чисел кратных 7:        ', my_list)
print('Сумма чисел:                  ', result)