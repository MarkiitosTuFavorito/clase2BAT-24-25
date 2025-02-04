#Crea un programa que pida al usuario 12 números enteros, los guarde en un
#array y luego le pregunte de forma repetitiva qué número quiere buscar. Le
#responderá si dicho número estaba o no entre los datos que se habían
#introducido inicialmente. Dejará de repetirse cuando se introduzca el número 0.

datos = [] 

for i in range(0,12):
    datos.append(int(input("Dame un número entero: ")))

n1 = int(input("Dime un número que quieras buscar y te dire si esta entre los números que me has dicho: "))

while  n1 != 0 :
    if n1 == (datos[i]):
        print("El número ", n1, "esta entre los números que me has dado anteriormente")
        n1 = int(input("Dime otro número que quieras buscar y te dire si esta entre los números que me has dicho: "))
    elif n1 != (datos[i]):
        print("El número ", n1, "no esta entre los números que me has dado anteriormente")
        n1 = int(input("Dime otro número que quieras buscar y te dire si esta entre los números que me has dicho: "))



print("Hasta luego")


