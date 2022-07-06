import colorama
from colorama import Fore, init
init(True)
#Ejercicio 6:
#A partir de un texto:
texto = 'Phylion aprovechó la 30ª Feria Internacional de la Bicicleta de China celebrada en ' \
    'Shanghái para presentar un escaparate de las últimas tecnologías, nuevos productos y ' \
    'nuevos servicios para las bicicletas eléctricas.'
#Mostrar en pantalla la cadena completa.
print(texto)

#Encontrar y colorear todas las vocales en rojo.
#Para el desarrollo de este ejercicio recomiendo ir imprimiendo letra por letra dentro de un bucle for.
v = {'a':0,'e':0,'i':0,'o':0,'u':0}
for v in texto:
    if v.upper() == 'A' or v.upper() == 'E' or v.upper() == 'I' or v.upper() == 'O' or v.upper() == 'U':
        print(Fore.RED + v + '', end='')
    else:
        print(v + '', end = '')


