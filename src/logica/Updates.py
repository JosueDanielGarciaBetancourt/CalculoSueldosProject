from modelo.tblBonificacion import tblBonificacion
from modelo.tblTrabajador import tblTrabajador
from modelo.tblDetalleMensualTrabajador import tblDetalleMensualTrabajador
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
    def updateDetalleMensualTrabajador(idTrabajador, idMes, horasExtras,
                                       minutosTardanzas, minutosJustificados, diasFalta,
                                       diasJustificados, sueldoNeto):
        with Session() as session:
            try:
                detalleMensualTrabajador = session.query(tblDetalleMensualTrabajador).filter_by(
                    IDTrabajador=idTrabajador, IDMes=idMes).first()
                if detalleMensualTrabajador:

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
