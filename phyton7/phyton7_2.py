#7.2 Pide al usuario un número entero (por ejemplo, 5) y muestra la tabla de
#multiplicar de ese número( Ejemplo: “5 x 1 = 5” hasta “5 x 10 = 50”)

n = int(input("Dime un número entero: "))
n1 = 1
for n1 in range (1,11) :
    print (n, "x", n1, "=", n*n1, )
