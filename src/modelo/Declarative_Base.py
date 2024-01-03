from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
# engine = create_engine('sqlite:///D:\Cursos UC\Ciclo 7\Construcción de Software\PFC\Proyecto '
#                       'final\EvaluacionParcialSueldosSemana8\src\Sueldos_DBLite.sqlite')

engine = create_engine('sqlite:///Sueldos_DBLite.sqlite')

Session = sessionmaker(bind=engine)
Base = declarative_base()


def reiniciarDB():
    try:
        # Eliminar todas las tablas existentes
        Base.metadata.drop_all(engine)
        # Crear las tablas
        Base.metadata.create_all(engine)
        print("Base de datos reiniciada correctamente.")
    except Exception as e:
        print(f"Error al reiniciar la base de datos: {e}")

# if __name__ == "__main__":
#    reiniciarDB()
