# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# *Пример:*

#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06

N = int(input('write N number: '))
dict = {}
count = 1
sum = 0
for i in range(1, N+1):
    count = (1+1/i)**i
    dict[i] = count
    sum += dict[i]
print(dict, sum)    