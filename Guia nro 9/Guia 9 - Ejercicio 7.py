#Escriba un programa que permita crear dos listas de palabras y que, a continuación,
#  elimine de la primera lista los nombres de la segunda lista.

v1= []
while True:
    palabra = input('Ingrese una palabra para v1: ')
    if palabra == '':
        break
    v1.append(palabra)

print('Lista v1: ',v1)

v2= []
while True:
    palabra = input('Ingrese una palabra para v2: ')
    if palabra == '':
        break
    v2.append(palabra)

print('Lista v1: ',v2)


for x in v2:
    if x in v1:
        v1.remove(x)

print('Lista v1: ',v1)
