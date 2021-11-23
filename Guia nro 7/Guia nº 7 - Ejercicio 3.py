#Ejercicio 3:
#A partir de una cadena de texto inicializada en el código, convertir a una lista p de palabras y mostrar.
texto ='Según Mark Zuckerberg: «Saber que una ardilla muere en tu jardín puede ser másrelevante para tus intereses que saber que en África muere gente»'
#Mostrar el elemento menor (en cantidad de caracteres), mayor (en cantidad de caracteres) y su posición en la lista p (aplicar min y max con el parámetro key = len)
#ejemplo: menor = min(palabras, key = len).
p = texto.split()
print('\n', p)
menor = min(p,key = len)
mayor = max(p,key =len)
posmin = p.index(menor)
posmax = p.index(mayor)
print('El menor elemento es:','"'+ menor+'"', 'en la posicion', posmin)
print('El mayor elemento es:','"'+ mayor+'"', 'en la posicion', posmax)
#Concatenar los elementos de la lista en una nueva cadena nuevo_texto pero en sentido inverso, es decir donde el primer elemento sea el último elemento de p y mostrar al finalizar (aplicar join con for reversed).
nuevo_texto = ' '.join(reversed(p))

print(nuevo_texto)

#Crear una función para mostrar la lista p, llamar desde main.
def mostrar_lista(l):
    for indice, valor in enumerate(1):
        print(indice, valor)

    return

mostrar_lista(p)