#Marcos Aguilera Alenda 5/2/25

"""Realizar un algoritmo que pida números (se pedirá por teclado la
cantidad de números a introducir). El programa debe informar de cuantos
números introducidos son mayores que 0, menores que 0 e iguales a 0.
"""

datos = []
ma = 0
me = 0
ig = 0

n1 = int(input("Introduce la cantidad de números que me vas a dar a continuación: "))

#Le asigno a datos (array) los números que me da el usuario
for i in range(0,n1):
    datos.append(int(input("Dame un número entero: ")))

#Para poder tener la cantidad de números mayores menores e iguales he utilizado las variables ma, me y ig como si fuera un contador, cada vez que pasa por ahí se le sumara 1.
for i in range(0,n1):
    if (datos[i]) > 0:
        ma = (ma+1)
    elif (datos[i]) < 0 :
        me = (me+1)
    else:
        ig = (ig+1)

print (" ")
print ("Tras analizar los números que me has dado te puedo decir que me has dado: ", ma, "números mayores que 0,", me, "menores que 0 y", ig, "iguales a 0.")