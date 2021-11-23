#Realice un algoritmo que:
#Permita el ingreso de 12 valores entre 1 y 100.
#Salir con -1 en caso de no completar la lista de los 12 números.
#Validar que el valor ingresado esté entre 1 y 100 inclusivos.
#Contar y acumular los divisibles por 2. (número % 2)
#Contar y acumular los no divisibles por 2. (else)
#Mostrar los resultados en caso de completar la lista.
#En caso de no completar la lista mostrar el mensaje “No ha completado la lista de 12 números”.

con1 = 0
con2 = 0
acum1 = 0
acum2 = 0

while con1 + con2 < 12:
    num = int(input('Ingrese un valor entre 1 y 100 '))
    if num == -1:
        break
    if num < 1 or num > 100:
        print('Valor fuera de rango')
        continue
    if num % 2 == 0:
        con1 = con1 + 1
        acum1 = acum1 + num
    else:
        con2 = con2 + 1
        acum2 = acum2 + num

print('Cantidad de valores divisibles por dos: ', con1)
print('Valores acumulados divisibles por dos: ', acum1)
print('Cantidad de valores no divisibles por dos: ',con2)
print('Valores acumulados no divisibles por dos: ',acum2)
if con1 + con2 < 12:
    print('No se completaron los doce numeros')

