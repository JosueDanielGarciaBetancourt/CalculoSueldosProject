from src.modelo.modeladoTablas import tblMes
from src.modelo.modeladoTablas import tblBonificacion
from src.modelo.modeladoTablas import tblTrabajador
from src.modelo.modeladoTablas import tblDetalleCalculoSueldo
from src.modelo.modeladoTablas import tblDetalleMensualTrabajador
from src.modelo.modeladoTablas import tblBoletaPago
from src.modelo.modeladoTablas import tblDetalleBonificacion
from modelo.Declarative_Base import Session
from sqlalchemy.exc import IntegrityError
from PyQt6.QtCore import pyqtSignal, QObject


class DeleteSignal(QObject):
    trabajadorDeleted = pyqtSignal()


class Deletes:
    signal = DeleteSignal()

    @staticmethod
    def deleteMes(idMes):
        with Session() as session:
            try:
                mes = session.query(tblMes).get(idMes)
                if mes:
                    print(f"Se borrará el mes: {mes.mesNombre}")
                    session.delete(mes)
                    session.commit()
                    print("Mes borrado exitosamente.")
                else:
                    print(f"No se encontró el mes con ID: {idMes}")
            except IntegrityError as e:
                print(f"Error al borrar el mes: {e}")
                session.rollback()  # Revertir cambios en caso de error

    @staticmethod
    def deleteBonificacion(idBonificacion):
        with Session() as session:
            try:
                bonificacion = session.query(tblBonificacion).get(idBonificacion)
                if bonificacion:
                    print(f"Se borrará la bonificación: {bonificacion.bonTipo}")
                    session.delete(bonificacion)
                    session.commit()
                    print("Bonificación borrada exitosamente.")
                else:
                    print(f"No se encontró la bonificación con ID: {idBonificacion}")
            except IntegrityError as e:
                print(f"Error al borrar la bonificación: {e}")
                session.rollback()  # Revertir cambios en caso de error

    @staticmethod
    def deleteTrabajador(idTrabajador):
        with Session() as session:
            try:
                trabajador = session.query(tblTrabajador).get(idTrabajador)
                if trabajador:
                    print(f"Se borrará el trabajador: {trabajador.trabNombreApellidos}")
                    session.delete(trabajador)
                    session.commit()
                    Deletes.signal.trabajadorDeleted.emit()
                    print("Trabajador borrado exitosamente.")
                else:
                    print(f"No se encontró el trabajador con ID: {idTrabajador}")
            except IntegrityError as e:
                print(f"Error al borrar el trabajador: {e}")
                session.rollback()  # Revertir cambios en caso de error


