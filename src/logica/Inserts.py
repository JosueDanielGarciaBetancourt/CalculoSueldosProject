from modelo.tblMes import tblMes
from modelo.tblBonificacion import tblBonificacion
from modelo.tblTrabajador import tblTrabajador
from modelo.tblDetalleMensualTrabajador import tblDetalleMensualTrabajador
from modelo.tblBoletaPago import tblBoletaPago
from modelo.tblDetalleBonificacion import tblDetalleBonificacion
from modelo.Declarative_Base import Session
from sqlalchemy.exc import IntegrityError
from vista.Window_Utils import MensajesWindow
from PyQt6.QtCore import pyqtSignal, QObject


class InsertSignal(QObject):
    trabajadorInserted = pyqtSignal()


class Inserts:
    signal = InsertSignal()

    @staticmethod
    def insertMes(idMes, nombMes):
        with Session() as session:
            try:
                existing_mes = session.query(tblMes).get(idMes)
                if existing_mes:
                    mensaje = f"El mes {idMes} ya existe en la base de datos."
                    print(mensaje)
                    # MensajesWindow.mostrarMensajeRegistroError("Error de registro", mensaje)
                else:
                    mes = tblMes(IDMes=idMes, mesNombre=nombMes)
                    session.add(mes)
                    session.commit()
                    mensaje = "Se agregó el mes satisfactoriamente"
                    print(f"{mensaje}: \nID: {idMes}\nNombre: {nombMes}")
                    # MensajesWindow.mostrarMensajeRegistroExito(mensaje)
            except IntegrityError as e:
                print(f"Error al agregar registro: {e}")
                session.rollback()  # Revertir cambios en caso de error

    @staticmethod
    def insertBonificacion(idBonificacion, boniTipo, boniUnidad, boniValor):
        with Session() as session:
            try:
                existing_bonificacion = session.query(tblBonificacion).get(idBonificacion)
                if existing_bonificacion:
                    mensaje = f"La bonificación {idBonificacion} ya existe en la base de datos."
                    print(mensaje)
                    MensajesWindow.mostrarMensajeRegistroError(mensaje)
                else:
                    bonificacion = tblBonificacion(IDBonificacion=idBonificacion, bonTipo=boniTipo, bonUnidad=boniUnidad, bonValor=boniValor)
                    session.add(bonificacion)
                    session.commit()
                    mensaje = f"Se registró correctamente la bonificación\n ID: {idBonificacion}\n" \
                              f" Tipo:  {boniTipo}\n Unidad: {boniUnidad}\n Valor: {boniValor}\n "
                    print(mensaje)
                    #MensajesWindow.mostrarMensajeRegistroExito(mensaje)
            except IntegrityError as e:
                print(f"Error al agregar registro: {e}")
                session.rollback()  # Revertir cambios en caso de error

    @staticmethod
    def insertTrabajador(idTrabajador, trabaNombreApellidos, trabaSueldoBase, Cargo):
        with Session() as session:
            try:
                existing_trabajador = session.query(tblTrabajador).get(idTrabajador)
                if existing_trabajador:
                    mensaje = f"El trabajador con DNI {idTrabajador} ya existe en la base de datos."
                    print(mensaje)
                    MensajesWindow.mostrarMensajeRegistroError(mensaje)
                else:
                    trabajador = tblTrabajador(IDTrabajador=idTrabajador, trabNombreApellidos=trabaNombreApellidos,
                                               trabSueldoBase=trabaSueldoBase, trabCargo=Cargo)
                    session.add(trabajador)
                    session.commit()
                    mensaje = "Se agregó el trabajador satisfactoriamente"
                    print(f"{mensaje}\nID: {idTrabajador}\nApellidos y Nombres: {trabaNombreApellidos}"
                          f"\nSueldo Base: {trabaSueldoBase}\nCargo: {Cargo}\nCreado el {trabajador.created_at}")
                    Inserts.signal.trabajadorInserted.emit()
                    #MensajesWindow.mostrarMensajeRegistroExito("Se agregó el trabajador satisfactoriamente")
            except IntegrityError as e:
                mensaje = f"Error al agregar registro: {e}"
                print(mensaje)
                MensajesWindow.mostrarMensajeRegistroError(mensaje)
                session.rollback()  # Revertir cambios en caso de error
            except Exception as ex:
                mensaje = f"INSERTS. Error al insertar trabajador {ex}"
                print(mensaje)
                MensajesWindow.mostrarMensajeRegistroError(mensaje)

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
                    detalleBonificacion = tblDetalleBonificacion(IDBonificacion=idBonificacion,
                                                                 IDBoletaPago=idBoletaPago,
                                                                 detbonMontoTotalPorBonificacion=detboniMontoTotalPorBonificacion)
                    session.add(detalleBonificacion)
                    session.commit()
                    print(f"Se agregó el detalle de bonificación {idBonificacion} de la boleta {idBoletaPago}")
            except IntegrityError as e:
                print(f"Error al agregar registro: {e}")
                session.rollback()  # Revertir cambios en caso de error
