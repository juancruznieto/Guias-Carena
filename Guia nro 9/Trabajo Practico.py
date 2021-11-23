print('Trabajo practico')
print()
print('Juan Cruz Nieto')
print()
'''''
Trabajo Práctico 3 - a
Desarrollar el siguiente algoritmo y codificar en lenguaje Python:
Crear una lista v1 con los valores indicados y mostrar en la consola como se muestra abajo.
v1 [67, 55, 41, 57, 34, 20, 47, 68, 48, 85, 29, 88]
'''''
v1 = [67, 55, 41, 57, 34, 20, 47, 68, 48, 85, 29, 88]
print('Lista v1: ', v1)
print()

'''
Obtener y mostrar una lista v2 (for) que comience con los elementos de posición par de v1 y finalice con los elementos de posición impar de v1.
v2 [67, 41, 34, 47, 48, 29, 55, 57, 20, 68, 85, 88]
'''
v2= []
for x in range(len(v1)):
    if x % 2 == 0:
        v2.append(v1[x])
for x in range(len(v1)):
    if x % 2 != 0:
        v2.append(v1[x])
print('Lista v2: ',v2)
print()
'''
Obtener y mostrar una lista v2 (comprensión) que comience con los elementos de posición par de v1 y finalice con los elementos de posición impar de v1.
v3 [67, 41, 34, 47, 48, 29, 55, 57, 20, 68, 85, 88]
'''
v3 = [y for x, y in enumerate (v1) if x %2 == 0] + [y for x, y in enumerate (v1) if x %2 != 0]
print('Lista v3: ', v3)
print()

'''
#Obtener y mostrar una lista v2 (slicing) que comience con los elementos de posición par de v1 y finalice con los elementos de posición impar de v1.
#v4 [67, 41, 34, 47, 48, 29, 55, 57, 20, 68, 85, 88]
'''
v4 = []
for x in range(0,len(v1),2):
    v4.append(v1[x])
for x in range(1,len(v1),2):
    v4.append(v1[x])
print('Lista v4: ',v4)
print()
'''
Obtener y mostrar una lista v5 (for) con los valores pares de v1 al comienzo y con los valores impares de v1 al finalizar.
v5 [34, 20, 68, 48, 88, 67, 55, 41, 57, 47, 85, 29]
'''
v5 = []
for x in v1:
    if x %2 == 0:
        v5.append(x)
for x in v1:
    if x %2 != 0:
        v5.append(x)
print('Lista v5: ',v5)
print()

'''
#Obtener y mostrar una lista v6 (comprensión) con los valores pares de v1 al comienzo y con los valores impares de v1 al finalizar.
#v6 [34, 20, 68, 48, 88, 67, 55, 41, 57, 47, 85, 29]
'''
v6 =  [y for x, y in enumerate(v1)if y %2 ==0] + [y for x, y in enumerate(v1)if y %2 !=0]
print('Lista v6: ',v6)