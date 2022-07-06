#Escriba un programa que permita crear dos listas de palabras y que,
# a continuación, escriba las siguientes listas (en las que no debe haber repeticiones):
v1= []
v2= []
while True:
    p =input('Ingrese una palabra para lista 1: ')
    if p == '':
        break
    else: v1.append(p)
    continue

while True:
    i = input('Ingrese una palabra para lista 2: ')
    if i == '':
        break
    elif i == p:
        print('Palabra repetida')
    else: v2.append(i)
    continue

#Lista de palabras que aparecen en las dos listas.
#Lista de palabras que aparecen en la primera lista, pero no en la segunda.
#Lista de palabras que aparecen en la segunda lista, pero no en la primera.
#Lista de palabras que aparecen en ambas listas.
#Nota: Para evitar las repeticiones, el programa deberá empezar eliminando los elementos repetidos en cada lista.