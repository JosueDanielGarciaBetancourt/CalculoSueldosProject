from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from .Declarative_Base import Base  # si no funciona es pq falta un punto delante de declarative xd
from datetime import datetime
from sqlalchemy.orm import relationship


class tblDetalleMensualTrabajador(Base):
    __tablename__ = 'tblDetalleMensualTrabajador'
    IDTrabajador = Column(String(8), ForeignKey('tblTrabajador.IDTrabajador'), primary_key=True)
    IDMes = Column(String(8), ForeignKey('tblMes.IDMes'), primary_key=True)
    IDDetalleCalculoSueldo = Column(String(15), ForeignKey('tblDetalleCalculoSueldo.IDDetalleCalculoSueldo'), primary_key=True)
    detalleAnio = Column(String(4), nullable=False, default=str(datetime.now().year))  # Año actual
    detalleHorasExtras = Column(Integer, nullable=False)
    detalleMinutosTardanzas = Column(Integer, nullable=False)
    detalleMinutosJustificados = Column(Integer, nullable=False)
    detalleDiasFalta = Column(Integer, nullable=False)
    detalleDiasJustificados = Column(Integer, nullable=False)
    detalleSueldoNeto = Column(Float, nullable=False)
    detalleFecha = Column(DateTime(), default=datetime.now)  # YYYY-MM-DD hh-mm-ss

    # Relación inversa con tblTrabajador
    trabajador = relationship('tblTrabajador', back_populates='detalles_mensuales')

    # Relación inversa con tblMes
    mes = relationship('tblMes', back_populates='detalles_mensuales')

    # Relación con tblDetalleCalculoSueldo
    detalleCalculoSueldo = relationship('tblDetalleCalculoSueldo', back_populates='detalleMensualTrabajador')


"""
Usando tabla MES se puede generar una especie de clave primaria compuesta por IDTrabajador,
IDMes y DetalleAnio 

| IDTrabajador | IDMes | DetalleAnio | HorasExtra | MinTardanzas | MinJustificados | DiasFalta | DiasJustificados | SueldoNeto |
|--------------|-------|-------------|------------|--------------|-----------------|-----------|------------------|------------|
| 001          | 01    | 2023        | 10         | 30           | 15              | 2         | 1                | 3100.0     |
| 001          | 02    | 2023        | 15         | 20           | 10              | 1         | 0                | 3200.0     |
| 001          | 03    | 2023        | 5          | 25           | 20              | 3         | 2                | 3000.0     |
| 001          | 01    | 2024        | 8          | 15           | 5               | 0         | 0                | 3300.0     |
| 001          | 02    | 2024        | 12         | 10           | 8               | 2         | 1                | 3150.0     |
| 001          | 03    | 2024        | 7          | 30           | 15              | 1         | 0                | 3100.0     |
"""
