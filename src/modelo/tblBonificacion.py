from sqlalchemy import Column, Float, String
from .Declarative_Base import Base  # si no funciona es pq falta un punto delante de delcarative xd
from sqlalchemy.orm import relationship


class tblBonificacion(Base):
    __tablename__ = 'tblBonificacion'
    IDBonificacion = Column(String(8), primary_key=True)
    bonTipo = Column(String(40), nullable=False)
    #bonUnidad = Column(String(10), nullable)
    bonValor = Column(Float, nullable=False)

    # Relación con tblDetalleBonificación
    detalles_bonificaciones = relationship('tblDetalleBonificacion', back_populates='bonificacion',
                                           cascade='all, delete, delete-orphan')