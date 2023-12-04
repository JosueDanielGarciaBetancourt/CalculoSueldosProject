from modelo.tblMes import tblMes
from modelo.tblBonificacion import tblBonificacion
from modelo.tblTrabajador import tblTrabajador
from modelo.tblDetalleMensualTrabajador import tblDetalleMensualTrabajador
from modelo.tblBoletaPago import tblBoletaPago
from modelo.tblDetalleBonificacion import tblDetalleBonificacion
from modelo.Declarative_Base import Session
from sqlalchemy.exc import IntegrityError
from PyQt6.QtWidgets import QMessageBox as mensaje

class Insert:
    @staticmethod
    def insertMes(idMes, nombMes):
        with Session() as session:
            try:
                existing_mes = session.query(tblMes).get(idMes)
                if existing_mes:
                    print(f"El mes {idMes} ya existe en la base de datos.")
                else:
                    mes = tblMes(IDMes=idMes, mesNombre=nombMes)
                    session.add(mes)
                    session.commit()
                    print(f"Se agregó el mes: {idMes} {nombMes}")
            except IntegrityError as e:
                print(f"Error al agregar registro: {e}")
                session.rollback()  # Revertir cambios en caso de error

    @staticmethod
    def insertBonificacion(idBonificacion, boniTipo, boniValor):
        with Session() as session:
            try:
                existing_bonificacion = session.query(tblBonificacion).get(idBonificacion)
                if existing_bonificacion:
                    print(f"La bonificación {idBonificacion} ya existe en la base de datos.")
                else:
                    bonificacion = tblBonificacion(IDBonificacion=idBonificacion, bonTipo=boniTipo, bonValor=boniValor)
                    session.add(bonificacion)
                    session.commit()
                    print(f"Se agregó la bonificación: {idBonificacion} {boniTipo} {boniValor}")
            except IntegrityError as e:
                print(f"Error al agregar registro: {e}")
                session.rollback()  # Revertir cambios en caso de error

    @staticmethod
    def insertTrabajador(idTrabajador, trabaNombreApellidos, trabaSueldoBase, Cargo):
        with Session() as session:
            try:
                existing_trabajador = session.query(tblTrabajador).get(idTrabajador)
                if existing_trabajador:
                    print(f"El trabajador {idTrabajador} ya existe en la base de datos.")

                else:
                    trabajador = tblTrabajador(IDTrabajador=idTrabajador, trabNombreApellidos=trabaNombreApellidos,
                                               trabSueldoBase=trabaSueldoBase, Cargo=Cargo)
                    session.add(trabajador)
                    session.commit()

                    print(f"Se agregó el trabajador: {idTrabajador} {trabaNombreApellidos} {trabaSueldoBase} "
                          f"Creado el: {trabajador.created_at}")
            except IntegrityError as e:
                print(f"Error al agregar registro: {e}")

                session.rollback()  # Revertir cambios en caso de error

    @staticmethod
    def insertDetalleMensualTrabajador(idTrabajador, idMes, horasExtras, minutosTardanzas,
                                       minutosJustificados, diasFalta, diasJustificados, sueldoNeto):
        with Session() as session:
            try:
                existing_DetalleMensualTrabajador = session.query(tblDetalleMensualTrabajador).filter_by(
                    IDTrabajador=idTrabajador, IDMes=idMes).first()
                if existing_DetalleMensualTrabajador:
                    print(f"El detalle mensual del trabajador {idTrabajador} en el mes {idMes} ya existe en la base "
                          f"de datos.")
                else:
                    detalleMensualTrabajador = tblDetalleMensualTrabajador(IDTrabajador=idTrabajador, IDMes=idMes,
                                                                           detalleHorasExtras=horasExtras,
                                                                           detalleMinutosTardanzas=minutosTardanzas,
                                                                           detalleMinutosJustificados=minutosJustificados,
                                                                           detalleDiasFalta=diasFalta,
                                                                           detalleDiasJustificados=diasJustificados,
                                                                           detalleSueldoNeto=sueldoNeto)
                    session.add(detalleMensualTrabajador)
                    session.commit()
                    print(f"Se agregó el detalle mensual del trabajador {idTrabajador} en el mes {idMes}")
            except IntegrityError as e:
                print(f"Error al agregar registro: {e}")
                session.rollback()  # Revertir cambios en caso de error

    @staticmethod
    def insertBoletaPago(idBoletaPago, idTrabajador, boleSueldoNeto, boleDescuentoTotal, boleBonificacionTotal):
        with Session() as session:
            try:
                existing_BoletaPago = session.query(tblBoletaPago).filter_by(
                    IDBoletaPago=idBoletaPago, IDTrabajador=idTrabajador).first()
                if existing_BoletaPago:
                    print(
                        f"La boleta de pago {idBoletaPago} del trabajador {idTrabajador} ya existe en la base "
                        f"de datos.")
                else:
                    boletaPago = tblBoletaPago(IDBoletaPago=idBoletaPago, IDTrabajador=idTrabajador,
                                               bolSueldoNeto=boleSueldoNeto, bolDescuentoTotal=boleDescuentoTotal,
                                               bolBonificacionTotal=boleBonificacionTotal)
                    session.add(boletaPago)
                    session.commit()
                    print(f"Se agregó la boleta de pago {idBoletaPago} del trabajador {idTrabajador}")
            except IntegrityError as e:
                print(f"Error al agregar registro: {e}")
                session.rollback()  # Revertir cambios en caso de error

    @staticmethod
    def insertDetalleBonificacion(idBonificacion, idBoletaPago, detboniMontoTotalPorBonificacion):
        with Session() as session:
            try:
                existing_DetalleBonificacion = session.query(tblDetalleBonificacion).filter_by(
                    IDBonificacion=idBonificacion, IDBoletaPago=idBoletaPago).first()
                if existing_DetalleBonificacion:
                    print(
                        f"El detalle de bonificación {idBonificacion} de la boleta {idBoletaPago} ya existe en la base "
                        f"de datos.")
                else:
                    detalleBonificacion = tblDetalleBonificacion(IDBonificacion=idBonificacion, IDBoletaPago=idBoletaPago,
                                                                 detbonMontoTotalPorBonificacion=detboniMontoTotalPorBonificacion)
                    session.add(detalleBonificacion)
                    session.commit()
                    print(f"Se agregó el detalle de bonificación {idBonificacion} de la boleta {idBoletaPago}")
            except IntegrityError as e:
                print(f"Error al agregar registro: {e}")
                session.rollback()  # Revertir cambios en caso de error