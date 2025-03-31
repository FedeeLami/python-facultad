"""
Implementa un programa que solicite al usuario que ingrese una lista de
números. Luego, imprime la lista pero detén la impresión si encuentras un
número negativo. Nota: utilice la sentencia break cuando haga falta.
"""

n = None
lista = []

while n != 0:
    n = int(input('Ingrese un numero entero o 0 para finalizar:'))
    lista.append(n)


for i in lista:
    if i>0:
        print(i)
    else:
        break
