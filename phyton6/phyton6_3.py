#6.3 Escriba un programa que pregunte una y otra vez si desea continuar con el
#programa, siempre que se conteste exactamente sí (en minúsculas y con tilde).

contraseña = input("Deseas continuar con el programa?: ")
while contraseña == "sí" :
    contraseña = input("Deseas continuar con el programa?: ")
print ("Bueno pues nada si no quieres continuar adios.")