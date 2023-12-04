from modelo.tblMes import tblMes
from modelo.tblBonificacion import tblBonificacion
from modelo.tblTrabajador import tblTrabajador
from modelo.tblDetalleMensualTrabajador import tblDetalleMensualTrabajador
from modelo.tblBoletaPago import tblBoletaPago
from modelo.tblDetalleBonificacion import tblDetalleBonificacion
from modelo.Declarative_Base import Session


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
    def get_trabajador_by_id(id_trabajador):
        with Session() as session:
            trabajador = session.query(tblTrabajador).filter_by(IDTrabajador=id_trabajador).first()
            return trabajador

    @staticmethod
    def get_detalle_mensual_trabajador_by_id(id_trabajador, id_mes):
        with Session() as session:
            detalle_mensual = session.query(tblDetalleMensualTrabajador).filter_by(IDTrabajador=id_trabajador,
                                                                                   IDMes=id_mes).first()
            return detalle_mensual

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
