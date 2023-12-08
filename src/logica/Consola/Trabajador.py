from logica.CalcBonifiDctos import CalcBonifiDctos

class Trabajador:
    # Lista para almacenar objetos Trabajador
    listaTrabajadores = []

    def __init__(self, IdTrabajador, nombreTrabajador, sueldoBasico, diasFalta, minutosTardanza, horasExtras):
        self.IdTrabajador = IdTrabajador
        self.nombreTrabajador = nombreTrabajador
        self.sueldoBasico = sueldoBasico
        self.diasFalta = diasFalta
        self.minutosTardanza = minutosTardanza
        self.horasExtras = horasExtras
        self.minutosJustificados = 0
        self.diasJustificados = 0
        # Atributos calculados
        self.pagoHorasExtras = 0.0
        self.movilidadTrabajador = 0.0
        self.bonificacionSuplementaria = 0.0
        self.bonificacionTotal = 0.0
        self.remuneracionComputable = 0.0
        self.remuneracionMinima = 0.0
        self.descuentoFaltas = 0.0
        self.descuentoTardanzas = 0.0
        self.descuentoTotal = 0.0
        self.sueldoNeto = 0.0
        self.sueldoNetoRedondeado = 0.0

        Trabajador.listaTrabajadores.append(self)

    def getTrabajador(self):
        return self.IdTrabajador, self.nombreTrabajador, self.sueldoBasico, self.diasFalta, self.minutosTardanza, \
        self.horasExtras, self.minutosJustificados, self.diasJustificados, self.pagoHorasExtras, self.movilidadTrabajador, self.bonificacionSuplementaria, \
        self.bonificacionTotal, self.remuneracionComputable, self.remuneracionMinima, self.descuentoFaltas, \
        self.descuentoTardanzas, self.descuentoTotal, self.sueldoNeto, self.sueldoNetoRedondeado

    def setTrabajador(self, nuevo_nombreTrabajador, nuevo_sueldoBasico, nuevo_diasFalta, nuevo_minutosTardanza, nuevo_horasExtras):
        self.nombreTrabajador = nuevo_nombreTrabajador
        self.sueldoBasico = nuevo_sueldoBasico
        self.diasFalta = nuevo_diasFalta
        self.minutosTardanza = nuevo_minutosTardanza
        self.horasExtras = nuevo_horasExtras

    def setDiasJustificados(self, nuevoDiasJustificados):
        self.diasJustificados = nuevoDiasJustificados

    def setMinutosJustificados(self, nuevoMinutosJustificados):
        self.minutosJustificados = nuevoMinutosJustificados

    def calcularBonificacion(self, trabajador):
        self.pagoHorasExtras, self.movilidadTrabajador, self.bonificacionSuplementaria, \
        self.bonificacionTotal, self.remuneracionComputable = CalcBonifiDctos.calcularBonificaciones(trabajador)

    def calcularDescuento(self, trabajador):
        self.remuneracionMinima, self.descuentoFaltas, self.descuentoTardanzas, self.descuentoTotal =\
        CalcBonifiDctos.calcularDescuentos(trabajador)

    def calcularSueldoNeto(self):
        self.sueldoNeto = self.sueldoBasico + self.bonificacionTotal + self.descuentoTotal
        self.sueldoNetoRedondeado = round(self.sueldoNeto, 2)

    def imprimir_atributos_trabajador(self):
        print(f" ID: {self.IdTrabajador}")
        print(f" El nombre es: {self.nombreTrabajador}")
        print(f" El sueldo es: {self.sueldoBasico}")
        print(f" Los días de falta son: {self.diasFalta}")
        print(f" Los minutos de tardanza son: {self.minutosTardanza}")
        print(f" Las horas extra son: {self.horasExtras}")
        print(f" El SUELDO NETO es: {self.sueldoNetoRedondeado}")
