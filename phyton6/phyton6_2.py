#6.2 Pide una clave y una contraseña al usuario. No se le dejará proseguir hasta
#que el código sea admin y la clave 0987. Debes utilizar conectores lógicos (and,
#or, not,...)

contraseña = input("Dame la contraseña: ")
clave = input("Dame la calve: ")

while contraseña != "admin" and clave != "0987" :
    print("CLAVE O/Y CONTRASEÑA INCORRECTA")
    contraseña = input("Dame la contraseña: ")
    calve = input("Dame la calve: ")
print ("Exacto la contraseña es admin y la clave es 987")