#Instancia evaluativa final integradora - b - Programación

#Realizar un código Python que incluya el siguiente texto en una cadena y realice los puntos abajo indicados:


cadena = 'Copilot está basado en el algoritmo Codex de OpenAI, un sistema de inteligencia artificial  que es capaz de "traducir lenguaje natural a código". Este sistema es un descendiente del espectacular GPT-3 que se ha convertido en una de las grandes sorpresas de la aplicación práctica de la inteligencia artificial.'


print(cadena)
print()
#Definir una función texto_a_palabras1 que reciba como parámetro el texto y retorne
# una lista con las palabras y la cantidad, llamar la función desde el programa principal,
# guardar el resultado en lista1 y cantidad1, mostrar los resultados por consola.
def texto_a_palabras1(texto):
    lista1 = texto.split()
    cantidad1 = 0
    for x in lista1:
        if x in lista1:
            cantidad1 += 1
    return print('Los elemento de la lista son: ',lista1, 'La cantidad de elementos de lista1 son: ',cantidad1)

texto_a_palabras1(cadena)
print()
#Definir una función texto_a_palabras2 que reciba como parámetro el texto y retorne
#una lista con las palabras y la cantidad, que no comiencen o no terminen con
# caracteres alfabéticos, llamar la función desde el código principal,
# guardar el resultado en lista2 y cantidad2, mostrar los resultados por consola.
def texto_a_palabras2(texto):
    lista1 = texto.split()
    lista2 = 0
    cantidad2 = 0
    for p in lista1:
        if p[0].isalpha() or p[-1].isalpha():
            continue
        else:
            cantidad2 += 1
            lista2.append(p)
    print('Los elementos de la lista son: ',lista2)
    print('Cantidad de palabras es de: ',cantidad2)


texto_a_palabras2(cadena)
print()
#Definir una función texto_a_palabras3 que reciba como parámetro el texto y retorne
#una lista con las palabras y la cantidad, que solo comiencen y terminen
# con caracteres alfabéticos y la cantidad de elementos, llamar la función desde el
# programa principal, guardar el resultado en lista3 y cantidad3, mostrar los resultados
# por consola.
def texto_a_palabras3(texto):
    lista1 = texto.split()
    lista3 = 0
    cantidad3 = 0
    for p in lista1:
        if p.isalpha[0] or p.isalpha[-1]:
            cantidad3 += 1
            lista3.append(p)
    return print('Los elementos de la lista son: ',lista3,'Cantidad de palabras es de: ',cantidad3)

texto_a_palabras3(cadena)
print()
#Definir una función texto_a_palabra4 que reciba como parámetro el texto,
# obtenga un nuevo texto solo con caracteres alfabéticos y/o dígitos, luego obtenga
#y retorne una lista con las palabras y la cantidad, llamar la función desde el programa
#principal, guardar el resultado en lista4 y cantidad4, mostrar los resultados por consola.
def texto_a_palabras4(texto):
    lista1 = texto.split()
    lista4a = []
    cantidad4 = 0
    for p in lista1:
        if p.isalpha() or p.isdigit():
            cantidad4 += 1
            lista4a.append(p)
    lista4 = ''.join(lista4a)
    return print('Los elementos de la lista 4 son: ',lista4, 'Cantidad de palabras es de: ',cantidad4)
texto_a_palabras4(cadena)
print()
#Definir una función contar_vocales_consonantes que reciba como parámetro el texto,
#cuente cuantas vocales y consonantes tiene el texto, llamar la función desde el
#programa principal, guardar el resultado en  vocales y consonantes, mostrar resultado
#por consola

def contar_vocales_consonantes(texto):
    vocales ='aeiouAEIOU'
    voc = []
    cons = []
    for x in texto:
        if x in vocales:
            voc += 1
        else:
            cons += 1
        continue
    print('Cantidad de vocales en el texto: ',voc)
    print('Cantidad de consonantes en el texto: ',cons)

contar_vocales_consonantes(cadena)
print()