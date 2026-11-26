from persona import persona

class docente(persona):

    def __init__(self, nombre, apellido, cedula, celular, correo, edad, direccion, asignatura, horas, salario, valor):
        super().__init__(nombre, apellido, cedula, celular, correo, edad, direccion)

        self.asignatura =asignatura
        self.horas = horas
        self.salario = 0
        self.valor = 20

    def calcular_salario(self):
        self.salario = self.horas * self.valor

    def __str__(self):
        return f"{super().__str__()} asignatura: {self.asignatura} salario: {self.salario}"

def validar_edad(self):
    return f"{super().validar_edad()} asignatura: {self.asignatura}"