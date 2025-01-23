#6.5 Realiza un programa que lea dos números por teclado y permita elegir entre
#4 opciones en un menú
#1 - Mostrar la suma de los dos números
#2 - Mostrar la resta de los dos números (el primero menos el segundo)
#3 - Mostrar la multiplicación de los dos números
#4 - Salir del programa
#En caso de introducir una opción inválida, el programa volverá a solicitar otra
#opción hasta que el usuario elija salir.

print ("A continuación te pedire dos número y con esos números te ofrecere hacer diferentes cosas con ellos -> ")
n1 = int(input("Dime un número: "))
n2 = int(input("Dime otro número: "))

print (" ")
print ("Teclea la opcion que desees: ")
print (" ")
print ("1 - Mostrar la suma de los dos números")
print ("2 - Mostrar la resta de los dos números (el primero menos el segundo)")
print ("3 - Mostrar la multiplicación de los dos números")
print ("4 - Salir del programa")
n3 = int(input("-> "))


while  (n3 != 1 ) or (n3 != 2) or (n3 != 3) or (n3 != 4) :
    print (" ")
    print ("INCORRECTO")
    print ("Teclea la opcion que desees: ")
    print (" ")
    print ("1 - Mostrar la suma de los dos números")
    print ("2 - Mostrar la resta de los dos números (el primero menos el segundo)")
    print ("3 - Mostrar la multiplicación de los dos números")
    print ("4 - Salir del programa")
    n3 = int(input("-> "))
 
if n3 == 1:
    print (("La suma de "), n1, ("y"), n2, ("es :"), n1 + n2)
elif n3 == 2 :
    print (("La resta de "), n1, ("y"), n2, ("es :"), n1 - n2)
elif n3 == 3 :
    print (("La multiplicación de "), n1, ("y"), n2 ("es :"), n1 * n2)
elif n3 == 4 :
    print ("Buenos pues nada hasta luego.")