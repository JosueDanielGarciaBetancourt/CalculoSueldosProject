from datetime import datetime

class BoletaPago:
    #Lista para almacenar objetos BoletaPago
    listaBoletaPago = []
    def __init__(self, IdBoleta, fechaEmision, descuentoTotal, bonificacionTotal, sueldoNeto):
        self.IdBoleta = IdBoleta
        self.fechaEmision = fechaEmision
        self.descuentoTotal = descuentoTotal
        self.bonificacionTotal = bonificacionTotal
        self.sueldoNeto = sueldoNeto

        BoletaPago.listaBoletaPago.append(self)
    @staticmethod
    def obtenerCodigoBoleta(IdTrabajador):
        now = datetime.now()
        mes_actual = now.month
        anio_actual = now.year
        IdBoletaPago = f"Boleta{anio_actual}{mes_actual}-{IdTrabajador}"
        return IdBoletaPago

    def imprimirBoletaPago(self):
        print(f"\nID de boleta: {self.IdBoleta}")
        print(f"Fecha de emisión: {self.fechaEmision}")
        print(f"Descuento total: {self.descuentoTotal}")
        print(f"Bonificación total: {self.bonificacionTotal}")
        print(f"Sueldo neto: {self.sueldoNeto}")