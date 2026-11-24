class Alimento:
    def __init__(self, codigo, marca, precio, sacos, descripcion=""):
        self.codigo = codigo
        self.marca = marca
        self.precio = precio
        self.sacos = sacos
        self.descripcion = descripcion
        self.validar()

    def validar(self):
        self.marca = self.marca.strip()
        if self.marca == "":
            raise ValueError("el campo no puede estar vacio.")
        if self.precio <= 0 or self.precio > 1000000:
            raise ValueError("el valor debe ser mayor que cero.")
        if self.sacos < 0:
            raise ValueError("el valor debe ser mayor o igual a 0.")

    def vender(self, cantidad):
        if cantidad <= 0:
            raise ValueError("la cantidad debe ser mayor que cero.")
        if cantidad > self.sacos:
            raise ValueError(f"solo hay {self.sacos} sacos.")
        self.sacos -= cantidad

    def __str__(self):
        return f"{self.codigo:<8}{self.marca:<24}{self.precio:<18.2f}{self.sacos:<14}{self.descripcion:<14}"


class ListaAlimentos:
    def __init__(self):
        self.lista = []
        self.siguiente_codigo = 1
        self.registrar("ProCan", 28.00, 15)
        self.registrar("Whiskas", 22.00, 10)

    def registrar(self, marca, precio, sacos):
        alimento = Alimento(self.siguiente_codigo, marca, precio, sacos)
        self.lista.append(alimento)
        self.siguiente_codigo += 1
        return alimento

    def buscar(self, codigo):
        for elemento in self.lista:
            if elemento.codigo == codigo:
                return elemento
        raise ValueError("no existe ese codigo.")

    def vender(self, codigo, cantidad):
        alimento = self.buscar(codigo)
        alimento.vender(cantidad)
        return alimento

    def eliminar(self, codigo):
        alimento = self.buscar(codigo)
        self.lista.remove(alimento)
        return alimento

    def obtener_todos(self):
        return self.lista