import random
#Inicializar 2 matrices v1 y v2 de 5 x 5 con valores enteros de hasta 2 dígitos.
v1 = []
v2 = []
for x in range(5):
    fila = []
    for i in range (5):
        nro = random.randint(0,99)
        fila.append(nro)
    v1.append(fila)
print(v1)
print()
for x in range(5):
    fila = []
    for i in range (5):
        nro = random.randint(0,99)
        fila.append(nro)
    v2.append(fila)
print(v2)
print()
#Cargar las listas con números al azar con dos for anidados para filas y columnas.
#Mostrar por separado cada lista con dos for, usar print(‘{:>2}’.format(v1[f][c])).
print('Matriz v1')
for f in range(5):
    for c in range(5):
        print('{:>2}'.format(v1[f][c]),  end=' ')
    print()
print()
print('Matriz v2')
for f in range(5):
    for c in range(5):
        print('{:>2}'.format(v2[f][c]),  end=' ')
    print()
