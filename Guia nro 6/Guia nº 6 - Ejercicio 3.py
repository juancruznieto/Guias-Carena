#Ejercicio 3:
#Realizar un algoritmo para ingresar una serie de temperaturas decimales entre -20 y 50.
#Salir con 100.
#Validar que los valores están entre -20 y 50.
#Contar y sacar el promedio de los valores bajo cero.
#Contar y sacar el promedio de los valores sobre cero.
#Contar cuántos valores ingresados son iguales a cero.
#Mostrar resultados.
cont1 = 0
acum1 = 0
cont2 = 0
acum2 = 0
cont3 = 0


while True:
    temp = int(input('Ingrese temperatura: '))
    if temp == 100:
        break
    elif temp <= -20 or temp > 50:
        print('Temperatura fuera de rango')
    elif temp > -20 or temp < 0:
        cont1 += 1
        acum1 + temp
    elif temp > 0 or temp <= 50:
        cont2 += 1
        acum2 + temp
    elif temp == 0:
        cont3 += 1

if cont1 != 0:
    prom1 = acum1 / cont1

if cont2 != 0:
    prom2 = acum2 / cont2

print('Promedio de valores bajo cero: ', prom1)
print('Promedio de valores sobre cero: ',prom2)
print('Cantidad de valores iguales a cero: ',cont3)

