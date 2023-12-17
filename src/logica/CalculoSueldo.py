class CalculoSueldo():
    def __init__(self, sueldoBase, horasExtra, diasFalta, minutosTardanza, montoMovilidad, factorSuplementaria):
        self.horasExtra = horasExtra
        self.sueldoBase = sueldoBase
        self.diasFalta = diasFalta
        self.minutosTardanza = minutosTardanza
        self.Movilidad = montoMovilidad
        self.Suplementaria = factorSuplementaria

    def CalcularSueldoNeto(self):
        sueldoBasico = self.sueldoBase
        bonificaciones = self.CalculoBonificaciones()
        descuentos = self.CalculoDescuentos()
        sueldoNeto = sueldoBasico+bonificaciones-descuentos
        sueldoNeto = round(sueldoNeto, 2)
        return sueldoNeto

    def CalculoBonificaciones(self):
        self.PagoHorasExtra = 1.50*self.horasExtra*((self.sueldoBase / 30) / 8)
        self.BonificacionSuplementaria = self.Suplementaria * self.sueldoBase
        self.Bonificaciones = self.Movilidad + self.BonificacionSuplementaria + self.PagoHorasExtra
        self.remuneracionComputable = self.sueldoBase + self.Movilidad + self.BonificacionSuplementaria
        return self.Bonificaciones

    def CalculoDescuentos(self):
        #self.remuneracionMinima = self.sueldoBase + self.Bonificaciones
        self.DescuentoFaltas = self.remuneracionComputable/30*self.diasFalta
        self.DescuentoTardanza = (((self.remuneracionComputable/30)/8)/60)*self.minutosTardanza
        self.descuentos = self.DescuentoFaltas+self.DescuentoTardanza
        return self.descuentos

