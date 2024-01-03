from datetime import datetime
from sqlalchemy import Column, Float, String, DateTime
from .Declarative_Base import Base
from sqlalchemy.orm import relationship


class tblTrabajador(Base):
    __tablename__ = 'tblTrabajador'
    IDTrabajador = Column(String(8), primary_key=True)
    trabNombreApellidos = Column(String(50), nullable=False)
    trabCargo = Column(String(150), nullable=False)
    trabSueldoBase = Column(Float, nullable=False)
    created_at = Column(DateTime(), default=datetime.now)  # YYYY-MM-DD hh-mm-ss

    # Relación con tblDetalleMensualTrabajador
    detalles_mensuales = relationship('tblDetalleMensualTrabajador', back_populates='trabajador',
                                      cascade='all, delete, delete-orphan')

    # Relación con tblDetalleCalculoSueldo
    detalleCalculoSueldo = relationship('tblDetalleCalculoSueldo', back_populates='trabajador1',
                                        cascade='all, delete, delete-orphan')

    # Relación con tblBoletaPago
    boleta_pago = relationship('tblBoletaPago', back_populates='trabajador',
                               cascade='all, delete, delete-orphan')
