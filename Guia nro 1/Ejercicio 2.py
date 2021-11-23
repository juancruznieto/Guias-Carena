#Desarrollar un algoritmo para el cálculo de la hipotenusa:

#Importar la librería math para obtener la raíz cuadrada (import math).
import math
#Mostrar mensaje de ingreso y guardar cateto A en A.
A = int(input('ingrese un valor para cateto a: '))

#Mostrar mensaje de ingreso y guardar cateto B en B.
B = int(input('ingrese un valor para cateto b: '))

#Calcular y guardar hipotenusa en C “C = math.sqrt( pow(A,2) + pow(B,2) )” o “C = math.sqrt(A ** 2 + B ** 2)”
C = math.sqrt(A ** 2 + B ** 2)
#Mostrar mensaje con el resultado de C.
print('El valor de la hipotenusa es: ',C)
