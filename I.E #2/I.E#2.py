#Programación I
#Instancia evaluativa 2 - a
#Desarrollar el siguiente algoritmo y codificar en lenguaje Python:
#Crear un bucle while para ingresar valores enteros con valores entre -30 y 30 inclusivos, salir con valor igual a 100.
#Guardarlos en una lista1.
#Encontrar y mostrar el valor máximo, mínimo y sus posiciones.
#Calcular y mostrar el acumulado y promedio de sus valores.
#Contar cuántos valores están por encima del promedio.
cont1 = 0
cont2 = 0
acum1 = 0
lista1 = []
while True:
    valor = int(input('Ingrese un valor entre -30 y 30: '))
    if valor == 100:
        break
    if valor < -30 or valor > 30:
        print('Valor fuera de rango')
        continue
    if valor >= -30 and valor <= 30:
        cont1 += 1
        acum1 += valor
        lista1.append(valor)
if cont1 != 0:
    prom1 = acum1 / cont1
print('\n')
print('Suma de valores acumulados: ',acum1)
print('Promedio de los valores acumulados:, ',prom1)
if valor >= prom1:
    cont2 =+ 1
print('Cantidad de valores por encima del promedio: ',cont2)

minimo = min(lista1)
maximo = max(lista1)
posmin = lista1.index(minimo)
posmax = lista1.index (maximo)
print('Valor mínimo: ', minimo, 'Posición: ', posmin)
print('Valor máximo: ', maximo, 'Posición: ', posmax)


