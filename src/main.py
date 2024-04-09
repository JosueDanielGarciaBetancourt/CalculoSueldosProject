# TODO: Hacer que aparezca el registro de historial de pagos en la fila correcta
# guardar el registro de boleta de pago en la BD con el mes simulado y no con el mes real

# TODO: Implementar ordenamiento de tablas por ID y por Fechas

# TODO: Implementar justificaciones

# TODO: Después de cada CRUD se debe actualizar la tabla de trabajadores GUI

# TODO: Testing

from src.modelo.Declarative_Base import reiniciarDB
from src.logica.EjemploOperacionesDB import EjemploOperacionesDB
from src.vista.GestorSueldos import GestorSueldos
from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication([])  # Inicializando aplicación
    
    reiniciarDB()
    EjemploOperacionesDB()

    print("\nEjecutando app...")
    App = GestorSueldos(app)
