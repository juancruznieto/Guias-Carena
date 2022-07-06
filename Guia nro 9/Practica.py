v1 = [47,89,19,51,37,32,28,20,96,13,10,79]

print('v', v1)
#x se refiere al valor, al elemento, o al contenido de la lista
#muestra todos los elementos
''''''
for x in v1:
    print(x, end= ' ')

print()
''''''
#Muestra el indice
for x in range (12):
    print(x,end= ' ')


print()

#mostra los elementos de las poiciones pares.
for x in range(12):
    if x % 2 == 0:
        print(x,v1[x])

for x in range(0,12,2):
    print(x,v1[x])
print()

#muestra los elementos pares
for x in v1:
    if x % 2 == 0:
        print(v1.index(x),x)
print()

for x in range(12):
    if v1[x] % 2 ==0:
        print(x,v1[x])
print()

for x,y in enumerate(v1):
    if x % 2 == 0:
        print(x,y)


#obtener los elementos pares en la pocicion impar

print()

for x,y in enumerate (v1):
    if x % 2 !=0 and y % 2 ==0:
        print(x,y)

print()

v2 = [y for x, x in enumerate (v1) if x %2 != 0 and y % 2 == 0]
print(v2)


print(v1[3:9])

for x in range (1,12,2):
    if v1[x] % 2 == 0:
        print(x,v1[x])

for x in range(3,9):
    print(x,v1[x])
print




