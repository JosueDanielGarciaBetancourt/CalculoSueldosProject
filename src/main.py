# TODO: Implementar el funcionamiento de ventana FormInspeccionarTrabajador

# TODO: Implementar registro de detalle mensual en las tablas respectivas
# TODO: Implementar pago de sueldo en la tabla historial de pagos
# TODO: Generar PDF para el comprobante de pago


# TODO: Implementar justificaciones


# TODO: Implementar ordenamiento de tablas por ID y por Fechas


# TODO: Después de cada CRUD se debe actualizar la tabla de trabajadores GUI


# TODO: Testing

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
