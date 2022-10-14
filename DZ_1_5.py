# Реализуйте алгоритм перемешивания списка.
import random

N = int(input('write N number: '))
dict = {}
count = 1
for i in range(1, N+1):
    dict[i] = i
print(dict)
dict[i],dict[j] = dict[j], dict[i]
print(dict)
# random.shuffle(dict)
# print(dict)