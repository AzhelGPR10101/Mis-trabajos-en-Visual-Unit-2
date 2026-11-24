class vista:
    def mostrar_menu(self):
        print()
        print("MENÚ")
        print("1. Registrar alimento")
        print("2. Mostrar alimentos")
        print("3. Vender alimento")
        print("4. Salir")
        return input("Seleccione una opción: ").strip()

    def pedir(self, mensaje):
        return input(mensaje)

    def mostrar_tabla(self, lista):
        print("Código  Marca                   Precio            Sacos")
        for a in lista:
            print(f"{a.codigo:<8}{a.marca:<24}{a.precio:<18.2f}{a.sacos:<14}{a.descripcion:<14}")

    def mostrar_mensaje(self, mensaje):
        print(mensaje)