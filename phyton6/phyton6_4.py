#6.4 Pide al usuario su nombre y un número. Después de esto, muestra por
#pantalla, su nombre el número de veces que haya elegido. Comprueba y evita
#que se produzcan errores.

nombre = input("Dime tu nombre: ")
n1 = int(input("Dime un número: "))
n2 = n1 
while n1 != 0 :
    n1 = (n1 - 1)
    print ("Este es tu nombre", nombre, "y este es tu número", n2)