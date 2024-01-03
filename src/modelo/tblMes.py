from sqlalchemy import Column, String
from .Declarative_Base import Base
from sqlalchemy.orm import relationship


class tblMes(Base):
    __tablename__ = 'tblMes'
    IDMes = Column(String(8), primary_key=True)
    mesNombre = Column(String(12), nullable=False)

    # Relación con tblDetalleMensualTrabajador
    detalles_mensuales = relationship('tblDetalleMensualTrabajador', back_populates='mes',
                                      cascade='all, delete, delete-orphan')

    # Relación con tblDetalleCalculoSueldo
    detalles_mensuales1 = relationship('tblDetalleCalculoSueldo', back_populates='mes1',
                                       cascade='all, delete, delete-orphan')
