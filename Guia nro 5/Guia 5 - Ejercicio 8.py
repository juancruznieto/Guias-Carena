from colorama import Fore, init

init(True)
#Ejercicio 8:
#A partir de un texto:
texto = 'Phylion aprovechó la 30ª Feria Internacional de la Bicicleta de China celebrada en ' \
    'Shanghái para presentar un escaparate de las últimas tecnologías, nuevos productos y ' \
    'nuevos servicios para las bicicletas eléctricas.'
#Mostrar en pantalla la cadena completa.
print(texto)
print()
lista = texto.split()
#Imprimir el texto y remarcar los artículos (el, la, los, las, un, una, unos, unas)
# en otro color.
for p in lista:
    if p == 'el' or p == 'la' or p  == 'los' or p == 'las' or p == 'un' or p == 'una' or p == 'unos' or p == 'unas':
        print(Fore.BLUE + p + ' ', end='')
    else:
        print(p + ' ', end='')
