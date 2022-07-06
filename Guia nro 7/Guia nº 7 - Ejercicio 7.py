#Ejercicio 7:
#1 Generar un vector de 30 números enteros al azar de 2 dígitos.
import random
v = random.sample(range(99),30)
#2 Mostrar cada elemento y su posición (enumerate).
for indice, valor in enumerate(v):
    print(indice, valor)

#3 Encontrar el elemento menor y su posición por arriba del valor 50 (aplicar sintaxis por comprensión o filter).
menor = min(valor for valor in v if valor > 50)
print(menor)
#4 Encontrar el elemento mayor y su posición por debajo del valor 50 (aplicar sintaxis por comprensión o filter).
mayor = max(valor for valor in v if valor < 50)
print(mayor)