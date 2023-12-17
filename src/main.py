# TODO: Implementar la ventana inspeccionar trabajador, tabla de doble entrada con los meses y que se filtre por años
# TODO: Implementar ordenamiento de tablas por ID y por Fechas
# TODO: Después de cada CRUD se debe actualizar la tabla de trabajadores GUI
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
