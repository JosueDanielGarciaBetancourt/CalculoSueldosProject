class CalcBonifiDctos:
    bonificaciones = 0.0
    remuneracionComputable = 0.0

    @staticmethod
    def inicializar_bonificaciones(factorHoraExtra, movilidad, factorBoniSuplementaria):
        CalcBonifiDctos.factorHoraExtra = factorHoraExtra
        CalcBonifiDctos.movilidad = movilidad
        CalcBonifiDctos.factorBoniSuplementaria = factorBoniSuplementaria

    @staticmethod
    def calcularBonificaciones(trabajador):
        pagoHorasExtras = (1 + CalcBonifiDctos.factorHoraExtra) * trabajador.horasExtras * trabajador.sueldoBasico * \
                          (1 / 30) * (1 / 8)
        movilidadTrabajador = CalcBonifiDctos.movilidad
        bonificacionSuplementaria = CalcBonifiDctos.factorBoniSuplementaria * trabajador.sueldoBasico
        bonificacionTotal = CalcBonifiDctos.movilidad + bonificacionSuplementaria + pagoHorasExtras
        remuneracionComputable = trabajador.sueldoBasico + CalcBonifiDctos.movilidad + bonificacionSuplementaria
        return pagoHorasExtras, movilidadTrabajador, bonificacionSuplementaria, bonificacionTotal, remuneracionComputable

    @staticmethod
    def calcularDescuentos(trabajador):
        remuneracionMinima = trabajador.sueldoBasico + CalcBonifiDctos.bonificaciones
        descuentoFaltas = CalcBonifiDctos.remuneracionComputable * (trabajador.diasFalta / 30)
        descuentoTardanzas = CalcBonifiDctos.remuneracionComputable * (1 / 30) * (1 / 8) * (1 / 60) * \
                             trabajador.minutosTardanza
        descuentoTotal = descuentoFaltas + descuentoTardanzas
        return remuneracionMinima, descuentoFaltas, descuentoTardanzas, descuentoTotal
