#A partir de un texto, crear una lista1 con las palabras
#Mostrar lista1

#Crear una lista3 al revez con las palabras de lista1, no usar reverse, usar slicing
#mostrar lista3

#Variables:
texto = 'Phylion aprovechó la 30ª Feria Internacional de la Bicicleta de China celebrada en ' \
    'Shanghái para presentar un escaparate de las últimas tecnologías, nuevos productos y ' \
    'nuevos servicios para las bicicletas eléctricas.'

lista1=texto.split()
print(lista1)
#Desarrollar un algoritmo para crear una lista2 al reves con las palabras de lista1( no usar reversed, usar for in range)
#Mostrar lista2
lista2 = []
for i in range(len(lista1)-1,-1,-1):
    lista2.append(lista1[i])
print()
print(lista2)
#Crear una lista3 al revez con las palabras de lista1, no usar reverse, usar slicing
#mostrar lista3
lista3 = lista1 [::-1]
print()
print(lista3)