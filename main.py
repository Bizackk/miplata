from sistema_logueado.registrar import registrarUsuarios, imprimir_informacion_personal
from sistema_logueado.inisiarSesion import inisioSesion
from banco.banco import GestorCuenta, ConsultorObjetos

import json

def main():
    continuar = True
    gestor = GestorCuenta()

    while continuar:
        print("Bienvenido a Mi Plata, espero se encuentre muy bien. Si ya tiene una cuenta, inicie sesión, si no tiene, cree una cuenta.")
        crear_iniciar = input("¿Qué desea hacer, iniciar sesión o crear una cuenta? (i/c): ").lower()
        print("-------------")

        if crear_iniciar == "c":
            registrarUsuarios()
            input("Has creado una cuenta correctamente. Presiona Enter para continuar.")
            print("-------------")
        elif crear_iniciar == "i":
            while True:
                if inisioSesion():
                    break
                else:
                    print("Usuario o contraseña incorrecto, intenta de nuevo.")
                    print("-------------")

        while True:
            print("-------------")
            print("Muy bien. Ahora puedes manejar tu dinero cómodamente con Mi Plata.")
            print("-------------")
            print("Opciones disponibles:")
            print("1. Consultar saldo")
            print("2. Consignar")
            print("3. Retirar")
            print("4. Consultar movimientos")
            print("5. Por hoy estoy bien")
            print("6. Imprimir información personal")
            print("-------------")

            hacer = input("Digite el número correspondiente a la acción (1, 2, 3, 4, 5, 6): ")
            print("-------------")

            if hacer == "1":
                print("Su saldo es:", ConsultorObjetos.consultar('saldo', gestor))
            elif hacer == "2":
                gestor.consignar()
            elif hacer == "3":
                gestor.retirar()
            elif hacer == "4":
                gestor.consultar_movimientos()
            elif hacer == "5":
                continuar = False
                break
            elif hacer == "6":
                imprimir_informacion_personal()
            else:
                print("Opción no válida, inténtelo de nuevo.")
                print("-------------")

if __name__ == "__main__":
    main()
