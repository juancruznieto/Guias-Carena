#Ejercicio 5:
#A partir de un texto:
texto = 'Phylion aprovechó la 30ª Feria Internacional de la Bicicleta de China celebrada en ' \
    'Shanghái para presentar un escaparate de las últimas tecnologías, nuevos productos y ' \
    'nuevos servicios para las bicicletas eléctricas.'
#Mostrar en pantalla la cadena completa.
print(texto)
#Encontrar las vocales y reemplazarlas según la siguiente lista
#  (a - 1, e - 2, i - 3, o - 4, u - 5)
texto_nuevo = texto.replace('a','1')
texto_nuevo2 = texto_nuevo.replace('e','2')
texto_nuevo3 = texto_nuevo2.replace('i','3')
texto_nuevo4 = texto_nuevo3.replace('o','4')
texto_nuevo5 = texto_nuevo4.replace('u','5')
#Mostrar como queda la nueva cadena o la cadena original modificada.
print()
print(texto_nuevo5)
