#Generar lista:
#Generar una lista de 20 números enteros al azar de 3 dígitos.
#Mostrar los números mayores a 300 y menores a 700.
#Acumular los números del rango.
#Contar los números del rango.

cont1 = 0
acum1 = 0
lista = []
import random

for x in range (0,20):
    numero = random.randint (100,999)
    lista.append(numero)
    if numero >= 300 and numero <= 700:
        cont1 += 1
        acum1 += numero
    else:
        continue
print(lista)
print('\n')
print('Cantidad de valores contados: ', cont1)
print('Cantidad de valores acumulados: ',acum1)
