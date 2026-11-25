class vista:
    def mostrar_menu(self):
        print()
        print("MENÚ")
        print("1. Registrar alimento")
        print("2. Mostrar alimentos")
        print("3. Vender alimento")
        print("4. Salir")
        return input("Seleccione una opción: ").strip()

#metodo para ingresar el texto
    def pedir(self, mensaje):
        return input(mensaje)
#metodo para mostrar la tabla con el formato que esta e modelo
    def mostrar_tabla(self, lista):
        print("Código  Marca                   Precio            Sacos")
        for elemento in lista:
            print(elemento)

#metodo que muestras los mensajes que genera el controlador
    def mostrar_mensaje(self, mensaje):
        print(mensaje)