#De un grupo de n notas de calificación de alumnos ingresadas
#  por teclado:
#Salir con -1.
#Ingresar valores enteros entre 1 y 10.
#Contar cuantas notas son menores a 7.
#Sacar el promedio de notas menores a 7.
#Contar cuantas notas son mayores o iguales a 7
#Sacar el promedio de notas mayores o iguales a 7.
#Mostrar los resultados de la cantidad de notas y los promedios.

cont1 = 0
acum1 = 0
prom1 = 0
cont2 = 0
prom2 = 0
acum2 = 0

while True:
    n = int(input('Ingrese la calificacion del alumno: '))
    if n == -1:
        break
    if n < 0 or n > 10:
        continue
    if n < 7:
        cont1 += 1
        acum1 += n
    if n >= 7:
        cont2 += 1
        acum2 += n
if cont1 != 0:
    prom1 = acum1 / cont1
if cont2 != 0:
    prom2 = acum2 / cont2
print('\n')
print('Notas menores a 7: ', cont1)
print('Notas mayores a 7: ',cont2)
print('Promedio de notas mayores a 7: ',prom1)
print('Promedio de notas menores a 7: ',prom2)
print('Fin del programa')