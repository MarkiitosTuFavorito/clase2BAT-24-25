#6.1 Crea un programa que pida al usuario que introduzca la suma de 135 y 768.
#Deberá repetirse hasta que se introduzca el resultado correcto


suma = int(input("Dame la suma de 135 y 768: "))

while suma != 903 :
    suma = int(input("INCORRECTO. Dame la suma de 135 y 768: "))
print("Exacto la suma es 903")