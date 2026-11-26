class Plato:
    def __init__(self, codigo, nombre, precio, porciones):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.porciones = porciones
        self.validar()

    def validar(self):
        self.nombre = self.nombre.strip()
        if self.nombre == "":
            raise ValueError("Error: el nombre del plato no puede estar vacío.")
        if "," in self.nombre:
            raise ValueError("Error: el nombre del plato no puede contener comas.")
        if self.precio <= 0:
            raise ValueError("Error: el precio debe ser mayor que 0.")
        if self.porciones < 0:
            raise ValueError("Error: las porciones deben ser mayores o iguales a 0.")

    def descontar_porciones(self, cantidad):
        if cantidad <= 0:
            raise ValueError("Error: la cantidad debe ser mayor que 0.")
        if cantidad > self.porciones:
            raise ValueError(f"Error: solo hay {self.porciones} porciones disponibles.")
        self.porciones -= cantidad

    def devolver_porciones(self, cantidad):
        self.porciones += cantidad

    def a_linea(self):
        return f"{self.codigo},{self.nombre},{self.precio},{self.porciones}\n"

    def __str__(self):
        return f"{self.codigo:<8} {self.nombre:<22} ${self.precio:>7.2f} {self.porciones:>10}"