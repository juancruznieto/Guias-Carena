#Genera una serie de 30 números al azar de hasta 3 dígitos.
#Importar la biblioteca random (import random).
import random
numero = None
contador1 = 0
contador2 = 0
contador3 = 0
acum1 = 0
acum2 = 0
acum3 = 0
#Generar números aleatorios entre 0 y 999 (random.randint(0,999).
for x in range(0,30):
    numero = random.randint(0,999)
    print(x,numero)
#Contar y acumular los valores entre 0 y 300 inclusivos.
    if numero < 301:
        contador1 += 1
        acum1 += numero
    if 301 < numero < 601:
            contador2 += 1
            acum2 += numero
    if 601 < numero < 1000:
            contador3 += 1
            acum3 += numero
print('\n')
print('Cantidad de numeros entre 0 y 300: ', contador1)
print('Cantidad acumulada de valores entre 0 y 300 es: ',acum1)
print('Cantidad de numeros entre 301 y 601: ', contador2)
print('Cantidad acumulada de valores entre 301 y 600 es: ',acum2)
print('Cantidad de numeros entre 601 y 1000:', contador3)
print('Cantidad acumulada de valores entre 601 y 1000 es: ', acum3)
print('\n')
print('Fin del programa')


#Contar y acumular los valores entre 301 y 600 inclusivos.
#Contar y acumular los valores entre 601 y 1000 inclusivos.
#Mostrar los resultados.
