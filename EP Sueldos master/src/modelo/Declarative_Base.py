from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///Sueldos_DBLite.sqlite')
Session = sessionmaker(bind=engine)
Base = declarative_base()

def reiniciarDB():
    # Eliminar todas las tablas existentes
    Base.metadata.drop_all(engine)
    # Crear las tablas
    Base.metadata.create_all(engine)


