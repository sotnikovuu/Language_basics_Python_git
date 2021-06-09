# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя ключевое слово yield.

max_num = 15
nums_gen = (num for num in range(1, max_num + 1, 2))

print(nums_gen)
print(next(nums_gen))
print(next(nums_gen))
print(list(nums_gen))