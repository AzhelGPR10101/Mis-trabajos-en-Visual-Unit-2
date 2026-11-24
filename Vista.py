class Menu:
    def mostrar(self):
        print()
        print("MENÚ")
        print("1. Registrar alimento")
        print("2. Mostrar alimentos")
        print("3. Vender alimento")
        print("4. Actualizar precio")
        print("5. Eliminar alimento")
        print("6. Salir")
        return input("Seleccione una opción: ").strip()


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Error: el campo no puede estar vacio.")


def leer_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("Error: ingrese solo numeros enteros.")
            continue
        if minimo is not None and valor < minimo:
            print(f"Error: el valor debe ser mayor o igual a {minimo}.")
            continue
        return valor


def leer_decimal(mensaje):
    while True:
        try:
            valor = float(input(mensaje).replace(",", "."))
        except ValueError:
            print("Error: ingrese solo numeros, por ejemplo 1.25.")
            continue
        if valor <= 0 or valor > 1000000:
            print("Error: el valor debe ser mayor que cero.")
            continue
        return valor


def mostrar_alimentos(lista):
    print(f"{'Código':<8}{'Marca':<24}{'Precio':<18}{'Sacos':<14}{'Descripción'}")
    for elemento in lista:
        print(elemento)