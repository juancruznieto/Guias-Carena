#Generar lista
#Generar una lista de 20 números enteros al azar de 3 dígitos.
#Mostrar toda lista.
#Marcar con * (asterisco) los divisibles por 2.
#Marcar con # (numeral) los divisibles por 3.
#Marcar con $ (peso) los divisible por 4.
#Marcar con & (per se and per sand – por sí mismo) los divisibles por 5.
import random
lista = []

for x in range (0,20):
    numero = random.randint (100,999)
    lista.append(numero)
    print, lista
for valor in lista:
    if valor % 2 == 0:
        print('*',valor)
    if valor % 3 == 0:
        print('#',valor)
    if valor % 4 ==0:
        print('$',valor)
    if valor % 5 ==0:
        print('&',valor)





