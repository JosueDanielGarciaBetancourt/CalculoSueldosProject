from sqlalchemy import Column, Float, String, ForeignKey
from .Declarative_Base import Base
from sqlalchemy.orm import relationship


class tblDetalleCalculoSueldo(Base):
    __tablename__ = 'tblDetalleCalculoSueldo'
    IDTrabajador = Column(String(8), ForeignKey('tblTrabajador.IDTrabajador'), primary_key=True)
    IDMes = Column(String(8), ForeignKey('tblMes.IDMes'), primary_key=True)
    IDDetalleCalculoSueldo = Column(String(15), primary_key=True)
    calcSueldoMontoMovilidad = Column(Float, nullable=False)
    calcSueldoMontoSuplementario = Column(Float, nullable=False)
    calcSueldoMontoHorasExtras = Column(Float, nullable=False)
    calcSueldoMontoRemunComputable = Column(Float, nullable=False)
    calcSueldoMontoDctoFalta = Column(Float, nullable=False)
    calcSueldoMontoDctoTardanzas = Column(Float, nullable=False)
    calcSueldoTotalBonificaciones = Column(Float, nullable=False)
    calcSueldoTotalDctos = Column(Float, nullable=False)

    # Relación inversa con tblTrabajador
    trabajador1 = relationship('tblTrabajador', back_populates='detalleCalculoSueldo')

    # Relación inversa con tblMes
    mes1 = relationship('tblMes', back_populates='detalles_mensuales1')

    detalleMensualTrabajador = relationship('tblDetalleMensualTrabajador', back_populates='detalleCalculoSueldo')
