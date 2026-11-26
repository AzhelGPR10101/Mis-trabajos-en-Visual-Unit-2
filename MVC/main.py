from MVC.vista import vista
from MVC.modelo import ListaAlimentos
from MVC.controlador import ControladorAlimento

modelo = ListaAlimentos()
vista = vista()
controlador = ControladorAlimento(modelo, vista)
controlador.ejecutar()