#Realice un algoritmo que:
#Permite ingresar una serie de números enteros entre 1 y 1000.
#Salir con cero (0).
#Validar que no se ingresen valores fuera del rango y mostrar un mensaje “Valor fuera de rango”.
#Contar y acumular los menores o igual a 500.
#Contar y acumular los valores mayores a 500.
#Mostrar los resultados.

contador1 = 0
contador2 = 0
acumulador1 = 0
acumulador2 = 0

while True:
    valor = int(input('Ingrese un valor entero: '))
    if valor == 0:
        break
    if valor < 1 or valor > 1000:
        print('Valor fuera de rango')
        continue
    if valor <= 500:
        contador1 = contador1 + 1
        acumulador1 = acumulador1 + valor
    else:
        contador2 = contador2 + 1
        acumulador2 = acumulador2 + valor
print('Cantidad de valores menor o igual a 500: ', contador1)
print('Valores acumulados menor o igual a 500: ', acumulador1)
print('Cantidad de valores mayor a 500: ', contador2)
print('Valores acumulados mayor a 500: ', acumulador2)

