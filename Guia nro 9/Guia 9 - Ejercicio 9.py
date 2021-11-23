#Escriba un programa que permita crear una lista de palabras y que, a continuación,
# elimine los elementos repetidos (dejando únicamente el primero de los elementos
# repetidos).
texto = 'Phylion  la 30ª Feria Internacional de la Bicicleta de China celebrada en ' \
    'Shanghái para presentar un escaparate de las últimas tecnologías, nuevos productos y ' \
    'nuevos servicios para las bicicletas eléctricas.'

lista = texto.split()

lista2 = lista

for x in range(len(lista)):
    for i in range(len(lista2)):
        if x != i and lista[x] == lista2[i]:
            lista2.remove(lista2[i])
print('Lista 1',' '.join(lista))
print()
print()
