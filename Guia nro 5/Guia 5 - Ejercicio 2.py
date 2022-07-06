#Guía 5 - Ejercicio 2:
from colorama import init, Style, Fore, Cursor, Back
init(True)

#1 A partir de una cadena de texto:
texto = 'Phylion aprovechó la 30ª Feria Internacional de la Bicicleta de China celebrada en ' \
    'Shanghái para presentar un escaparate de las últimas tecnologías, nuevos productos y ' \
    'nuevos servicios para las bicicletas eléctricas.'

#Mostrarlo en pantalla la cadena completa.
print(texto + '\n')

#Pasar el texto a un vector de palabras.
lista = texto.split()
print(lista)
print('\n')

#Recorrer el vector.
for palabra in lista:
    #Determinar si la palabra o elemento comienza en mayúscula.
    #Si empieza con mayúscula imprimir en color rojo sino imprimir en blanco, deben formar un párrafo.
    letra = palabra[0:1]
    if ord(letra) >= 65 and ord(letra) <= 90:
        print(Fore.RED + palabra + ' ', end='')
    else:
        print(palabra + ' ', end='')