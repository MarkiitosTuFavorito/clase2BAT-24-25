#7.3 Pide al usuario un número entero (por ejemplo, 58) y nos dé todos los
#múltiplos de 7 que hay entre el número 1 y ese número (incluido)

n = int(input("Dime un número entero: "))
n1 = 1

for n1 in range (0,n+1,7):
  print (n1)