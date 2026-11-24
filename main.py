from modelo import ListaAlimentos
from vista import vista
from controlador import Controlador

modelo = ListaAlimentos()
vista = vista()
controlador = Controlador(modelo, vista)
controlador.iniciar()