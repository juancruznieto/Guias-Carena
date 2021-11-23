#Ejercicio 4:



def mostrar_lista(l):
    for i, v in enumerate(l):
        print(i,v)

    return

def may_men_prom(l):
    mayor=min(l)
    menor=max(l)
    prom=sum(l) / len(l)

    print('Mayor elemento', mayor)
    print('Menor elemento', menor)
    print('Promedio de valores', prom)

    return

#Crear un código para ingresar n valores decimales entre 1 y 100, salir con cero.
V1 =[]
V2 =[]

while True:
    valor = int(input('Ingrese un valor entre 1 y 100: '))

    if valor == 0:
        break
    if valor < 1 or valor > 100:
        print('Valor fuera de rango.')
        continue
#Guardar los valores ingresados en una lista v1 y hacer una copia en una segunda 
#lista v2 con los valores del primero que sean mayor a 50 (sintaxis por comprensión).
V1.append(valor)

print(V1)
V2 = [x for x in V1 if x > 50]
print(V2)

#Crear una función para mostrar todos los elementos de un vector cualquiera y su posición,
#llamarla desde el main para mostrar v1 y v2.
mostrar_lista(V1)
mostrar_lista(V2)
#Crear una función para encontrar el mayor menor y el promedio de una lista cualquiera, llamar desde el main para mostrar los resultados de v1 y v2.
may_men_prom(V1)
may_men_prom(V2)
