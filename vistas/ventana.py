import sys # pylint: disable=no-name-in-module
from PyQt6.QtWidgets import QApplication, QMainWindow # pylint: disable=no-name-in-module

app = QApplication(sys.argv) 
ventana = QMainWindow()
ventana.setWindowTitle("Cooperativa")
ventana.resize(800, 500)
ventana.show()
sys.exit(app.exec()) 