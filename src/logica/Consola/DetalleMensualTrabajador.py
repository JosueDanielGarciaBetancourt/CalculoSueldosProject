class DetalleMensualTrabajador:
    def __init__(self, IdTrabajador, IdMes, Anio, horasExtras, minutosTardanza, minutosJustificados, diasFalta,
                 diasJustificados, sueldoNeto):
        self.IdTrabajador = IdTrabajador
        self.IdMes = IdMes
        self.Anio = Anio
        self.horasExtras = horasExtras
        self.minutosTardanza = minutosTardanza
        self.minutosJustificados = minutosJustificados
        self.diasFalta = diasFalta
        self.diasJustificados = diasJustificados
        self.sueldoNeto = sueldoNeto

    def imprimirDetalleMensualTrabajador(self):
        print(f"\nID del trabajador: {self.IdTrabajador}")
        print(f"ID del mes: {self.IdMes}")
        print(f"Año: {self.Anio}")
        print(f"Horas extra: {self.horasExtras}")
        print(f"Minutos de tardanza: {self.Anio}")
        print(f"Minutos justificados: {self.minutosJustificados}")
        print(f"Días faltados: {self.diasFalta}")
        print(f"Días justificados: {self.diasJustificados}")
        print(f"Sueldo Neto: {self.sueldoNeto}")



