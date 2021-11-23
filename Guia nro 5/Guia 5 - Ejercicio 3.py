import colorama
from colorama import init, Fore, Back
init(True)
#A partir de un texto:
texto = 'Phylion aprovechó la 30ª Feria Internacional de la Bicicleta de China celebrada en ' \
    'Shanghái para presentar un escaparate de las últimas tecnologías, nuevos productos y ' \
    'nuevos servicios para las bicicletas eléctricas.'

#mostrar en pantalla la cadena completa..
print('\n')
print(texto)
print('\n')
#Pasar el texto a un vector.
lista = texto.split()
print(lista)
print()

#Recorrer el vector.
for p in lista:
    #Determinar si el elemento o palabra es uno de artículos (el, la, los, las, un, una, unos, unas).
    #Las palabras que no son artículos de la lista mostrarlas en color blanco y a los artículos en color rojo, deben formar un párrafo.
    if p == 'el' or p == 'la' or p  == 'los' or p == 'las' or p == 'un' or p == 'una' or p == 'unos' or p == 'unas':
        print(Fore.RED + p + ' ', end='')
    else:
        print(p + ' ', end='')
