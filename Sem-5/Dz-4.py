# 42. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from itertools import groupby

with open('Sem5_Dz-4.txt', 'w') as f:
     f.write('AAAAAAAABBBBCCCCFF')

with open('Sem5_Dz-4.txt', 'r') as f:
    my_string = f.read()
    print(my_string)

def rle(text):
    return [(key, len(tuple(group))) for key, group in groupby(text)]
result = rle(my_string)
print(result)

with open('Sem5_Dz-4(result).txt', 'w') as f:
    f.write(str(result))
    