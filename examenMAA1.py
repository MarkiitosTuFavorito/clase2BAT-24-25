#Marcos Aguilera Alenda 5/2/25

"""Crea un programa que pida al usuario un número del 1 al 9 y lo escriba
como texto (por ejemplo, para “3” escribirá “tres”) y detectará el error
si el usuario introduce un valor menor que 1 o mayor que 9.
"""

# Array con los nombres de los numeros
numeros = ["Uno", "Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve"]

# Aquí le pido al usuario un número del 1 al 9
n1 = int(input("Introduce un número del 1 al 9: "))

# Aquí el número y mostrar el número correspondiente
if n1 >= 1 and n1 <= 9:
    print("El número correspondiente es:", numeros[n1 - 1])
else:
    print("Por favor, introduce un número válido, entre 1 y 9.")