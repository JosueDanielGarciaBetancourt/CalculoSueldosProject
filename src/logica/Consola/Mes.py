from datetime import datetime

class Mes:
    # Lista para almacenar objetos Mes
    listaMeses = []

    def __init__(self, IdMes, nombMes):
        self.__IdMes = IdMes  # name mangling
        self.__nombMes = nombMes
        Mes.listaMeses.append(self)


    def getMes(self):
        return self.__IdMes, self.__nombMes

    def setMes(self, nuevo_IdMes, nuevo_nombre_mes):
        self.__IdMes = nuevo_IdMes
        self.__nombMes = nuevo_nombre_mes

    @staticmethod
    def obtenerMesActual():
        fecha_actual = datetime.now()
        mes_actual = fecha_actual.month
        IdMesActual = None
        nombMesActual = None
        for mes in Mes.listaMeses:
            if mes.__IdMes == mes_actual:
                IdMesActual, nombMesActual = mes.getMes()
        return IdMesActual, nombMesActual

    @staticmethod
    def imprimir_meses():
        print(f"ID  Nombre")
        for mes in Mes.listaMeses:
            __id_mes, __nombMes = mes.getMes()
            print(f"{__id_mes} {__nombMes.ljust(40)}")
