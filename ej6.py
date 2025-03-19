"""
Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas
listas, una con los número pares y otras con los que son impares. Imprima
las listas al terminar de procesarlas
"""

import random
lista = []

rango = random.randint(1,100)

for i in range(rango):
    n = random.randint(1,100)
    lista.append(n)

listaPar = []
listaImpar = []

for i in lista:
    if (i % 2 == 0):
        listaPar.append(i)
    else:
        listaImpar.append(i)

print(listaPar)
print(listaImpar)