n = input() 
suma = 0
while n != 0:
    x = n % 10
    suma = suma + x
    n = n // 10
    
print("Сумма:", int(suma))

