#Ejercicio 10:
#A partir de un texto:
texto = 'Phylion aprovechó la 30ª Feria Internacional de la Bicicleta de China celebrada en ' \
    'Shanghái para presentar un escaparate de las últimas tecnologías, nuevos productos y ' \
    'nuevos servicios para las bicicletas eléctricas.'
#Mostrar en pantalla la cadena completa.
print(texto)
#Imprimir nuevamente el texto pero con  los artículos (el, la, los, las, un, una
#, unos, unas) encerrados entre asteriscos (ej: *el*)
#(Trabajarlo con una lista)
l = texto.split()

for x in l:
    if x == 'el' or x == 'la' or x == 'los' or x == 'las' or x == 'un' or x =='una'or x== 'unos' or x =='unas':
        print( '*',x,'* ', end= '')
    else:
        print(x + ' ', end= '')

