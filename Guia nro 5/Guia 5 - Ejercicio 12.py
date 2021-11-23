#Ejercicio 12:
from colorama import Fore, init
init(True)
#A partir de un texto:
texto = 'Phylion aprovechó la 30ª Feria Internacional de la Bicicleta de China celebrada en ' \
    'Shanghái para presentar un escaparate de las últimas tecnologías, nuevos productos y ' \
    'nuevos servicios para las bicicletas eléctricas.'
#Mostrar en pantalla la cadena completa.
print(texto)
print()
#Pasar el texto a un vector v.
v = texto.split()
#Contar e Imprimir nuevamente el texto coloreando las palabras con acento ortográfico.
#Mostrar el resultado del contador.
contar = 0

for palabra in v:
    flag = False

    for letra in palabra:
        #if (letra >= 'Á' and letra <= 'Ú) or (letra >= 'a' and letra <= 'u'):
        if letra.upper() >= 'Á' and letra.upper() <= 'Ú':
            contar += 1
            flag = True

    if flag:
        print( Fore.RED + palabra, '',end='' )
    else:
        print( palabra, '', end='')