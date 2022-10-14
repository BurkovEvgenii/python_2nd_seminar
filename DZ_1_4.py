# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции вводятся с клавиатуры .

from re import X


N = int(input('write N number: '))
dict = {}
for i in range(-N , N+1):
    dict[i] = i
print(dict)
X = int(input('write X position: '))
Y = int(input('write Y position: '))
mult = 0
if X >= -N and Y <= N+1:
    mult = dict[X] * dict[Y]
    print(mult)