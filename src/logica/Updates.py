from src.modelo.modeladoTablas import tblMes
from src.modelo.modeladoTablas import tblBonificacion
from src.modelo.modeladoTablas import tblTrabajador
from src.modelo.modeladoTablas import tblDetalleCalculoSueldo
from src.modelo.modeladoTablas import tblDetalleMensualTrabajador
from src.modelo.modeladoTablas import tblBoletaPago
from src.modelo.modeladoTablas import tblDetalleBonificacion
from modelo.Declarative_Base import Session
from sqlalchemy.exc import IntegrityError


class Updates:
    @staticmethod
    def updateSueldoBase(idTrabajador, nuevoSueldoBase):
        with Session() as session:
            try:
                trabajador = session.query(tblTrabajador).get(idTrabajador)
                if trabajador:
                    print(f"Actualizando sueldo base para el trabajador {idTrabajador}")
                    trabajador.trabSueldoBase = nuevoSueldoBase
                    session.merge(trabajador)
                    session.commit()
                    print(
                        f"Sueldo base actualizado exitosamente: {idTrabajador} - Nuevo Sueldo Base: {nuevoSueldoBase}")
                else:
                    print(f"No se encontró el trabajador con ID: {idTrabajador}")
            except IntegrityError as e:
                print(f"Error al actualizar sueldo base: {e}")
                session.rollback()

    @staticmethod
    def updateValorBonificacion(idBonificacion, nuevoValor):
        with Session() as session:
            try:
                bonificacion = session.query(tblBonificacion).get(idBonificacion)
                if bonificacion:
                    print(f"Actualizando valor de bonificación para {idBonificacion}")
                    bonificacion.bonValor = nuevoValor
                    session.merge(bonificacion)
                    session.commit()
                    print(
                        f"Valor de bonificación actualizado exitosamente: {idBonificacion} - Nuevo Valor: {nuevoValor}")
                else:
                    print(f"No se encontró la bonificación con ID: {idBonificacion}")
            except IntegrityError as e:
                print(f"Error al actualizar valor de bonificación: {e}")
                session.rollback()

    @staticmethod
    def updateDetalleCalculoSueldo(idTrabajador, idMes, idDetalleCalculoSueldo, montoMovilidad, montoSuplementario,
                                   montoHorasExtras, montoRemunComputable, montoDctoFalta, montoDctoTardanzas,
                                   totalBonificaciones, totalDctos):
        with Session() as session:
            try:
                detalleCalculoSueldo = session.query(tblDetalleCalculoSueldo).filter_by(
                    IDTrabajador=idTrabajador, IDMes=idMes).first()
                if detalleCalculoSueldo:

                    detalleCalculoSueldo.IDDetalleCalculoSueldo = idDetalleCalculoSueldo
                    detalleCalculoSueldo.calcSueldoMontoMovilidad = montoMovilidad
                    detalleCalculoSueldo.calcSueldoMontoSuplementario = montoSuplementario
                    detalleCalculoSueldo.calcSueldoMontoHorasExtras = montoHorasExtras
                    detalleCalculoSueldo.calcSueldoMontoRemunComputable = montoRemunComputable
                    detalleCalculoSueldo.calcSueldoMontoDctoFalta = montoDctoFalta
                    detalleCalculoSueldo.calcSueldoMontoDctoTardanzas = montoDctoTardanzas
                    detalleCalculoSueldo.calcSueldoTotalBonificaciones = totalBonificaciones
                    detalleCalculoSueldo.calcSueldoTotalDctos = totalDctos
                    session.merge(detalleCalculoSueldo)
                    session.commit()
                    print(f"Actualización exitosa del detalle del cálculo del sueldo del trabajador {idTrabajador} del mes {idMes}\n"
                          f"ID detalle calculo sueldo: {idDetalleCalculoSueldo}\n"
                          f"Monto de movilidad: {montoMovilidad}\n"
                          f"Monto suplementario: {montoSuplementario}\n"
                          f"Monto de horas extras: {montoHorasExtras}\n"
                          f"Monto de remuneración computable: {montoRemunComputable}\n"
                          f"Monto de descuento por faltas: {montoDctoFalta}\n"
                          f"Monto de descuento por tardanzas: {montoDctoTardanzas}\n"
                          f"Total de bonificaciones: {totalBonificaciones}\n"
                          f"Total de descuentos: {totalDctos}\n")
                else:
                    print(f"UPDATES. No se encontró el detalle del cálculo del sueldo del trabajador {idTrabajador} del mes {idMes}")
            except IntegrityError as e:
                print(f"Error al actualizar el detalle del cálculo mensual: {e}")
                session.rollback()

    @staticmethod
    def updateDetalleMensualTrabajador(idTrabajador, idMes, idDetalleCalculoSueldo, horasExtras,
                                       minutosTardanzas, minutosJustificados, diasFalta,
                                       diasJustificados, sueldoNeto):
        with Session() as session:
            try:
                detalleMensualTrabajador = session.query(tblDetalleMensualTrabajador).filter_by(
                    IDTrabajador=idTrabajador, IDMes=idMes).first()
                if detalleMensualTrabajador:

                    detalleMensualTrabajador.IDDetalleCalculoSueldo = idDetalleCalculoSueldo
                    detalleMensualTrabajador.detalleHorasExtras = horasExtras
                    detalleMensualTrabajador.detalleMinutosTardanzas = minutosTardanzas
                    detalleMensualTrabajador.detalleMinutosJustificados = minutosJustificados
                    detalleMensualTrabajador.detalleDiasFalta = diasFalta
                    detalleMensualTrabajador.detalleDiasJustificados = diasJustificados
                    detalleMensualTrabajador.detalleSueldoNeto = sueldoNeto
                    session.merge(detalleMensualTrabajador)
                    session.commit()
                    print(f"Actualización exitosa del detalle mensual del trabajador {idTrabajador} del mes {idMes}\n"
                          f"Horas extras: {horasExtras}\n"
                          f"Minutos de tardanza: {minutosTardanzas}\n"
                          f"Minutos justificados: {minutosJustificados}\n"
                          f"Días faltados: {diasFalta}\n"
                          f"Días justificados: {diasJustificados}\n"
                          f"Sueldo Neto: {sueldoNeto}")
                else:
                    print(f"UPDATES. No se encontró el detalle mensual del trabajador {idTrabajador} del mes {idMes}")
            except IntegrityError as e:
                print(f"Error al actualizar el detalle mensual: {e}")
                session.rollback()
