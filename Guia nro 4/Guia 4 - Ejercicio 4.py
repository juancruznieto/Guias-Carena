#Generar lista:
#Generar una lista de 20 números enteros al azar de 3 dígitos.
#Encontrar el mayor entre los menores a 500.
#Encontrar el menor entre los menores a 500.
#Encontrar el menor entre los mmayores a 500.
#Encontrar el mayor entre los mayores a 500.

import random
menor1 = menor2 = 1000
mayor1 = mayor2 = 0

lista = []
for x in range (20):
    nro = random.randint(100,999)
    lista.append(nro)
    if nro < 500:
        if nro < menor1:
            menor1 = nro
        if nro > mayor1:
            mayor1 = nro
    else:
        if nro < menor2:
            menor2 = nro
        if nro > mayor2:
            mayor2 = nro

lista.sort()
print(lista, '\n')

print('El mayor entre los menores a 500 es: ', menor1)
print('El menor entre los menores a 500 es: ',mayor1)
print('El mayor entre los mayores a 500 es: ',menor2)
print('El menor entre los mayores a 500 es: ',mayor2)