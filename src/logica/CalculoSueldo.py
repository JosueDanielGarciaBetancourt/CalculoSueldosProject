class CalculoSueldo:
    def __init__(self, sueldoBase, horasExtra, diasFalta, minutosTardanza, factHorasExtra, montoMovilidad,
                 factorSuplementaria):
        self.horasExtra = horasExtra
        self.sueldoBase = sueldoBase
        self.diasFalta = diasFalta
        self.minutosTardanza = minutosTardanza
        self.factHorasExtra = factHorasExtra
        self.montoMovilidad = montoMovilidad
        self.Suplementaria = factorSuplementaria
        self.DescuentoTardanzas = 0.0
        self.descuentosTotal = 0.0
        self.DescuentoFaltas = 0.0
        self.remuneracionComputable = 0.0
        self.bonificacionesTotal = 0.0
        self.totalSuplementaria = 0.0
        self.totalHorasExtra = 0.0
        self.sueldoNeto = 0.0

    def calcularBonificaciones(self):
        self.totalHorasExtra = self.factHorasExtra * self.horasExtra * ((self.sueldoBase / 30) / 8)
        self.totalSuplementaria = self.Suplementaria * self.sueldoBase
        self.remuneracionComputable = self.sueldoBase + self.montoMovilidad + self.totalSuplementaria
        self.bonificacionesTotal = round(self.montoMovilidad + self.totalSuplementaria + self.totalHorasExtra, 2)
        return self.bonificacionesTotal

    def calcularDescuentos(self):
        self.DescuentoFaltas = (self.remuneracionComputable / 30) * self.diasFalta
        self.DescuentoTardanzas = (((self.remuneracionComputable / 30) / 8) / 60) * self.minutosTardanza
        self.descuentosTotal = round(self.DescuentoFaltas + self.DescuentoTardanzas, 2)
        return self.descuentosTotal

    def calcularSueldoNeto(self):
        sueldoNeto = self.sueldoBase + self.bonificacionesTotal - self.descuentosTotal
        self.sueldoNeto = round(sueldoNeto, 2)
        return self.sueldoNeto

