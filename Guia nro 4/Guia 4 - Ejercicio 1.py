cont1 = 0
acum1 = 0
cont2 = 0
acum2 = 0
cont3 = 0
prom1 = 0
prom2 = 0
#Realizar un algoritmo para ingresar una serie de temperaturas decimales entre -20 y 50.
while True:
    temperatura = float(input('Ingrese una temperatura entre -20 y 50: '))
#Salir con 100.
    if temperatura == 100:
        break
#Validar que los valores estén entre -20 y 50.
    if temperatura < -20 or temperatura > 50:
        print('Temperatura fuera de rango')
        continue
#Contar y sacar el promedio de los valores bajo cero.
    if temperatura < 0:
        cont1 += 1
        acum1 += temperatura
#Contar y sacar el promedio de los valores sobre cero.
    if temperatura > 0:
        cont2 += 1
        acum2 += temperatura
#Contar cuántos valores ingresados son iguales a cero.
    if temperatura == 0:
        cont3 += 1
if cont1 + cont2 +cont3 != 0:
#Mostrar resultados.
    if cont1 != 0:
        prom1 = acum1 / cont1

    if cont2 !=0:
        prom2 = acum2 / cont2

print('\n')
print('Cantidad de temperaturas menores a cero: ', cont1)
print('Cantidad de temperaturas mayores a cero: ', cont2)
print('Promedio de temperaturas menores a cero: ', prom1)
print('Promedio de temperaturas mayores a cero: ', prom2)
