#Pide al usuario un número del 1 al 12 y escribe el número del mes
#correspondiente (1 = enero, 2= febrero,..) usando un array.

#datos = []

#datos.append(int(input("Dame un número del 1 al 12 y te dire a que mes corresponde: ")))


# Array con los nombres de los meses
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Pedir al usuario un número del 1 al 12
n1 = int(input("Introduce un número del 1 al 12: "))

# Validar el número y mostrar el mes correspondiente
if n1 >= 1 and n1 <= 12:
    print("El mes correspondiente es:", meses[n1 - 1])
else:
    print("Por favor, introduce un número válido entre 1 y 12.")
