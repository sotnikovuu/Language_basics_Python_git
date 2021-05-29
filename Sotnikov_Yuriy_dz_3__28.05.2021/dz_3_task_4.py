# *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки
# в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
# а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
#
# Как поступить, если потребуется сортировка по ключам?
import json


def thesaurus_adv(*name):
    dictionary = {}
    num = 0
    while num < len(name):
        name_employee = name[num]
        letter_surname = name_employee.split(' ')[1]
        letter_surname = letter_surname[0]
        letter_name = name[num][0]
        dictionary.setdefault(letter_surname, {})
        dictionary[letter_surname].setdefault(letter_name, [])
        dictionary[letter_surname][letter_name].append(name_employee)
        num += 1
    # print(dictionary)
    print(json.dumps(dictionary, ensure_ascii=False, indent=4, sort_keys=True))

thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

