from datetime import datetime

class Pedido:
    def __init__(self, numero, codigo_plato, mesa, cantidad, total, fecha=None, estado="activo"):
        self.numero = numero
        self.codigo_plato = codigo_plato
        self.mesa = mesa
        self.cantidad = cantidad
        self.total = total
        self.fecha = fecha if fecha is not None else datetime.now().strftime("%Y-%m-%d %H:%M")
        self.estado = estado
        self.validar()

    def validar(self):
        if self.mesa < 1 or self.mesa > 20:
            raise ValueError("Error: la mesa debe estar entre 1 y 20.")
        if self.cantidad <= 0:
            raise ValueError("Error: la cantidad debe ser mayor que 0.")

    def anular(self):
        if self.estado != "activo":
            raise ValueError("Error: el pedido ya está anulado.")
        self.estado = "anulado"

    def a_linea(self):
        return f"{self.numero},{self.codigo_plato},{self.mesa},{self.cantidad},{self.total},{self.fecha},{self.estado}\n"

    def __str__(self):
        return (
            f"{self.numero:<8} {self.codigo_plato:<8} {self.mesa:<6} "
            f"{self.cantidad:<10} ${self.total:>7.2f}  {self.fecha:<17} {self.estado:<10}"
        )