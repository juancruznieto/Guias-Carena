#1 A partir de una cadena de texto iniciada en el código, mostrar la cadena en color azul.

#Encontrar y mostrar el elemento menor, mayor y su posición en el vector p,
#  inicializar menor con el primer elemento del vector y mayor con nada (“”).
from colorama import Fore, init
init(True)
texto ='Según Mark Zuckerberg: «Saber que una ardilla muere en tu jardín puede ser másrelevante para tus intereses que saber que en África muere gente»'


print('\n', Fore.BLUE + texto)
#2 En el texto quitar los caracteres que no sean letras ni números,
#mostrar nuevamente el texto en blanco, utilizar la función Replace para quitar.
nuevo_texto = ''
for caracter in texto:
    if (caracter.upper() >='A' and caracter.upper() <= 'Z') or caracter.isspace():
        nuevo_texto += caracter

print('\n', nuevo_texto)
#3 Convertir el texto en un vector p() de palabras y mostrar todos los elementos y su
#  posición en blanco.

palabras = texto.split()
for indice, valor in enumerate(palabras):
    print(indice,valor)

menor = palabras [0]
for x,palabra in enumerate(palabras):
    if len(palabra) < len(menor):
        menor = palabra
        posmenor = x

mayor = ''
for x,palabra in enumerate(palabras):
    if len(palabra) > len(mayor):
        mayor = palabra
        posmayor = x
print()









