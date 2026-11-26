from estudiante import estudiante
from docente import docente

estudiantes = [
    estudiante("Gerard", "Perez", "0303156897", "097654321", "gerardprez@gmail.com", 21, "Av.Siempre Viva 123", "TDSU", [9,7,8,8,7]),
    estudiante("María", "González", "0104567891", "0991234567", "mariagonzalez@gmail.com", 19, "Av. Loja y Remigio Crespo", "TDSU", [8,9,10,8,9]),
    estudiante("Carlos", "Mendoza", "0105678912", "0987654321", "carlosmendoza@gmail.com", 22, "Calle Bolívar 456", "TDSU", [7,8,9,8,7]),
    estudiante("Andrea", "Ramírez", "0106789123", "0961234567", "andrearamirez@gmail.com", 20, "Av. Don Bosco 789", "TDSU", [10,9,8,10,9]),
    estudiante("Luis", "Cárdenas", "0107891234", "0956781234", "luiscardenas@gmail.com", 18, "Calle Larga y Huayna Cápac", "TDSU", [6,8,7,9,8]),
]

docentes = [
    docente("Andrés", "Molina", "0102345678", "0994561230", "andres.molina@gmail.com", 35, "Av. Solano 123", "Programación", 40, 0, 20),
    docente("Patricia", "Vásquez", "0103456789", "0985672341", "patricia.v@gmail.com", 42, "Calle Larga 456", "Base de Datos", 32, 0, 20),
    docente("Roberto", "Cárdenas", "0104567891", "0976783452", "roberto.cardenas@gmail.com", 29, "Av. Remigio Crespo 789", "Matemáticas", 25, 0, 20),
    docente("Daniela", "Ortega", "0105678912", "0967894563", "daniela.ortega@gmail.com", 38, "Calle Bolívar 321", "POO", 36, 0, 20),
    docente("Miguel", "Serrano", "0106789123", "0958905674", "miguel.serrano@gmail.com", 50, "Av. de las Américas 654", "Redes", 20, 0, 20),
]

for e in estudiantes:
    print(e.promedio())
    print(e.validar_edad())
    print(e)

for d in docentes:
    d.calcular_salario()
    print(d.validar_edad())
    print(d)