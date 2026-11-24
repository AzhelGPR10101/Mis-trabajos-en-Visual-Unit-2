class Alimento:
    def __init__(self, codigo, marca, precio, sacos, descripcion):
        self.codigo = codigo
        self.marca = marca
        self.precio = precio
        self.sacos = sacos
        self.descripcion = descripcion

    def vender(self, cantidad):
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor que cero.")
            return False
        if cantidad > self.sacos:
            print(f"Error: solo hay {self.sacos} sacos.")
            return False
        self.sacos -= cantidad
        return True

    def __str__(self):
        return f"{self.codigo:<8}{self.marca:<24}{self.precio:<18.2f}{self.sacos:<14}{self.descripcion:<14}"


class ListaAlimentos:
    def __init__(self):
        self.lista = []
        self.siguiente_codigo = 1

    def agregar(self, marca, precio, sacos, descripcion):
        alimento = Alimento(self.siguiente_codigo, marca, precio, sacos, descripcion)
        self.lista.append(alimento)
        self.siguiente_codigo += 1
        return alimento

    def obtener_todos(self):
        return self.lista

    def buscar(self, codigo):
        for elemento in self.lista:
            if elemento.codigo == codigo:
                return elemento
        return None

    def actualizar_precio(self, codigo, precio):
        elemento = self.buscar(codigo)
        if elemento is None:
            return False
        elemento.precio = precio
        return True

    def eliminar(self, codigo):
        elemento = self.buscar(codigo)
        if elemento is None:
            return False
        self.lista.remove(elemento)
        return True