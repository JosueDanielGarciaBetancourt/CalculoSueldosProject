from sqlalchemy import Column, String, Float, DateTime, ForeignKey, Integer, Date, Time, func
from datetime import datetime
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
    detalles_calculo_sueldo = relationship('tblDetalleCalculoSueldo', back_populates='mes1',
                                           cascade='all, delete, delete-orphan')


class tblBonificacion(Base):
    __tablename__ = 'tblBonificacion'
    IDBonificacion = Column(String(8), primary_key=True)
    bonTipo = Column(String(40), nullable=False)
    bonUnidad = Column(String(10), nullable=False)
    bonValor = Column(Float, nullable=False)

    # Relación con tblDetalleBonificación
    detalles_bonificaciones = relationship('tblDetalleBonificacion', back_populates='bonificacion',
                                           cascade='all, delete, delete-orphan')


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
    mes1 = relationship('tblMes', back_populates='detalles_calculo_sueldo')

    detalleMensualTrabajador = relationship('tblDetalleMensualTrabajador', back_populates='detalleCalculoSueldo')


@staticmethod
def obtenerFechaAhora():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class tblDetalleMensualTrabajador(Base):
    __tablename__ = 'tblDetalleMensualTrabajador'
    IDTrabajador = Column(String(8), ForeignKey('tblTrabajador.IDTrabajador'), primary_key=True)
    IDMes = Column(String(8), ForeignKey('tblMes.IDMes'), primary_key=True)
    IDDetalleCalculoSueldo = Column(String(15), ForeignKey('tblDetalleCalculoSueldo.IDDetalleCalculoSueldo'),
                                    primary_key=True)
    detalleAnio = Column(String(4), nullable=False, default=str(datetime.now().year))  # Año actual
    detalleHorasExtras = Column(Integer, nullable=False)
    detalleMinutosTardanzas = Column(Integer, nullable=False)
    detalleMinutosJustificados = Column(Integer, nullable=False)
    detalleDiasFalta = Column(Integer, nullable=False)
    detalleDiasJustificados = Column(Integer, nullable=False)
    detalleSueldoNeto = Column(Float, nullable=False)
    detalleFechaFormateada = Column(String(19), default=obtenerFechaAhora())  # YYYY-MM-DD hh-mm-ss
    detalleFecha = Column(DateTime(), default=datetime.now)  # YYYY-MM-DD hh-mm-ss-ms

    # Relación inversa con tblTrabajador
    trabajador = relationship('tblTrabajador', back_populates='detalles_mensuales')

    # Relación inversa con tblMes
    mes = relationship('tblMes', back_populates='detalles_mensuales')

    # Relación con tblDetalleCalculoSueldo
    detalleCalculoSueldo = relationship('tblDetalleCalculoSueldo', back_populates='detalleMensualTrabajador')


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


class tblDetalleBonificacion(Base):
    __tablename__ = 'tblDetalleBonificacion'
    IDBonificacion = Column(String(8), ForeignKey('tblBonificacion.IDBonificacion'), primary_key=True)
    IDBoletaPago = Column(String(8), ForeignKey('tblBoletaPago.IDBoletaPago'), primary_key=True)
    detbonMontoTotalPorBonificacion = Column(Float, primary_key=True)

    # Relación inversa con tblBoletaPago
    boleta_pago = relationship('tblBoletaPago', back_populates='detalles_bonificaciones')

    # Relación inversa con tblBonificacion
    bonificacion = relationship('tblBonificacion', back_populates='detalles_bonificaciones')
