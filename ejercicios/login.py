base_datos = {
    "usuario1": "contrasena1",
    "usuario2": "contrasena2",
    "usuario3": "contrasena3",
    "usuario4": "contrasena4",
    "usuario5": "contrasena5"
}

def login(usuario:str, contraseña:str):
    if usuario in base_datos:
        print("Usuario existe")
        if contraseña == base_datos[usuario]:
            print("Bienvenido")
            return True
        else:
            print("contraseña invalida")
            return False
    else:
        print("ususario no existe")
        return False

def main():
    user = input("ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    resultado = login(user, password)
    
    cont = 0 
    while resultado == False:
        user = input("ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        resultado = login(user, password)
        if resultado == False:
            cont += 1
            if cont == 3:
                print("Exedió el limite de intentos. Vuelva a intentar más tarde")
                break
        else:
            print("Acceso concedido")
            break





if __name__ == "__main__":
    main()