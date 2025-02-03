#Crea un array con los número 10, 20, 30, 40 y 50 y luego muestra los que hay
#en las posiciones impares (primero, tercero y quinto: 10, 30 y 50)

#datos = [10, 20, 30, 40, 50 ]

#print("Imprimimos la primera y la tercera: ")
#print(datos[0])
#print(datos[2])
#print(datos[4])

datos = [10, 20, 30, 40, 50]

print("Imprimimos la primera, tercera y quinta: ")
for i in range(0,5,2) :
    print(datos[i])