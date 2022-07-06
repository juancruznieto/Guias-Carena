#Ejercicio 2:
import random
def minmax(lista):
    minimo = min(lista)
    maximo = max(lista)
    posmin = lista.index(minimo)
    posmax = lista.index(maximo)
    print('El elemento menor es:',minimo)
    print('La posición del menor elemento es:',posmin)
    print('El elemento mayor es:',maximo)
    print('La posición del mayor elemento es es:',posmax)
    print()
#Generar un vector de 20 elementos enteros al azar de hasta dos dígitos.
lista1 = random.sample(range(0,99), 20)
print('lista1', lista1)
print()
#Calcular el menor, mayor elemento y sus posiciones de los primeros 10.
lista2 = lista1[0:10]
print('Lista 2', lista2)
minmax(lista2)
#Calcular el mayor, menor elemento y sus posiciones de los segundos 10.
lista3 = lista1[10:20]
print('Lista 3', lista3)
minmax(lista3)
#Mostrar resultados.
