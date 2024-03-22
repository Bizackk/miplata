import json

def inisioSesion():
    usuario = input("Digite su nombre de usuario: ")
    contrasena = input("Digite su contrasena: ")
    contador = 0
    
    try:
        with open('almacenamiento.txt', 'r') as f:
            for linea in f:
                datos_usuario = json.loads(linea.strip())
                if datos_usuario['usuario'] == usuario and datos_usuario['contraseña'] == contrasena:
                    print(f"¡Hola {datos_usuario['usuario']} has iniciado sesión correctamente!")
                    return True
                elif datos_usuario['usuario'] == usuario and datos_usuario['contraseña'] != contrasena:
                    contador += 1
                    print(f"Contraseña incorrecta. Intento {contador} de 3.")
                    if contador == 3:
                        print("Has excedido el número máximo de intentos de inicio de sesión. La cuenta está bloqueada por 24 horas.")
                        return False
            print("Usuario o contraseña incorrecto, intenta de nuevo.")
    except FileNotFoundError:
        print("No se encontró el archivo de almacenamiento de usuarios.")
    
    return False