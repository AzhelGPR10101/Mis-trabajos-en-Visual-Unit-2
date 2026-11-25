from vista import vista
from modelo import ListaAlimentos
from controlador import ControladorAlimento

modelo = ListaAlimentos()
vista = vista()
controlador = ControladorAlimento(modelo, vista)
controlador.ejecutar()