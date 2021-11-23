#Ejercicio 9:
#A partir de un texto:
#Mostrar en pantalla la cadena completa.
#Imprimir el texto con las vocales coloreadas según la siguiente tabla:
# a á A Á Blue
# e é E É Cyan
# i í I Í Green
# o ó O Ó Magenta
# u ú U Ú Red
from colorama import Fore, init

init(True)

texto = 'Phylion aprovechó la 30ª Feria Internacional de la Bicicleta de China celebrada en ' \
    'Shanghái para presentar un escaparate de las últimas tecnologías, nuevos productos y ' \
    'nuevos servicios para las bicicletas eléctricas.'
print(texto)
print()
for p in texto:
    if p.upper() == 'A' or p.upper() == 'Á':
        print(Fore.BLUE + p, end= '')
    elif p.upper() == 'E' or p.upper() == 'É':
        print(Fore.CYAN + p, end= '')
    elif p.upper() == 'I' or p.upper() == 'Ì':
        print(Fore.GREEN + p, end= '')
    elif p.upper() == 'O' or p.upper() == 'Ó':
        print(Fore.MAGENTA + p, end= '')
    elif p.upper() == 'U' or p.upper() == 'Ú':
        print(Fore.RED + p, end= '')
    else:
        print(p,end= '')

