#1
#Desarrollar el siguiente algoritmo y codificar en lenguaje Python:
#Crear dos listas v1 y v2 con los valores indicados y mostrar en la consola.
#v1 [237, 576, 100, 151, 123, 808, 950, 739, 115, 817]
#v2 [216, 680, 455, 691, 219, 400, 524, 145, 788, 873]
v1 = [237, 576, 100, 151, 123, 808, 950, 739, 115, 817]
v2 = [216, 680, 455, 691, 219, 400, 524, 145, 788, 873]
print("Lista V1",v1)
print()
print("Lista V2",v2)
print()
#2
#Escribir un algoritmo para crear una tercera lista v3 con los elementos
# de posición impar de la v1 y con los elementos de la posición par de la v2
# intercalando un elemento de v1 con un elemento de v2,
#luego mostrar en consola.
#v3 [576, 216, 151, 455, 808, 219, 739, 524, 817, 788]
v3i = []
v3p = []
while True:
    for x in range(len(v1)):
        if x % 2 !=0:
            v3i.append(v1[x])
    for x in range(len(v2)):
        if x % 2 ==0:
            v3p.append(v2[x])
    break
v3= v3i + v3p
v3[::2] = v3i
v3[1::2] = v3p
print('Lista V3',v3)
print()
#3.	Escribir un algoritmo para recorrer y crear una lista v4 con los elementos de
# valor impar de v1 y v2 en el orden que van apareciendo, luego mostrar en consola.
#V4 [237, 455, 151, 691, 123, 219, 739, 145, 115, 817, 873]
v41=[]
v42=[]
while True:
    for x in v1:
        if x % 2 != 0:
            v41.append(x)
    for x in v2:
        if x % 2 != 0:
            v42.append(x)
    break
v4 = v41 + v42
v4[::2] = v41
v4[1::2] = v42
print("Lista V4",v4)
print()
#4.	Escribir un algoritmo para obtener todos los elementos con índice impar de v1 y
#todos los elementos con índice par de v2 para luego agregarlos en ese orden en v5,
# mostrar en consola.
#v5 [576, 151, 808, 739, 817, 216, 455, 219, 524, 788]
v5 =[]
while True:
    for x in range(len(v1)):
        if x % 2 !=0:
            v5.append(v1[x])
    for x in range(len(v2)):
        if x % 2 ==0:
            v5.append(v2[x])
    break
print("Lista V5",v5)
print()
#5.	Escribir el algoritmo del punto 4 con sintaxis por comprensión y con slicing para
#obtener v6 y v7, mostrar en consola.
#v6 [576, 151, 808, 739, 817, 216, 455, 219, 524, 788]
v6 =  [y for x, y in enumerate (v1) if x %2 != 0] + [y for x, y in enumerate (v2) if x %2 == 0]
print('Lista v6', v6)
print()
#v7 [576, 151, 808, 739, 817, 216, 455, 219, 524, 788]
v7 =v1[1:len(v1):2] + v2[:len(v2):2]
print('Lista v7', v7)


