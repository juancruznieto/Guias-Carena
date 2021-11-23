#Generar lista:
#Generar una lista de 20 números enteros al azar de 3 dígitos.
#Sumar los números menores a 500.
#Contar los números menores a 500.
#Sumar los números mayores a 500.
#Contar los números mayores a 500.
cont1 = 0
acum1 = 0
cont2 = 0
acum2 = 0
lista = []
import random

for x in range (0,20):
    numero = random.randint (100,999)
    lista.append(numero)
    if numero <= 500:
        cont1 += 1
        acum1 += numero
    else:
        cont2 += 1
        acum2 += numero
print('\n')
print(lista)
print('\n')
print('Cantidad de numeros menores a 500: ',cont1)
print('Valores acumulados menores a 500: ', acum1)
print('Cantidad de numeros mayores a 500: ', cont2)
print('Valores acumulados mayores a 500: ',acum2)