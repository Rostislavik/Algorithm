# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9."

a = [0]*8
for i in range(2,100):
    for j in range(2,10):
        if i%j == 0:
            a[j-2] += 1
i = 0
while i < len(a):
    print(i+2, ' - ', a[i])
    i += 1


# 4. Определить, какое число в массиве встречается чаще всего.

from random import random
N = 20
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 30)
print(arr)
num = arr[0]
max_frq = 1
for i in range(N-1):
    frq = 1
    for k in range(i+1,N):
        if arr[i] == arr[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = arr[i]
if max_frq > 1:
   print(max_frq, 'раз(а) встречается', num)
else:
   print('Повторений нет')


# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import random
N = 20
arr = []
for i in range(N):
        arr.append(int(random() * 100) - 50)
print(arr)
i = 0
index = -1
while i < N:
        if arr[i] < 0 and index == -1:
                index = i
        elif arr[i] < 0 and arr[i] > arr[index]:
                index = i
        i += 1
print(index+1,':', arr[index+1])


# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import random
M = 10
N = 5
a = []
for i in range(N):
    b = []
    for j in range(M):
        n = int(random()*200)
        b.append(n)
        print('%4d' % n,end='')
    a.append(b)
    print()
 
max = -1
for j in range(M):
    min = 200
    for i in range(N):
        if a[i][j] < min:
            min = a[i][j]
    if min > max:
        max = min
print("Максимум из минимума: ", max)


# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

from random import random
N = 15
a = [0]*N
for i in range(N):
    a[i] = int(random()*100)
    print('%3d' % a[i], end='')
print()
min_id = 0
max_id = 0
for i in range(1,N):
    if a[i] < a[min_id]:
        min_id = i 
    elif a[i] > a[max_id]:
        max_id = i
print(a[min_id], a[max_id])

if min_id > max_id:
    min_id, max_id = max_id, min_id
summa = 0
for i in range(min_id+1, max_id):
    summa += a[i]
print('Сумма элементов между max и min массива =',summa)


# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить
# значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

from random import random
N = 15
arr = [0]*N
even = []
for i in range(N):
    arr[i] = int(random() * 15) + 15
    if arr[i] % 2 == 0:
        even.append(i)
print(arr)
print('Индексы четных чисел: ', even)





