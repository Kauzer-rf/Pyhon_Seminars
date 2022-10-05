# 19.	Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

# 1. Вариант решения
# c = 10
# a = 2
# b = 3
# x = 7
# m = 100

# list = []
# for i in range(c):
#     x = (a * x + b) % m
#     list.append(x)
# print(list)

# 2. Реализация алгоритмна с привязкой ко времени.
# import time
# print(int(str(time.time())[-1]))

# 3. Способ решения через функцию

import time

def random_num(start = 0, end = 1):
    seconds = time.time()
    next = True
    while next:
        rand = end * (seconds % 1)
        if rand >= start or rand > end: next = False
    return int(rand)
print (random_num(1,100))
