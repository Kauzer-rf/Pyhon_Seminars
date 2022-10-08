# 31.	Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 70 = 2*5*7 => [2, 5, 7] 
# 140 = 2*2*5*7 => [2, 2, 5, 7]
# 140|2
#  70|2
#  35|5
#   7|7
import os


def cls():
    os.system('cls'if os.name == 'nt' else 'clear')


cls()
num = int(input('Введите натуральное число n: '))

def simple_multiply(n):
   i = 2
   result_list = []
   while i * i <= n:
       while n % i == 0:
           result_list.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       result_list.append(int(n))
   return result_list

print(simple_multiply(num))