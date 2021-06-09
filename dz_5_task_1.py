# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...
#

def odd_nums(max_num):
    n = 1
    while n <= max_num:
        yield n
        n += 2


odd_to_15 = odd_nums(15)
print(odd_to_15)
print(next(odd_to_15))
print(list(odd_to_15))

