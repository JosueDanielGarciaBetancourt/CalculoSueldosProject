class Bonificacion:
    # Lista para almacenar objetos Bonificacion
    listaBonificaciones = []

    def __init__(self, IdBonificacion, tipo, valor):
        self.__IdBonificacion = IdBonificacion  # name mangling
        self.__tipo = tipo
        self.__valor = valor
        Bonificacion.listaBonificaciones.append(self)

    def getBonificacion(self):
        return self.__IdBonificacion, self.__tipo, self.__valor

    def setBonificacion(self, nuevo_IdBonificacion, nuevo_tipo, nuevo_valor):
        self.__IdBonificacion = nuevo_IdBonificacion
        self.__tipo = nuevo_tipo
        self.__valor = nuevo_valor

    @staticmethod
    def imprimirTablaBonificaciones():
        print(f"\nID  Tipo                                    Valor")
        for bonificacion in Bonificacion.listaBonificaciones:
            id_bono, tipo, valor = bonificacion.getBonificacion()
            print(f"{id_bono}   {tipo.ljust(40)} {valor}")

