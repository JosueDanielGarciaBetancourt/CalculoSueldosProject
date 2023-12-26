class CalculoSueldo():
    def __init__(self, sueldoBase, horasExtra, diasFalta, minutosTardanza, factHorasExtra, montoMovilidad,
                 factorSuplementaria):
        self.horasExtra = horasExtra
        self.sueldoBase = sueldoBase
        self.diasFalta = diasFalta
        self.minutosTardanza = minutosTardanza
        self.factHorasExtra = factHorasExtra
        self.Movilidad = montoMovilidad
        self.Suplementaria = factorSuplementaria
        self.DescuentoTardanza = None
        self.descuentosTotal = None
        self.DescuentoFaltas = None
        self.remuneracionComputable = None
        self.bonificacionesTotal = None
        self.BonificacionSuplementaria = None
        self.PagoHorasExtra = None

    def calcularBonificaciones(self):
        self.PagoHorasExtra = self.factHorasExtra * self.horasExtra * ((self.sueldoBase / 30) / 8)
        self.BonificacionSuplementaria = self.Suplementaria * self.sueldoBase
        self.bonificacionesTotal = round(self.Movilidad + self.BonificacionSuplementaria + self.PagoHorasExtra, 2)
        self.remuneracionComputable = self.sueldoBase + self.Movilidad + self.BonificacionSuplementaria
        return self.bonificacionesTotal

    def calcularDescuentos(self):
        self.DescuentoFaltas = self.remuneracionComputable / 30 * self.diasFalta
        self.DescuentoTardanza = (((self.remuneracionComputable / 30) / 8) / 60) * self.minutosTardanza
        self.descuentosTotal = round(self.DescuentoFaltas + self.DescuentoTardanza, 2)
        return self.descuentosTotal

    def calcularSueldoNeto(self):
        sueldoBasico = self.sueldoBase
        bonificaciones = self.calcularBonificaciones()
        descuentos = self.calcularDescuentos()
        sueldoNeto = sueldoBasico + bonificaciones - descuentos
        sueldoNeto = round(sueldoNeto, 2)
        return sueldoNeto
