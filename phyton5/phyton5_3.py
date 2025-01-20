año = int(input("Dame un año y t dice si es bisiesto o no: "))
n1 = año%100
n2 = año % 400
n3 = año % 4

if n3 == 0 and n1 != 0 or n2 == 0: 
    print ("Este es bisiesto")
else :
    print ("Este año no es bisieseto")

