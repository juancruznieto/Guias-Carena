#Ejercicio 2:
#Generar una lista de 30 elementos enteros al azar entre 50 y 250 inclusivos
#y guardarlos en una lista v1 (random.sample).
import random, statistics
v1 = random.sample(range(50,250),30)
print('Lista v1', v1)
print()


#Hacer una copia en una segunda lista v2 con los valores del primero
#que se encuentren entre 75 y 225 (ap
# licar sintaxis por comprensión).
v2 = ([x for x in v1 if x >= 75 and x <= 225])
print('Lista v2', v2)

#Crear una función para mostrar todos los elementos de una lista cualquiera y
#su posiciónl, llamarla desde el main para mostrar v1 y v2.
def poslist(lista):
    for x, y in enumerate(lista):
        print(x,y)

print()
poslist(v1)
print()
poslist(v2)


#Crear una función para encontrar el mayor, menor y el promedio de un vector
#cualquiera, llamar desde el main para mostrar los resultados de v1 y v2.
def maxminpro(lista):
    print('El elemento menor de la lista es: ',min(lista))
    print('El elemento mayor de la lista es: ',max(lista))
    mean = statistics.mean(lista)
    print('El promedio de la lista es: ',mean)

print()
maxminpro(v1)
print()
maxminpro(v2)
