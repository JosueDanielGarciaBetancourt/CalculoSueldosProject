from src.modelo.modeladoTablas import tblMes
from src.modelo.modeladoTablas import tblBonificacion
from src.modelo.modeladoTablas import tblTrabajador
from src.modelo.modeladoTablas import tblDetalleCalculoSueldo
from src.modelo.modeladoTablas import tblDetalleMensualTrabajador
from src.modelo.modeladoTablas import tblBoletaPago
from src.modelo.modeladoTablas import tblDetalleBonificacion
from modelo.Declarative_Base import Session
from sqlalchemy import func


class Queries:
    @staticmethod
    def get_mes_by_id(id_mes):
        with Session() as session:
            mes = session.query(tblMes).filter_by(IDMes=id_mes).first()
            return mes

    @staticmethod
    def get_bonificacion_by_id(id_bonificacion):
        with Session() as session:
            bonificacion = session.query(tblBonificacion).filter_by(IDBonificacion=id_bonificacion).first()
            return bonificacion

    @staticmethod
    def get_last_bonification():
        with Session() as session:
            # Ordena las bonificaciones por ID de manera descendente y toma la primera
            bonificacion = session.query(tblBonificacion).order_by(tblBonificacion.IDBonificacion.desc()).first()
            return bonificacion

    @staticmethod
    def get_num_bonificaciones():
        with Session() as session:
            num_bonificaciones = session.query(func.count(tblBonificacion.IDBonificacion)).scalar()
            return num_bonificaciones

    @staticmethod
    def get_trabajador_by_id(id_trabajador):
        with Session() as session:
            trabajador = session.query(tblTrabajador).filter_by(IDTrabajador=id_trabajador).first()
            return trabajador

    @staticmethod
    def get_trabajadores_by_idPrefijo(idPrefijo):
        with Session() as session:
            trabajadores = session.query(tblTrabajador).filter(tblTrabajador.IDTrabajador.like(f"{idPrefijo}%")).all()
            return trabajadores

    @staticmethod
    def get_trabajador_by_name(nomb_apell_Trabajador):
        with Session() as session:
            trabajador = session.query(tblTrabajador).filter_by(trabNombreApellidos=nomb_apell_Trabajador).first()
            return trabajador

    @staticmethod
    def get_trabajadores_by_namePrefijo(namePrefijo):
        with Session() as session:
            trabajadores = session.query(tblTrabajador).filter(
                tblTrabajador.trabNombreApellidos.like(f"{namePrefijo}%")).all()
            return trabajadores

    @staticmethod
    def get_all_trabajadores():
        with Session() as session:
            allTrabajadores = session.query(tblTrabajador).all()
            return allTrabajadores

    @staticmethod
    def get_detalle_mensual_trabajador_by_id(id_trabajador, id_mes):
        with Session() as session:
            detalle_mensual = session.query(tblDetalleMensualTrabajador).filter_by(IDTrabajador=id_trabajador,
                                                                                   IDMes=id_mes).first()
            return detalle_mensual


    @staticmethod
    def get_detalle_mensual_trabajador_by_date(datetime):
        with Session() as session:
            detalle_mensual = session.query(tblDetalleMensualTrabajador).filter_by(detalleFecha=datetime).first()
            return detalle_mensual

    @staticmethod
    def get_all_detalle_mensual_trabajador_by_id(id_trabajador):
        with Session() as session:
            detalle_mensual_lista = session.query(tblDetalleMensualTrabajador).filter_by(
                IDTrabajador=id_trabajador).all()
            return detalle_mensual_lista

    @staticmethod
    def get_detalle_calculo_sueldo_by_id(id_trabajador, id_mes):
        with Session() as session:
            detalle_calculo_sueldo = session.query(tblDetalleCalculoSueldo).filter_by(IDTrabajador=id_trabajador,
                                                                                      IDMes=id_mes).first()
            return detalle_calculo_sueldo

    @staticmethod
    def get_boleta_pago_by_id(id_boleta_pago):
        with Session() as session:
            boleta_pago = session.query(tblBoletaPago).filter_by(IDBoletaPago=id_boleta_pago).first()
            return boleta_pago

    @staticmethod
    def get_detalle_bonificacion_by_id(id_bonificacion, id_boleta_pago):
        with Session() as session:
            detalle_bonificacion = session.query(tblDetalleBonificacion).filter_by(IDBonificacion=id_bonificacion,
                                                                                   IDBoletaPago=id_boleta_pago).first()
            return detalle_bonificacion
