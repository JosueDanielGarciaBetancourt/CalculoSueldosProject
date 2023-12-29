from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4


class GeneradorPDF:
    @staticmethod
    def generar_pdf_comprobante_pago(boleta_obj, file_path):
        pdf_canvas = canvas.Canvas(file_path, pagesize=A4)

        pdf_canvas.setFont("Helvetica", 12)

        # Obtener información de la boleta de pago
        ID_boleta = boleta_obj.IDBoletaPago
        id_trabajador = boleta_obj.IDTrabajador
        sueldo_neto = boleta_obj.bolSueldoNeto
        descuento_total = boleta_obj.bolDescuentoTotal
        bonificacion_total = boleta_obj.bolBonificacionTotal
        fecha_emision = boleta_obj.bolFechaEmision.strftime("%Y-%m-%d")
        hora_emision = boleta_obj.bolHoraEmision.strftime("%H:%M:%S")

        # Crear contenido del PDF
        contenido = [
            f"ID Boleta: {ID_boleta}",
            f"ID Trabajador: {id_trabajador}",
            f"Sueldo Neto: {sueldo_neto}",
            f"Descuento Total: {descuento_total}",
            f"Bonificación Total: {bonificacion_total}",
            f"Fecha de Emisión: {fecha_emision}",
            f"Hora de Emisión: {hora_emision}"
        ]

        # Agregar contenido al PDF
        pdf_canvas.drawString(100, 750, "Comprobante de Pago")
        pdf_canvas.drawString(100, 730, "-" * 40)

        y_position = 710  # Posición vertical inicial
        for line in contenido:
            pdf_canvas.drawString(100, y_position, line)
            y_position -= 12  # Desplazarse hacia arriba para la siguiente línea

        pdf_canvas.save()
