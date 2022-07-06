#Realice un algoritmo que:
#Genere una lista de 30 números al azar de hasta 2 dígitos.
#Mostrar los pares con un “*” asterisco delante. (nro % 2 = 0)
#Mostrar los impares con un “#” numeral delante. (else)
#Contar y acumular los pares.
#Contar y acumular los impares.
#Mostrar el resultado de la cuenta y el acumulado de cada grupo.
numero = None
cont1 = 0
cont2 = 0
acum1 = 0
acum2 = 0
import random
lista = []
for x in range (0,30):
    numero = random.randint(0,99)
    lista.append(numero)
    if numero % 2 == 0:
        print(x, '*', numero)
        cont1 += 1
        acum1 += numero
    else:
        print(x, '#', numero)
        cont2 += 1
        acum2 += numero

print('Cantidad de valores pares: ', cont1)
print('Acumulado de valores pares: ', acum1)
print('Cantidad de valores inpares: ', cont2)
print('Acumulado de valores inpares: ', acum2)