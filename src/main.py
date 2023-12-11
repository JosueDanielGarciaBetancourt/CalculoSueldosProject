#TODO: Mejorar la ventana BUSCAR TRABAJADOR, debe haber un botón para buscar y otro para seleccionar que se habilita según se seleccione un trabajador
from logica.EjemploOperacionesDB import EjemploOperacionesDB
from modelo.Declarative_Base import reiniciarDB
from vista.GestorSueldos import GestorSueldos
from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication([])  # Inicializando aplicación
    
    reiniciarDB()
    EjemploOperacionesDB()

    print("\nEjecutando app...")
    App = GestorSueldos(app)
