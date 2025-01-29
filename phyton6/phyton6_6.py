#AVANZADO (para el 10)
#6.6 Árbol de navidad en Python. Imprime un árbol de navidad formado con *
#haciendo uso del while y de la multiplicación de un entero por una cadena,
#cuyo resultado en Python es replicar la cadena.
# *
# ***
# *****
# *******
# *********
# ***********

n = int(input("Introduce que altura de árbol quieras: "))
n2 = 1

while n2 <= n:
    nada = n - n2
    estrella = (2*n2) - 1
    print (" "*nada + "*"*estrella)
    n2 = n2 + 1