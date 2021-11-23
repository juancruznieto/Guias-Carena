#Realizar un algoritmo que:
#Permite ingresar una serie de números enteros entre 100 y 500 inclusivos.
#Acumular los valores.
#Contar los valores.
#Sacar el promedio de los valores.
#Salir con -1.

cont1 = 0
acum1 = 0
prom1 = 0

while True:
    numero = int(input('Ingrese un numero entre 100 y 500: '))
    if numero == -1:
        break
    if numero < 100 or numero > 500:
        print('Valor fuera de rango')
        continue
    if numero >= 100 and numero <= 500:
        cont1 += 1
        acum1 += numero
prom1 = acum1/cont1
print('\n')
print('Cantidad de numeros ingresados: ', cont1)
print('Cantidad de valores acumulados: ', acum1)
print('Promedio de los valores ingresados: ',prom1)


