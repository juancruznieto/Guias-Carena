#Ejercicio 5:
#1 Permitir el ingreso de una serie de temperaturas entre -60 y 60 (no debe permitir valores fuera del rango).
#2 Salir con 100.
#3 Obtener la cantidad y el promedio de las lecturas menores a cero grados.
#4 Obtener la cantidad y el promedio de las lecturas mayores o igual a cero grados.
#5 Obtener la lectura menor y mayor de la serie.
acum_menor = 0
cont_menor = 0
acum_mayor = 0
cont_mayor = 0
menor = 61
mayor = -61
while True:
    valor = int(input('Ingresar una temperatura entre -60 y 60  : '))
    if valor == 100:
        break
    if valor <= -60 or valor >60:
        print('Valor fuera de rango')
        continue

    if valor <0:
        acum_menor += valor
        cont_menor += 1
    if valor >0:
        acum_mayor += valor
        cont_mayor =+1

    if valor < menor:
        menor = valor
    if valor > mayor:
        mayor = valor
if cont_menor + cont_mayor > 0:
    print()
    print('Cantidad de valores menores a 0 ',cont_menor)
    print('promedio de valores menores a 0 ',acum_menor / cont_menor)
    print('Cantidad de valores mayores a 0 ',cont_mayor)
    print('promedio de valores mayores a 0 ',acum_mayor / cont_mayor)
    print('Elemento menor de la serie ', menor)
    print('Elemento mayor de la serie ', mayor)
