#Guía 8 - Ejercicio 7.py
import random
# 1 Crear una función para las siguientes tareas.
def tratar_lista(lista):
# 2 Recibir como parámetro una lista.
# 3 Mostrar cada elemento y su posición.
    for indice, valor in enumerate(lista):
        print(indice,valor)
# 4 Encontrar el elemento menor y su posición por arriba del valor 50.
    menor1 = min(lista, key =lambda x: x > 50)
    menor2 = min([x for x in lista if x > 50])
    print('Menor elemento mayor a 50:',menor2)
    print('Menor elemento mayor a 50:',menor2)
# 5 Encontrar el elemento mayor y su posición por debajo del valor 50.
    v2 = [x for x in lista if x < 50]
    mayor = max(v2)
    print('Mayor elemento menor a 50 es: ', mayor)
# 6 Llamar a la función desde el main con dos listas diferentes de 30 y 20 valores.

v1 = random.sample(range(99),30)
tratar_lista(v1)

v2 = random.sample(range(99),20)
tratar_lista(v2)