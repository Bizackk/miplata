import json

class GestorCuenta:
    def __init__(self):
        self.datos = self.cargar_datos()

    def cargar_datos(self):
        try:
            with open('datos.json', 'r') as file:
                datos = json.load(file)
                if 'movimientos' not in datos:
                    datos['movimientos'] = [] 
        except (FileNotFoundError, json.JSONDecodeError):
            datos = {'saldo': 0, 'movimientos': []}
        return datos

    def guardar_datos(self):
        with open('datos.json', 'w') as file:
            json.dump(self.datos, file, indent=4)

    def consignar(self):
        saldo = self.datos['saldo']
        try:
            cuanto = int(input("Cuánto dinero depositará: "))
            if cuanto <= 0:
                print("Error: La cantidad a depositar debe ser un número positivo.")
                return
        except ValueError:
            print("Error: Debe ingresar un número válido.")
            return

        nuevoSaldo = saldo + cuanto
        self.datos['saldo'] = nuevoSaldo
        self.datos['movimientos'].append({'tipo': 'Consignación', 'monto': cuanto})
        self.guardar_datos()
        print(f"Has depositado la cantidad de {cuanto}$ y tu saldo ahora es de {self.datos['saldo']}$")

    def retirar(self):
        saldoDisponible = self.datos['saldo']
        try:
            cantidadRetiro = int(input("Cuánto va a retirar: "))
            if cantidadRetiro <= 0:
                print("Error: La cantidad a retirar debe ser un número positivo.")
                return
        except ValueError:
            print("Error: Debe ingresar un número válido.")
            return

        if cantidadRetiro > saldoDisponible:
            print("Error: Ha digitado un número mayor a su saldo, inténtelo de nuevo.")
        else:
            nuevoSaldo = saldoDisponible - cantidadRetiro
            self.datos['saldo'] = nuevoSaldo
            self.datos['movimientos'].append({'tipo': 'Retiro', 'monto': cantidadRetiro})
            self.guardar_datos()
            print(f"Esta es su cantidad de retiro: {cantidadRetiro}$ y aquí está su saldo actualizado: {self.datos['saldo']}$")

    def consultar_saldo(self):
        print(f"Su saldo es {self.datos['saldo']}$")

    def consultar_movimientos(self):
        movimientos = self.datos.get('movimientos', [])
        if movimientos:
            print("Movimientos:")
            for movimiento in movimientos:
                print(f"{movimiento['tipo']}: {movimiento['monto']}$")
        else:
            print("No hay movimientos registrados.")

class ConsultorObjetos:
    @staticmethod
    def consultar(detalle, objeto):
        if detalle == 'saldo':
            return objeto.datos['saldo']
        else:
            return "Detalle no válido"

if __name__ == "__main__":
    gestor = GestorCuenta()
    while True:
        print("\nOpciones: 1) Consignar 2) Retirar 3) Consultar saldo 4) Consultar movimientos 5) Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            gestor.consignar()
        elif opcion == '2':
            gestor.retirar()
        elif opcion == '3':
            gestor.consultar_saldo()
        elif opcion == '4':
            gestor.consultar_movimientos()
        elif opcion == '5':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida, inténtelo de nuevo.")
