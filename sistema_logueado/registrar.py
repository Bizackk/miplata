import json

almacenamiento = []
indice_actual = 0
    
def cargarUsuarios():
    global almacenamiento
    try:
        with open('almacenamiento.txt', 'r') as archivo:
            lineas = archivo.readlines()
            if lineas:
                almacenamiento = [json.loads(linea.strip()) for linea in lineas]
            else:
                almacenamiento = []
    except FileNotFoundError:
        almacenamiento = []
    return almacenamiento


def guardarUsuarios():
    with open('almacenamiento.txt', 'w') as archivo:
        for usuario in almacenamiento:
            archivo.write(json.dumps (usuario) + '\n')


def registrarUsuarios():
    
    global indice_actual
    indice_actual += 1
    
    id_usuario = input("Ingrese el ID del usuario: ")
    nombre_usuario = input("Ingrese el nombre del usuario: ")
    correo_usuario = input("Ingrese el correo electrónico del usuario: ")
    contraseña_usuario = input("Ingrese la contraseña del usuario: ")
    
    almacenarUsuarios(id_usuario,nombre_usuario,correo_usuario,contraseña_usuario)
    
     
def almacenarUsuarios(id , usuario , correo , contraseña):
    
    nuevo_usuario = {
        'id': id,
        'usuario': usuario,
        'correo': correo,
        'contraseña': contraseña 
    }
    almacenamiento.append(nuevo_usuario)
    guardarUsuarios()
    

def imprimir_informacion_personal():
    
    usuario_ingresado = input("ingrese su usuario: ")
    contraseña_ingresado = input("ingrese su contraseña: ")
    
    for usuario in almacenamiento:
        if usuario['usuario'] == usuario_ingresado and usuario['contraseña'] == contraseña_ingresado:
            print (f"Información del usuario: Identificación: {usuario['id']} - Usuario: {usuario['usuario']} - Correo: {usuario['correo']} - Contraseña: {usuario['contraseña']}")
        elif usuario['usuario'] == usuario_ingresado:
            print (f"{usuario['usuario'].capitalize()}: La contraseña es incorrecta")
    
    
almacenamiento = cargarUsuarios()