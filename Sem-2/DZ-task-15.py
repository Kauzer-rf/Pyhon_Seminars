# 15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def multiplication(num):
    result = [1]
    for i in range(1, num):
        result.append((i+1)*result[i - 1])
    return result


N = int(input('Введите целое положительное число: '))
multipli = multiplication(N)
print(f'Результат перемножения: {multipli}')