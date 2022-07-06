from os import system
system('cls')

numero = 0
vector = ()

while numero != -1:
    numero = int(input('ingrese un valor enteroo entre 0 y 99: '))
    vector.append(numero)

    if numero == -1:
        break

    if numero < 0 or numero > 99:
        print('El valor ingresado esta fuera de rango')
        continue

    vector.append(numero)
print(vector)