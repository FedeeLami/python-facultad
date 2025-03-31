"""
Escribe un programa que tome una lista de números enteros como entrada
del usuario. Luego, convierte cada número en la lista a string y únelos en
una sola cadena, separados por guiones ('-'). Sin embargo, excluye cualquier
número que sea múltiplo de 3 de la cadena final.
"""
import random
lista = []

rango = random.randint(1,100)

for i in range(rango):
    n = random.randint(1,9)
    lista.append(n)

cadena = ''

for i in lista:
    if i % 3 != 0:
        cadena += str(i) + ' - '

print(cadena)
