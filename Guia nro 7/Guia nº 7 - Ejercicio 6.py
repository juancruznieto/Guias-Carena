#Ejercicio 6:
#A partir de una cadena de texto (no pueden ser todas mayúsculas) realizar cada punto y mostrar el resultado en pantalla.
texto = 'De acuerdo con Van Rossum, Python simplemente utiliza demasiada memoria y energía del ' \
    'hardware, por lo que el no le ve futuro en la creación de sitios web, además de los servicios ' \
    'Back End y su uso en WebAssembly, explicó el portal ZDNet. «Las personas que han logrado usar ' \
    'CPython en una tableta Android o iOS han encontrado que necesita demasiados recursos», resaltó ' \
    'el programador.'
#Colocar la palabra en una lista (Split).
lista = texto.split()
print(lista)
print()
#Desarrollar un bucle while para el ingreso de una palabra a buscar en la lista.
while True:
    palabra = input('Ingrese una palabra a buscar: ')

#Salir cuando no se ingrese ningún valor (Enter).
    if palabra == '':
        break
#Buscar la palabra en la lista y mostrar si se encontró o no, y su posición en la lista.
    if palabra in lista:
        print('La palabra se encontro en la posicion: ', lista.index(palabra))
    else:
        print('La palabra no se encontro')

#Unir el vector en una nueva cadena con el primer carácter en mayúscula y el resto como está originalmente (Join, capitalize).
nuevo_texto = ' '.join(p.capitalize() for p in lista)
print(nuevo_texto)
