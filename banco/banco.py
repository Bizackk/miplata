import json

def cargar_datos():
    try:
        with open('datos.json', 'r') as file:
            datos = json.load(file)
    except FileNotFoundError:
        datos = {'saldo': 0}
    return datos

def guardar_datos(datos):
    with open('datos.json', 'w') as file:
        json.dump(datos, file)
        
def consignar():
    datos = cargar_datos()
    saldo = datos['saldo']
    cuanto = input("Cuánto dinero depositará: ")
    nuevoSaldo = saldo + int(cuanto)
    datos['saldo'] = nuevoSaldo  
    guardar_datos(datos)
    print(f"Has depositado la cantidad de {cuanto}$ y tu saldo ahora es de {datos['saldo']}$")
    
def retirar():
    datos = cargar_datos()
    
    saldoDisponible = datos['saldo']
    cantidadRetiro = int(input("Cuanto va a retirar: "))
    
    
    if cantidadRetiro <= 0:
        print("Error: La cantidad a retirar debe ser un número positivo.")
    elif cantidadRetiro > saldoDisponible: 
        print("Error, Digito un numero mayor a su saldo, intentelo de nuevo")
    else:
        nuevoSaldo = saldoDisponible - cantidadRetiro
        datos['saldo'] = nuevoSaldo     
    
        print(f"Esta es su cantidad de retiro: {cantidadRetiro}$ y aqui esta su saldo actulizado: {datos['saldo']}$")
        guardar_datos(datos)
        
def consultarSaldo():
    datos = cargar_datos()
    
    input(f"Su saldo es {datos['saldo']}$") 
    
#def consultarMovimientos(): no lo hice por falta de tiempo, perdon :c