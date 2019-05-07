"""Провереяем производительность двух вариантов кода из задачи 3-го урока:
(В массиве случайных целых чисел поменять местами
минимальный и максимальный элементы)"""

print("Вариант замера с 1-м вариантом кода.")
import timeit
setup = '''
from random import random
N = 15
arr = [0]*N
for i in range(N):
    arr[i] = int(random()*100)
    print(arr[i],end=' ')
print()
 
# 1-й вариант кода
mn = min(arr)
mx = max(arr)
imn = arr.index(mn)
imx = arr.index(mx)
print('arr[%d]=%d arr[%d]=%d' % (imn+1, mn, imx+1, mx))
arr[imn],arr[imx] = arr[imx],arr[imn]

for i in range(15):
    print(arr[i],end=' ')
print()'''
print("Время исполнения 1-го варианта (100000 раз) = ", timeit.Timer(setup=setup).repeat(1,100000), " секунд")



print("\nВариант замера со 2-м вариантом кода.")
setup = '''
from random import random
N = 15
arr = [0]*N
for i in range(N):
    arr[i] = int(random()*100)
    print(arr[i],end=' ')
print()
 

# 2-й вариант кода
mn = 0
mx = 0
for i in range(N):
    if arr[i] < arr[mn]:
        mn = i
    elif arr[i] > arr[mx]:
        mx = i
print('arr[%d]=%d arr[%d]=%d' % (mn+1, arr[mn], mx+1, arr[mx]))
b = arr[mn]
arr[mn] = arr[mx]
arr[mx] = b
 
for i in range(15):
    print(arr[i],end=' ')
print()'''
print("Время исполнения 2-го варианта (100000 раз) = ", timeit.Timer(setup=setup).repeat(1,100000), " секунд")
