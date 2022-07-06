from colorama import init, Style, Fore, Cursor, Back
init(True)


#1 A partir de una cadena de texto:
texto = 'Phylion aprovechó la 30ª Feria Internacional de la Bicicleta de China celebrada en ' \
    'Shanghái para presentar un escaparate de las últimas tecnologías, nuevos productos y ' \
    'nuevos servicios para las bicicletas eléctricas.'

#2 Mostrar en pantalla la cadena completa.
print('\n')
print(texto)
print('\n')

#3 Solicitar al usuario ingrese una palabra a buscar en el texto.
while True:
    palabra = input('Ingrese la palabra a buscar: ')

    if palabra == '':
        break

    buscar = texto.find(palabra)

    #4 Si la palabra se encuentra mostrar el texto con la palabra coloreada en rojo
    #sino mostrar el cartel “La palabra no se encuentra”.
    if buscar == -1:
        print('La palabra no se encuentra.')
    else:
        print(Fore.RED + palabra)

    print('\n')