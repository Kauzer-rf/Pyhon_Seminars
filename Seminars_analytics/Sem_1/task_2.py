# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# numbers = []
# for i in range(5):
#     numbers.append(int(input(f'Enter number: ')))
# print(numbers)
# print(max(numbers))

num1 = 1
num2 = 44
num3 = 3
num4 = 18
num5 = 152

array = [num1, num2, num3, num4, num5]
max_num = array[0]
for i in array:
    if max_num < i:
        max_num = i
print(array)
print(f'Максималное число = {max_num}')

# my_max = 0
# for _ in range(5):
#     num = int(input('Введите число: '))
#     if my_max < num:
#         my_max = num

# print(my_max)

# range(5) -> range(start=0, stop=5, step=1):
# range(1,5) -> range(start=1, stop=5, step=1)
# range(1,9,2) -> range(start=1, stop=9, step=2)
# range(9,1,-1) -> range(start=9, stop=1, step=-1)
