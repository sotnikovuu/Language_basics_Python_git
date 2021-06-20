# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
# #
# @type_logger
# def calc_cube(x):
#    return x ** 3
# #
# >>> a = calc_cube(5)
# 5: <class 'int'>
# #
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)
#

from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(args):
        print(f'{func.__name__} ({args}: {type(args)})')
        return func(args)
    return wrapper

@type_logger
def calc_cube(arg):
    """Калькулятор Куба"""
    print(arg**3)

calc_cube(4)