# pylint: disable=raise-missing-from
class ControladorAlimento:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def pedir_entero(self, mensaje):
        texto = self.vista.pedir(mensaje)
        try:
            return int(texto)
        except ValueError:
            raise ValueError("ingrese solo numeros enteros.")

    def pedir_decimal(self, mensaje):
        texto = self.vista.pedir(mensaje)
        try:
            return float(texto.replace(",", "."))
        except ValueError:
            raise ValueError("ingrese solo numeros, por ejemplo 1.25.")

    def ejecutar(self):
        opcion = ""
        while opcion != "4":
            opcion = self.vista.mostrar_menu()
            try:
                if opcion == "1":
                    marca = self.vista.pedir("Marca: ")
                    precio = self.pedir_decimal("Precio: ")
                    sacos = self.pedir_entero("Sacos: ")
                    alimento = self.modelo.registrar(marca, precio, sacos)
                    self.vista.mostrar_mensaje(f"Registrado con el codigo {alimento.codigo}.")
                elif opcion == "2":
                    self.vista.mostrar_tabla(self.modelo.obtener_todos())
                elif opcion == "3":
                    codigo = self.pedir_entero("Codigo: ")
                    cantidad = self.pedir_entero("Cantidad: ")
                    alimento = self.modelo.vender(codigo, cantidad)
                    self.vista.mostrar_mensaje(f"Listo. Quedan {alimento.sacos} sacos.")
                elif opcion == "4":
                    self.vista.mostrar_mensaje("Programa finalizado.")
                else:
                    self.vista.mostrar_mensaje("Opción no valida.")
            except ValueError as error:
                self.vista.mostrar_mensaje(f"Error: {error}")