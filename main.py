from sistema_logueado.registrar import registrarUsuarios , imprimir_informacion_personal 
from sistema_logueado.inisiarSesion import inisioSesion 
from banco.banco import *
import json

continuar = True

while continuar:
    
    print("Bienvenida a Mi PLata, espero se enctuentre muy bien. Si ya tiene una cuenta, inicie sesion, si no tiene cree una cuenta.")
    crear_iniciar = input("Que desea iniciar sesion o crear cuenta? (i/c): ")
    print("-------------")
    
    if crear_iniciar.lower() == "c":
        registrarUsuarios()
        input("has creado una cuenta correctamente")
        print("-------------")
    elif crear_iniciar.lower() == "i":
        while True:  
            if inisioSesion():  
                break  
            else:
                print("Usuario o contraseña incorrecto, intenta de nuevo.")
                print("-------------")
    
    
    while True:
        print("-------------")
        print(f"Muy bien. Ahora puedes tener el gusto de manejar tu dinero comodamente con Mi Plata!!")
        print("-------------")
        print("Opciones para hacer:")
        print("1. ¿Consultar saldo?")
        print("2. ¿Consignar?")
        print("3. ¿Retirar?")
        print("4. ¿Consultar movimientos?")
        print("5. Por hoy estoy bien")
        print("6. Tenemos una seccion que te imprime tus datos, esto fue una adicion de la pagina y futuramente podras actualizar tus datos")
        print("-------------")
        
    
        hacer = input("Digite el numero que corresponde la accion (1,2,3,4,5,6): ")
        print("-------------")
    
  
        if hacer == "1":
            consultarSaldo()
        elif hacer == "2":
            consignar()
        elif hacer == "3":
            retirar()
        elif hacer == "5":
            continuar = False
            break
        elif hacer == "6":
            imprimir_informacion_personal()