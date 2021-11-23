#Guía 6 - Ejercicio 5.py

def selectionSort(aList):
    for i in range(len(aList) - 1):
        posmen = i

        for j in range(i + 1, len(aList)):
            if aList[j] < aList[posmen]:
                posmen = j

        aList[i], aList[posmen] = aList[posmen], aList[i]

#Realizar una estructura de control para permitir el ingreso de nombres.
nombres = []
while True:
    nombre = input('Ingrese un nombre: ')
    #Salir con enter.
    if nombre == '':
        break

    nombres.append(nombre)

print(nombres)

#Ordenarlos alfabéticamente sin utilizar el método sort, programar algún
# algoritmo de ordenamiento como burbujas, quick sort, etc.
selectionSort(nombres)

#Al salir del bucle de carga mostrar todos los elementos.
print(nombres)
