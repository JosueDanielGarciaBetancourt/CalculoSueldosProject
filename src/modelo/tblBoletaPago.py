from sqlalchemy import Column, Float, String, Date, Time, ForeignKey, func
from .Declarative_Base import Base
from sqlalchemy.orm import relationship


class tblBoletaPago(Base):
    __tablename__ = 'tblBoletaPago'
    IDBoletaPago = Column(String(8), primary_key=True)
    IDTrabajador = Column(String(8), ForeignKey('tblTrabajador.IDTrabajador'))
    bolSueldoNeto = Column(String(150), nullable=False)
    bolDescuentoTotal = Column(Float, nullable=False)
    bolBonificacionTotal = Column(Float, nullable=False)
    bolFechaEmision = Column(Date, default=func.current_date())  # YYYY-MM-DD
    bolHoraEmision = Column(Time, default=func.current_time())  # hh-mm-ss

    # Relación con tblDetalleBonificación
    detalles_bonificaciones = relationship('tblDetalleBonificacion', back_populates='boleta_pago',
                               cascade='all, delete, delete-orphan')

    # Relación inversa con tblTrabajador
    trabajador = relationship('tblTrabajador', back_populates='boleta_pago')

