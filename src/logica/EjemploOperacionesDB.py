from logica.Inserts import Inserts, MensajesWindow
from logica.Deletes import Deletes
from logica.Updates import Updates
from logica.Queries import Queries
from logica.CalculoSueldo import CalculoSueldo


def EjemploOperacionesDB():
    print("\n==============INSERTS==============")
    print("\nMESES")

    # Insertar meses
    Inserts.insertMes("MES01", "ENERO")
    Inserts.insertMes("MES02", "FEBRERO")
    Inserts.insertMes("MES03", "MARZO")
    Inserts.insertMes("MES04", "ABRIL")
    Inserts.insertMes("MES05", "MAYO")
    Inserts.insertMes("MES06", "JUNIO")
    Inserts.insertMes("MES07", "JULIO")
    Inserts.insertMes("MES08", "AGOSTO")
    Inserts.insertMes("MES09", "SEPTIEMBRE")
    Inserts.insertMes("MES10", "OCTUBRE")
    Inserts.insertMes("MES11", "NOVIEMBRE")
    Inserts.insertMes("MES12", "DICIEMBRE")

    print("\nBONIFICACIONES")
    # Insertar bonificaciones
    Inserts.insertBonificacion("BONI01", "Factor por horas extras", "-", 0.50)
    Inserts.insertBonificacion("BONI02", "Movilidad", "S/.", 1000.00)
    Inserts.insertBonificacion("BONI03", "Factor de bonificación suplementaria", "-", 0.03)

    print("\nTRABAJADORES")
    # Insertar trabajador
    Inserts.insertTrabajador("77043114", "Josué García", 500.00, "CIO")
    Inserts.insertTrabajador("12345678", "Sergio Ramírez", 700.00, "CIO2")
    Inserts.insertTrabajador("12345672", "Manuel Romero", 1200.00, "CIO3")
    Inserts.insertTrabajador("12345661", "Emiliano Peralta", 1100.00, "CIO4")
    Inserts.insertTrabajador("12345662", "Jeison Oré", 1700.00, "CIO5")
    Inserts.insertTrabajador("12345400", "David Contreras", 1000.00, "CIO6")
    Inserts.insertTrabajador("12345401", "Eduardo Campos", 1500.00, "CIO7")
    Inserts.insertTrabajador("87654321", "Gian Piere", 1200.00, "CIO8")

    print("\nDETALLE MENSUAL TRABAJADOR")
    # Insertar detalle mensual trabajador
    Inserts.insertDetalleMensualTrabajador("77043114", "MES11", 3, 60, 30, 1, 1, 2000.00)
    Inserts.insertDetalleMensualTrabajador("77043114", "MES12", 3, 60, 30, 1, 1, 2000.00)
    Inserts.insertDetalleMensualTrabajador("12345678", "MES05", 3, 60, 30, 1, 1, 2000.00)

    print("\nBOLETA DE PAGO")
    # Insertar boleta pago
    Inserts.insertBoletaPago("BOLE0177043114", "77043114", 2000.00, 200.00, 1700.00)
    Inserts.insertBoletaPago("BOLE0112345678", "12345678", 2000.00, 200.00, 1700.00)

    print("\nDETALLE BONIFICACIÓN")
    # Insertar detalle de bonificación
    Inserts.insertDetalleBonificacion("BONI01", "BOLE0177043114", 250.00)
    Inserts.insertDetalleBonificacion("BONI02", "BOLE0177043114", 1000.00)
    Inserts.insertDetalleBonificacion("BONI03", "BOLE0112345678", 750.00)

    print("\n==============DELETES==============")
    print("\nMES")
    # Eliminando un mes
    # Deletes.deleteMes("MES12")

    print("\nTRABAJADOR")
    # Eliminando un trabajador (esto borrará registros en boletaPago)
    Deletes.deleteTrabajador("77043114")

    print("\nBONIFICACIÓN")
    # Eliminando una bonificación (esto borrará registros en detalleBonificacion)
    # Delete.deleteBonificacion("BONI02")

    print("\n==============UPDATES==============")

    print("\nSUELDO BASE")
    Updates.updateSueldoBase("12345678", 100)

    print("\nBONIFICACIÓN")
    Updates.updateValorBonificacion("BONI01", 0.6)

    print("\n==============QUERIES==============\n")

    # Ejemplo: Obtener un mes por ID
    print("MES")
    mes = Queries.get_mes_by_id("MES05")
    if mes:
        print("ID del Mes: ", mes.IDMes)
        print("Nombre del Mes: ", mes.mesNombre)
    else:
        print("No se encontró el mes.")

    print()

    # Ejemplo: Obtener una bonificación por ID
    print("BONIFICACIÓN")
    bonificacion = Queries.get_bonificacion_by_id("BONI03")
    if bonificacion:
        print("ID de Bonificación: ", bonificacion.IDBonificacion)
        print("Tipo de Bonificación: ", bonificacion.bonTipo)
        print("Valor de Bonificación: ", bonificacion.bonValor)
    else:
        print("No se encontró la bonificación.")

    print()

    # Ejemplo: Obtener un trabajador por ID
    print("TRABAJADOR")
    trabajador = Queries.get_trabajador_by_id("12345678")
    if trabajador:
        print("ID del Trabajador: ", trabajador.IDTrabajador)
        print("Nombre y Apellidos: ", trabajador.trabNombreApellidos)
        print("Cargo: ", trabajador.trabCargo)
        print("Sueldo Base: ", trabajador.trabSueldoBase)
        print("Fecha de Creación: ", trabajador.created_at)
    else:
        print("No se encontró el trabajador.")

    print()

    # Ejemplo: Obtener un detalle mensual de trabajador por ID de trabajador y ID de mes
    print("DETALLE MENSUAL")
    detalle_mensual = Queries.get_detalle_mensual_trabajador_by_id("12345678", "MES05")
    if detalle_mensual:
        print("ID del Trabajador: ", detalle_mensual.IDTrabajador)
        print("ID del Mes: ", detalle_mensual.IDMes)
        print("Año: ", detalle_mensual.detalleAnio)
        print("Horas extras: ", detalle_mensual.detalleHorasExtras)
        print("Minutos de tardanza: ", detalle_mensual.detalleMinutosTardanzas)
        print("Horas extras: ", detalle_mensual.detalleHorasExtras)
        print("Minutos justificados: ", detalle_mensual.detalleMinutosJustificados)
        print("Días de falta: ", detalle_mensual.detalleDiasFalta)
        print("Días justificados: ", detalle_mensual.detalleDiasJustificados)
        print("Sueldo Neto: ", detalle_mensual.detalleSueldoNeto)
    else:
        print("No se encontró el detalle mensual.")

    print()

    # Ejemplo: Obtener una boleta de pago por ID
    print("BOLETA DE PAGO")
    boleta_pago = Queries.get_boleta_pago_by_id("BOLE0112345678")
    if boleta_pago:
        print("ID de Boleta de Pago:", boleta_pago.IDBoletaPago)
        print("ID del Trabajador:", boleta_pago.IDTrabajador)
        print("Sueldo Neto:", boleta_pago.bolSueldoNeto)
        print("Descuento Total:", boleta_pago.bolDescuentoTotal)
        print("Bonificación Total:", boleta_pago.bolBonificacionTotal)
        print("Fecha de Emisión:", boleta_pago.bolFechaEmision)
        print("Hora de Emisión:", boleta_pago.bolHoraEmision)
    else:
        print("No se encontró la boleta de pago.")

    print()

    # Ejemplo: Obtener un detalle de bonificación por ID de bonificación y ID de boleta de pago
    print("DETALLE DE BONIFICACIÓN")
    detalle_bonificacion = Queries.get_detalle_bonificacion_by_id("BONI03", "BOLE0112345678")
    if detalle_bonificacion:
        print("ID de Bonificación:", detalle_bonificacion.IDBonificacion)
        print("ID de Boleta de Pago:", detalle_bonificacion.IDBoletaPago)
        print("Monto total de bonificación: ", detalle_bonificacion.detbonMontoTotalPorBonificacion)
    else:
        print("No se encontró el detalle de bonificación.")

    print("\n==============PRUEBA CÁLCULO SUELDO==============\n")

    trab02 = Queries.get_trabajador_by_id("12345678")
    detalleTrab02 = Queries.get_detalle_mensual_trabajador_by_id("12345678", "MES05")
    factHorasExtra = Queries.get_bonificacion_by_id("BONI01")
    Movilidad = Queries.get_bonificacion_by_id("BONI02")
    factSuplementaria = Queries.get_bonificacion_by_id("BONI03")

    print("BONIFICACIONES: \n")
    print("Factor de horas extra: ", )
    print("Movilidad: ", factHorasExtra.bonValor)
    print("Factor de bonif. Suplementaria: ", factSuplementaria.bonValor)
    print("12345678: \n")
    print("ID del Trabajador: ", trab02.IDTrabajador)
    print("Nombre y Apellidos: ", trab02.trabNombreApellidos)
    print("Sueldo Base: ", trab02.trabSueldoBase)
    print("Fecha de Creación: ", trab02.created_at)
    print("\nDetalle mensual 12345678: \n")
    print("ID del Trabajador: ", detalleTrab02.IDTrabajador)
    print("ID del Mes: ", detalleTrab02.IDMes)
    print("Año: ", detalleTrab02.detalleAnio)
    print("Horas extras: ", detalleTrab02.detalleHorasExtras)
    print("Minutos de tardanza: ", detalleTrab02.detalleMinutosTardanzas)
    print("Horas extras: ", detalleTrab02.detalleHorasExtras)
    print("Minutos justificados: ", detalleTrab02.detalleMinutosJustificados)
    print("Días de falta: ", detalleTrab02.detalleDiasFalta)
    print("Días justificados: ", detalleTrab02.detalleDiasJustificados)

    calcularSueldoTrab01 = CalculoSueldo(trab02.trabSueldoBase, detalleTrab02.detalleHorasExtras,
                                         detalleTrab02.detalleDiasFalta, detalleTrab02.detalleMinutosTardanzas,
                                         factHorasExtra.bonValor, Movilidad.bonValor, factSuplementaria.bonValor)

    sueldoNetoTrab02 = calcularSueldoTrab01.calcularSueldoNeto()

    print(f"\nEl SUELDO NETO de 12345678 es: {sueldoNetoTrab02}")
