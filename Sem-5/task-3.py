# 35. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найдите это число.

with open('Sem5_task3.txt', 'w') as f:
    f.write('1 2 3 \n4 5 6 8 \n9 10 \n')
    f.write('77 78 \n79 80 81 \n')
num_row = []

path = 'Sem5_task3.txt'
data = open (path, 'r')
for line in data:
    print(line)
    num_row += list(map(int, line.split()))
data.close()

print(num_row)

for i, elem in enumerate(num_row[:-1]):
    if elem +1 != num_row[i+1]:
        print(elem + 1)
