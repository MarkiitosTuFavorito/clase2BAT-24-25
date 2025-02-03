#Pide al usuario un número del 1 al 12 y escribe el número del mes
#correspondiente (1 = enero, 2= febrero,..) usando un array.

#datos = []

#datos.append(int(input("Dame un número del 1 al 12 y te dire a que mes corresponde: ")))


# Array con los nombres de los meses
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Pedir al usuario un número del 1 al 12
numero = int(input("Introduce un número del 1 al 12: "))

# Validar que el número esté en el rango correcto
if 1 <= numero <= 12:
    # Usar un bucle for para recorrer los meses
    for i in range(len(meses)):
        if i == numero - 1:  # Comparar el índice con el número ingresado
            print(f"El mes correspondiente es: {meses[i]}")
            break  # Salir del bucle una vez encontrado el mes
else:
    print("Número fuera de rango. Por favor, introduce un número entre 1 y 12.")
