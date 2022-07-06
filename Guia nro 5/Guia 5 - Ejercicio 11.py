#Ejercicio 11:
#A partir de un texto:
texto = 'Phylion aprovechó la 30ª Feria Internacional de la Bicicleta de China celebrada en ' \
    'Shanghái para presentar un escaparate de las últimas tecnologías, nuevos productos y ' \
    'nuevos servicios para las bicicletas eléctricas.'
#Mostrar en pantalla la cadena completa.
print(texto)
print()
#Pasar el texto a un vector de palabras.
v = texto.split()
#Recorrer el vector y encerrar entre paréntesis aquellas palabras que empiecen con una vocal minúsculas, mayúscula o acentuada.
for i in range(len(v)):
    #palabra = lista[i]
    letra = v[i][0:1]
    if letra == 'a' or letra == 'á' or letra == 'A' or letra == 'Á' or \
        letra == 'e' or letra == 'é' or letra == 'E' or letra == 'É' or \
        letra == 'i' or letra == 'í' or letra == 'I' or letra == 'Í' or \
        letra == 'o' or letra == 'ó' or letra == 'O' or letra == 'Ó' or \
        letra == 'u' or letra == 'ú' or letra == 'U' or letra == 'Ú':
        v[i] = '(' + v[i] + ')'
#Armar o concatenar el vector en otra variable String como por ejemplo nuevotexto.
#Imprimir el nuevo texto.
nuevo_texto = ' '.join(v)
print(nuevo_texto)