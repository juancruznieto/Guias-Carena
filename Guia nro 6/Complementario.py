# Complementario.py
# 8- Definir una función superposicion() que tome dos listas y devuelva True
# si tienen al menos 1 miembro en común o devuelva False de lo contrario.
# Escribir la función usando el bucle for anidado.

import random

def superposicion(l1, l2):
    for valor1 in l1:
        for valor2 in l2:
            if valor1 == valor2:
                print(valor1)
                return True
    return False

def super(l1,l2):
    result = [valor for valor in l1 if valor in l2]
    print(result)
    return result

lista1 = random.sample(range(0,49), 20)
lista2 = random.sample(range(50,99), 20)

print()
print(lista1)
print(lista2)
print()

if superposicion(lista1, lista2):
    print('Hay superposición en las listas.')
else:
    print('No hay superposición')

if super(lista1, lista2):
    print('Hay superposición en las listas.')
else:
    print('No hay superposición')