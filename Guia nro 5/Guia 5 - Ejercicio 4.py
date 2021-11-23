#Guía 5 - Ejercicio 4.py
from colorama import Fore, init
init(True)

# 1 A partir de un texto:
texto = 'De acuerdo con Van Rossum, Python simplemente utiliza demasiada memoria y energía del ' \
    'hardware, por lo que el no le ve futuro en la creación de sitios web, además de los servicios ' \
    'Back End y su uso en WebAssembly, explicó el portal ZDNet. «Las personas que han logrado usar ' \
    'CPython en una tableta Android o iOS han encontrado que necesita demasiados recursos», resaltó ' \
    'el programador.'

# 2 Mostrar en pantalla la cadena completa.
print(texto, '\n')

# 3 Encontrar cada unos de los artículos de la lista (el, la, los, las, un, una, unos, unas)
# e imprimir el artículo y la posición dentro de la cadena de cada aparición.
# Hacemos un diccionario con las palabras a buscar.
dictio = {'el':0, 'la':0, 'los':0, 'las':0, 'un':0, 'una':0, 'unos':0, 'unas':0}

# 4 Contar y mostrar cuantos artículos de cada uno se encontraron.
for palabra in dictio:
    indice = 0

    while indice < len(texto):
        buscar = texto.find(' ' + palabra + ' ', indice)

        if buscar > -1:
            print('Se encontró ','"', palabra, '"', 'en la posición', buscar)
            indice = buscar + 1
            dictio[palabra] += 1
        else:
            break

print()

for clave, valor in dictio.items():
    print('Cantidad de apariciones de la palabra', clave, valor)



#Contar y mostrar cuantos artículos de cada uno se encontraron.
