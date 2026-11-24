class Alimento:
    def __init__(self, codigo, marca, precio, sacos, descripcion=""):
        self.codigo = codigo
        self.marca = marca
        self.precio = precio
        self.sacos = sacos
        self.descripcion = descripcion
        self.validar()

    def validar(self):
        self.marca = str(self.marca).strip()
        if self.marca == "":
            raise ValueError("el campo no puede estar vacio.")
        try:
            self.precio = float(str(self.precio).replace(",", "."))
        except ValueError as exc:
            raise ValueError("ingrese solo numeros, por ejemplo 1.25.") from exc
        if self.precio <= 0 or self.precio > 1000000:
            raise ValueError("el valor debe ser mayor que cero.")
        try:
            self.sacos = int(self.sacos)
        except ValueError as exc:
            raise ValueError("ingrese solo numeros enteros.") from exc
        if self.sacos < 0:
            raise ValueError("el valor debe ser mayor o igual a 0.")

    def vender(self, cantidad):
        try:
            cantidad = int(cantidad)
        except ValueError as exc:
            raise ValueError("ingrese solo numeros enteros.") from exc
        if cantidad <= 0:
            raise ValueError("la cantidad debe ser mayor que cero.")
        if cantidad > self.sacos:
            raise ValueError(f"solo hay {self.sacos} sacos.")
        self.sacos -= cantidad


class ListaAlimentos:
    def __init__(self):
        self.lista = []

    def registrar(self, marca, precio, sacos):
        alimento = Alimento(len(self.lista) + 1, marca, precio, sacos)
        self.lista.append(alimento)
        return alimento

    def buscar(self, codigo):
        try:
            codigo = int(codigo)
        except ValueError as exc:
            raise ValueError("ingrese solo numeros enteros.") from exc
        for elemento in self.lista:
            if elemento.codigo == codigo:
                return elemento
        raise ValueError("no existe ese codigo.")

    def vender(self, codigo, cantidad):
        alimento = self.buscar(codigo)
        alimento.vender(cantidad)
        return alimento

    def obtener_todos(self):
        return self.lista