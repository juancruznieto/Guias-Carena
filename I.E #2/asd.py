cont1 = 0
cont2 = 0
acum1 = 0
lista1 = []
while True:
    num = int(input('Ingrese un valor entre -30 y 30: '))
    if num == 100:
        break
    if num < -30 or num > 30:
        print('Valor fuera de rango')
        continue
    if num >= -30 and num <= 30:
        cont1 =+ 1
        acum1 =+ num
        lista1.append(num)
if cont1 != 0:
    prom1 = acum1 / cont1
print('\n')
print('Suma de valores acumulados: ',acum1)
print('Promedio de los valores acumulados:, ',prom1)
if num >= prom1:
    cont2 =+ 1
print('Cantidad de valores por encima del promedio: ',cont2)

minimo = min(lista1)
maximo = max(lista1)
posmin = lista1.index(minimo)
posmax = lista1.index (maximo)
print('Valor mínimo: ', minimo, 'Posición: ', posmin)
print('Valor máximo: ', maximo, 'Posición: ', posmax)
