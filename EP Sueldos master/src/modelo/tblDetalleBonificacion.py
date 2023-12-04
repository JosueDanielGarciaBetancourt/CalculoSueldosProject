from sqlalchemy import Column, Float, String, ForeignKey
from .Declarative_Base import Base  # si no funciona es pq falta un punto delante de declarative xd
from sqlalchemy.orm import relationship


class tblDetalleBonificacion(Base):
    __tablename__ = 'tblDetalleBonificacion'
    IDBonificacion = Column(String(8), ForeignKey('tblBonificacion.IDBonificacion'), primary_key=True)
    IDBoletaPago = Column(String(8), ForeignKey('tblBoletaPago.IDBoletaPago'), primary_key=True)
    detbonMontoTotalPorBonificacion = Column(Float, primary_key=True)

    # Relación inversa con tblBoletaPago
    boleta_pago = relationship('tblBoletaPago', back_populates='detalles_bonificaciones')

    # Relación inversa con tblBonificacion
    bonificacion = relationship('tblBonificacion', back_populates='detalles_bonificaciones')
