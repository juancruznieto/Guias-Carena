#Generar una serie de 20 números al azar de hasta 3 dígitos.

#Importar la biblioteca random (import random).
import random
#Generar números aleatorios entre 0 y 999 (random.randint(0,999).
Numero = None
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0

for x in range(0,20):
    numero = random.randint(0,999)
    print(x,numero)
#Contar y acumular los divisibles por 2 (operador módulo %).
    if numero % 2 == 0:
        contador2 += 1
#Contar y acumular los divisibles por 3.
    if numero % 3 == 0:
        contador3 += 1
#Contar y acumular los divisibles por 4.
    if numero % 4 == 0:
        contador4 += 1
#Contar y acumular los divisibles por 5.
    if numero % 5 == 0:
        contador5 += 1
#Mostrar los resultados al finalizar el bucle.
print('\n')
print('Los numeros divisibles por 2 son: ', contador2)
print('Los numeros divisibles por 3 son: ', contador3)
print('Los numeros divisibles por 4 son: ', contador4)
print('Los numeros divisibles por 5 son: ', contador5)
print('\n')
print('Fin del programa')


