class Restaurante:
    def __init__(self, archivo_platos="platos.txt", archivo_pedidos="pedidos.txt"):
        self.archivo_platos = archivo_platos
        self.archivo_pedidos = archivo_pedidos
        self.platos = []
        self.pedidos = []
        self.siguiente_codigo = 1
        self.siguiente_numero = 1
        self.cargar()

    def cargar(self):
        if os.path.exists(self.archivo_platos):
            with open(self.archivo_platos, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        codigo, nombre, precio, porciones = linea.split(",")
                        plato = Plato(int(codigo), nombre, float(precio), int(porciones))
                        self.platos.append(plato)
            if self.platos:
                self.siguiente_codigo = max(p.codigo for p in self.platos) + 1
        else:
            self.registrar_plato("Almuerzo ejecutivo", 3.50, 40)
            self.registrar_plato("Mote pillo", 2.75, 20)
            self.registrar_plato("Cuy asado", 15.00, 6)

        if os.path.exists(self.archivo_pedidos):
            with open(self.archivo_pedidos, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        numero, codigo_plato, mesa, cantidad, total, fecha, estado = linea.split(",")
                        pedido = Pedido(
                            int(numero),
                            int(codigo_plato),
                            int(mesa),
                            int(cantidad),
                            float(total),
                            fecha,
                            estado,
                        )
                        self.pedidos.append(pedido)
            if self.pedidos:
                self.siguiente_numero = max(p.numero for p in self.pedidos) + 1

    def guardar(self):
        with open(self.archivo_platos, "w", encoding="utf-8") as archivo:
            for plato in self.platos:
                archivo.write(plato.a_linea())

        with open(self.archivo_pedidos, "w", encoding="utf-8") as archivo:
            for pedido in self.pedidos:
                archivo.write(pedido.a_linea())

    def registrar_plato(self, nombre, precio, porciones):
        nuevo_plato = Plato(self.siguiente_codigo, nombre, precio, porciones)
        self.platos.append(nuevo_plato)
        self.siguiente_codigo += 1
        return nuevo_plato

    def buscar_por_codigo(self, codigo):
        for plato in self.platos:
            if plato.codigo == codigo:
                return plato
        raise ValueError("Error: no existe ese código.")

    def buscar(self, texto):
        texto = texto.strip().lower()
        if texto == "":
            raise ValueError("Error: debe ingresar un nombre para buscar.")
        return [p for p in self.platos if texto in p.nombre.lower()]

    def registrar_pedido(self, codigo_plato, mesa, cantidad):
        plato = self.buscar_por_codigo(codigo_plato)
        total = plato.precio * cantidad
        nuevo_pedido = Pedido(self.siguiente_numero, plato.codigo, mesa, cantidad, total)
        plato.descontar_porciones(cantidad)
        self.pedidos.append(nuevo_pedido)
        self.siguiente_numero += 1
        return nuevo_pedido, plato

    def buscar_pedido(self, numero):
        for pedido in self.pedidos:
            if pedido.numero == numero:
                return pedido
        raise ValueError("Error: no existe ese número de pedido.")

    def anular(self, numero):
        pedido = self.buscar_pedido(numero)
        pedido.anular()
        plato = self.buscar_por_codigo(pedido.codigo_plato)
        plato.devolver_porciones(pedido.cantidad)
        return pedido, plato

    def reporte(self):
        return {
            "total_platos": len(self.platos),
            "porciones_disponibles": sum(p.porciones for p in self.platos),
            "pedidos_activos": sum(1 for p in self.pedidos if p.estado == "activo"),
            "pedidos_anulados": sum(1 for p in self.pedidos if p.estado == "anulado"),
            "total_vendido": sum(p.total for p in self.pedidos if p.estado == "activo"),
            "bajo_stock": [p for p in self.platos if p.porciones < 5],
        }

    def obtener_platos(self):
        return self.platos

    def obtener_pedidos(self):
        return self.pedidos