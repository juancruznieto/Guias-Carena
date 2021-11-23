#Guía 6 - Ejercicio 1.1.py
import random

#1 Generar un lista V1 de 20 elementos enteros de hasta 2 dígitos.
V1 = random.sample(range(0,99),20)
print('Lista V1', V1)

V2 = []
V3 = []
for valor in V1:
    if valor % 2 == 0:
        #2 Obtener un lista V2 a partir del lista V1 con los elementos divisibles por 2.
        V2.append(valor)
    else:
        #3 Obtener un lista V3 a partir del lista V1 con los elementos no divisibles por 2.
        V3.append(valor)

#4 Calcular el mayor, menor elemento y sus posiciones del lista V2.
print('Lista V2', V2)
minimo = min(V2)
maximo = max(V2)
posmin = V2.index(minimo)
posmax = V2.index(maximo)

print('El elemento menor de V2 es:',minimo)
print('La posición del elemento menor de V2 es:',posmin)
print('El elemento mayor de V2 es:',maximo)
print('La posición del elemento mayor de V2 es:',posmax)

#5 Calcular el mayor, menor elemento y sus posiciones del lista V3.
print('Lista V3', V3)
minimo = min(V3)
maximo = max(V3)
posmin = V3.index(minimo)
posmax = V3.index(maximo)

print('El elemento menor de V3 es:',minimo)
print('La posición del elemento menor de V3 es:',posmin)
print('El elemento mayor de V3 es:',maximo)
print('La posición del elemento mayor de V3 es:',posmax)

#6 Mostrar los resultados