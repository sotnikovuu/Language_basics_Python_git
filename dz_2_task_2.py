# Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до
# двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была',
# '"', '+05', '"', 'градусов']
#
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
#
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к
# его реализации позже. Главное: дополнить числа до двух разрядов нулём!

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(my_list)
print(id(my_list))
len_my_list = len(my_list)
list_number = 0
while list_number < len(my_list):
    if my_list[list_number].isdigit() == True:
        format_value = f'{float(my_list[list_number]):02.0f}'
        my_list.insert(0, '"')
        my_list.insert(0, format_value)
        my_list.insert(0, '"')
        list_number += 4
    elif my_list[list_number][1:].isdigit() == True:
        format_value = my_list[list_number][:1] + f'{float(my_list[list_number][1:]):02.0f}'
        my_list.insert(0, '"')
        my_list.insert(0, format_value)
        my_list.insert(0, '"')
        list_number += 4
    else:
        my_list.insert(0, my_list[list_number])
        list_number += 2

counter = 0
while counter < len_my_list:
    del my_list[-(len_my_list - counter)]
    counter += 1

my_list.reverse()

print(my_list)
print(id(my_list))

print(' '.join(my_list))


