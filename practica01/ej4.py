"""
Cree un programa que dada una lista de números imprima sólo los que son
pares. Nota: utilice la sentencia continue donde haga falta
"""
import random
lista = []

rango = random.randint(1,100)

for i in range(rango):
    n = random.randint(1,100)
    lista.append(n)

for i in lista:
    if (i % 2 == 0):
        print(i)
