from logica.EjemploOperacionesDB import EjemploOperacionesDB
from modelo.Declarative_Base import reiniciarDB
from vista.GestorSueldos import GestorSueldos

if __name__ == '__main__':

    # Borrar tablas y crear nuevamente
    reiniciarDB()
    EjemploOperacionesDB()

    print("\nEjecutando app...")

    # Ejecutar App
    App = GestorSueldos()
