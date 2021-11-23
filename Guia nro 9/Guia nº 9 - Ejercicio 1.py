# Escribir una funcion que reciba como parametro una cadena de palabras separadas por espacios
#y que devuelva como resultado, cuantas palabras de mas de cinco letras tiene la cadena

cadena= 'conocé las últimas noticias de Boca y todas las novedades de hoy, lunes 4 de octubre.'
'El Xeneize perdió 2-1 ante River en una nueva edición del Superclásico'
'del fútbol argentino y así Sebastián Battaglia cortó su invicto de ocho partidos.'

v= cadena.split()

c = 0
for x in v:
    if len(x) > 5:
        c += 1
print(c)

s= len([x for x in v if len(x) >5])
print(s)
f= len(list(filter(lambda x: len(x) > 5, v)))
print(f)