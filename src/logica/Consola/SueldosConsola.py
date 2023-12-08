import os
from datetime import datetime
from logica.EntradaDatos import EntradaDatos
from logica.Consola.Trabajador import Trabajador
from logica.Consola.Usuario import Usuario
from logica.CalcBonifiDctos import CalcBonifiDctos
from logica.Bonificacion import Bonificacion
from logica.BoletaPago import BoletaPago
from logica.Consola.DetalleMensualTrabajador import DetalleMensualTrabajador
from logica.Consola.Mes import Mes

if __name__ == "__main__":

    def limpiar_pantalla():
        os.system('cls')


    def obtenerFechaActual():
        fechaHoraHoy = datetime.now()
        return fechaHoraHoy


    def obtenerHoraActual():
        horaNow = datetime.now()
        return horaNow


    def obtenerAtributosBonificaciones():
        global id1, tipo1, FactorHorasExtra
        global id2, tipo2, movilidad
        global id3, tipo3, factorBoniSuplementaria

        id1, tipo1, FactorHorasExtra = boniFactorHorasExtras.getBonificacion()
        id2, tipo2, movilidad = boniMovilidad.getBonificacion()
        id3, tipo3, factorBoniSuplementaria = boniFactorBoniSuplementaria.getBonificacion()


    def validarLoginUsuario(usernameIngresado, passwordIngresado):
        listaUsuarios = Usuario.listaUsuarios
        resultado_login = False
        global usuarioAceptado
        for usuario in listaUsuarios:
            if usernameIngresado == usuario.getUsername() and passwordIngresado == usuario.getPassword():
                resultado_login = True
                usuarioAceptado = usuario
                break
        return resultado_login


    global numBoletaPago
    numBoletaPago = 0

    # Ejemplo de creación de usuario
    usuarioJosue = Usuario("1", "1")

    # Ejemplo de creación de tres objetos de la clase Bonificacion
    boniFactorHorasExtras = Bonificacion(1, "Factor por horas extras", 0.2)
    boniMovilidad = Bonificacion(2, "Movilidad", 500.0)
    boniFactorBoniSuplementaria = Bonificacion(3, "Factor de bonificación suplementaria", 0.05)
    print("\nBONIFICACIONES INICIALES")
    Bonificacion.imprimirTablaBonificaciones()

    # Ejemplo de modificación de los valores de las bonificaciones
    obtenerAtributosBonificaciones()
    boniFactorHorasExtras.setBonificacion(id1, tipo1, 0.5)
    boniMovilidad.setBonificacion(id2, tipo2, 1000.0)
    boniFactorBoniSuplementaria.setBonificacion(id3, tipo3, 0.03)
    print("\nBONIFICACIONES ACTUALIZADAS")
    Bonificacion.imprimirTablaBonificaciones()

    # Creación de los objetos de la clase Mes
    nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
                     "Octubre", "Noviembre", "Diciembre"]

    for i, nombre_mes in enumerate(nombres_meses, start=1):
        mes = Mes(i, nombre_mes)

    # Ingreso al sistema
    menuInicial = True
    while menuInicial:
        print("\n===============SISTEMA GESTOR DE SUELDOS===============\n")
        print("1. Iniciar sesión\n")
        print("2. SALIR\n")
        op = EntradaDatos.validar_entero_positivo("Ingrese el número de opción: ",
                                                  "La opción no puede ser negativa")
        if op == 1:
            menuInicioSesion = True
            while menuInicioSesion:
                limpiar_pantalla()
                print("\n===============INICIO DE SESIÓN===============\n")
                print("Por favor ingresa tus credenciales de usuario\n")
                usernameIngresado, passwordIngresado = EntradaDatos.obtener_datos_usuario()
                resultado_login = validarLoginUsuario(usernameIngresado, passwordIngresado)

                if not resultado_login:
                    print("\nNombre de usuario o contraseña incorrectas, vuelva a ingresar sus credenciales")
                    input()
                else:
                    username = usuarioAceptado.getUsername()
                    password = usuarioAceptado.getPassword()
                    menuPrincipal = True
                    while menuPrincipal:
                        listaTrabajadores = Trabajador.listaTrabajadores
                        obtenerAtributosBonificaciones()
                        CalcBonifiDctos.inicializar_bonificaciones(FactorHorasExtra, movilidad, factorBoniSuplementaria)
                        limpiar_pantalla()
                        print(f"Bienvenido {username}!!!")
                        print("\n===============MENÚ PRINCIPAL===============\n")
                        print("1. Ingresar trabajadores\n")
                        print("2. Imprimir resultados\n")
                        print("3. Justificar faltas/tardanzas\n")
                        print("4. Actualizar bonificaciones\n")
                        print("5. Imprimir boleta de pago\n")
                        print("6. Cerrar sesión\n")

                        opc = EntradaDatos.validar_entero_positivo("Ingrese el número de opción: ",
                                                                   "La opción no puede ser negativa")
                        if opc == 1:
                            limpiar_pantalla()
                            print("---Ingrese los datos de un nuevo trabajador---\n")
                            nuevo_IdTrabajador, nuevo_nombre, nuevo_sueldoBasico, nuevo_diasFalta, nuevo_minutosTardanza, nuevo_horasExtras = \
                                EntradaDatos.obtener_datos_trabajador()
                            nuevo_trabajador = Trabajador(nuevo_IdTrabajador, nuevo_nombre, nuevo_sueldoBasico,
                                                          nuevo_diasFalta,
                                                          nuevo_minutosTardanza, nuevo_horasExtras)

                            # Cálculos de nuevo_trabajador
                            nuevo_trabajador.calcularBonificacion(nuevo_trabajador)
                            nuevo_trabajador.calcularDescuento(nuevo_trabajador)
                            nuevo_trabajador.calcularSueldoNeto()
                        elif opc == 2:
                            limpiar_pantalla()
                            print("---DATOS DEL USUARIO---")
                            usuarioAceptado.imprimir_atributos_usuario()
                            print("\n---DATOS DE LOS TRABAJADORES---\n")
                            for idx, trabajador in enumerate(listaTrabajadores, start=1):
                                print(f"→ Trabajador {idx}: ")
                                trabajador.imprimir_atributos_trabajador()
                                print()  # Espacio entre trabajadores
                            input()
                        elif opc == 3:
                            menuJustificaciones = True
                            while menuJustificaciones:
                                limpiar_pantalla()
                                print("\n---Justificar tardanzas y faltas---\n")
                                print("1. Ingresar el nombre del trabajador")
                                print("2. ←REGRESAR\n")

                                opcion = EntradaDatos.validar_entero_positivo("Ingrese el número de opción: ",
                                                                              "La opción no puede ser negativa")
                                if opcion == 1:
                                    trabajador_justificar = None
                                    nombre_busqueda = input("\nNombre a buscar: ")
                                    for trabajador in listaTrabajadores:
                                        if trabajador.nombreTrabajador == nombre_busqueda:
                                            trabajador_justificar = trabajador
                                            break
                                    if trabajador_justificar:
                                        print(f"Datos de : {trabajador_justificar.nombreTrabajador}")
                                        trabajador_justificar.imprimir_atributos_trabajador()
                                        while True:
                                            numFaltasJustificar = EntradaDatos.validar_entero_positivo(
                                                "\nNúmero de días de falta a justificar: ",
                                                "El número de faltas a justificar debe ser positivo")
                                            if (numFaltasJustificar > trabajador_justificar.diasFalta):
                                                print(
                                                    "El número de faltas a justicar debe ser menor a las faltas "
                                                    "actuales")
                                            else:
                                                trabajador_justificar.setDiasJustificados(numFaltasJustificar)
                                                trabajador_justificar.diasFalta -= numFaltasJustificar
                                                print(f"Días de falta actual: {trabajador_justificar.diasFalta}")
                                                break

                                        while True:
                                            minTardanzaJustificar = EntradaDatos.validar_entero_positivo(
                                                "\nMinutos de tardanza a justificar: ",
                                                "La cantidad de minutos de tardanza a justificar debe ser positiva")
                                            if (minTardanzaJustificar > trabajador_justificar.minutosTardanza):
                                                print(
                                                    "La cantidad de minutos de tardanza debe ser menor a los minutos "
                                                    "actuales")
                                            else:
                                                trabajador_justificar.setMinutosJustificados(minTardanzaJustificar)
                                                trabajador_justificar.minutosTardanza -= minTardanzaJustificar
                                                print(
                                                    f"Minutos de tardanza actual: {trabajador_justificar.minutosTardanza}")
                                                break
                                    else:
                                        print("Trabajador no encontrado...")
                                        input()
                                elif opcion == 2:
                                    menuJustificaciones = False
                                else:
                                    print("Opción inválida. Intente nuevamente.")
                                    input()
                        elif opc == 4:
                            menuActzrBonif = True
                            while menuActzrBonif:
                                limpiar_pantalla()
                                obtenerAtributosBonificaciones()
                                Bonificacion.imprimirTablaBonificaciones()
                                print("\n---Actualizar bonificaciones---")
                                print("1. Suplementaria")
                                print("2. Por movilidad")
                                print("3. Horas extra")
                                print("4. ←REGRESAR\n")

                                opcion = EntradaDatos.validar_entero_positivo("Ingrese el número de opción: ",
                                                                              "La opción no puede ser negativa")
                                if opcion == 1:
                                    print(f"\nFactor actual: {factorBoniSuplementaria}")
                                    nuevo_factorBoniSuplementaria = EntradaDatos.validar_numero_positivo(
                                        "Ingrese el nuevo Factor en formato "
                                        "decimal(ejem: 0.05): ",
                                        "El Factor no puede ser negativo")
                                    boniFactorBoniSuplementaria.setBonificacion(id3, tipo3,
                                                                                nuevo_factorBoniSuplementaria)
                                    print("Valor ingresado correctamente...")
                                    input()
                                elif opcion == 2:
                                    print(f"\nBonificación por movilidad actual: {movilidad}")
                                    nueva_movilidad = EntradaDatos.validar_numero_positivo(
                                        "Ingrese el nuevo valor de la "
                                        "bonificación "
                                        "por movilidad (soles): ",
                                        "la movilidad no puede ser negativa")
                                    boniMovilidad.setBonificacion(id2, tipo2, nueva_movilidad)
                                    print("Valor ingresado correctamente...")
                                    input()
                                elif opcion == 3:
                                    print(f"Factor de bonificación por horas extra: {FactorHorasExtra}")
                                    nuevo_FactorHoraExtra = EntradaDatos.validar_numero_positivo(
                                        "Ingrese el nuevo valor del factor de horas extra: ",
                                        "el factor de horas extra no puede ser negativo")
                                    boniFactorHorasExtras.setBonificacion(id2, tipo2, nuevo_FactorHoraExtra)
                                    print("Valor ingresado correctamente...")
                                    input()
                                elif opcion == 4:
                                    menuActzrBonif = False
                                else:
                                    print("Opción inválida. Intente nuevamente.")
                                    input()
                        elif opc == 5:
                            menuImprimirBoleta = True
                            while menuImprimirBoleta:
                                limpiar_pantalla()
                                print("\n---Imprimir boleta de pago---")
                                print("1. Buscar trabajador")
                                print("2. ←REGRESAR\n")

                                opcion = EntradaDatos.validar_entero_positivo("Ingrese el número de opción: ",
                                                                              "La opción no puede ser negativa")
                                if opcion == 1:
                                    trabajador_boletaImprimir = None
                                    nombre_busqueda = input("\nIngresar nombre del trabajador: ")
                                    for trabajador in listaTrabajadores:
                                        if trabajador.nombreTrabajador == nombre_busqueda:
                                            trabajador_boletaImprimir = trabajador
                                            break

                                    if trabajador_boletaImprimir:
                                        IdTrabajador, nombreTrabajador, sueldoBasico, diasFalta, minutosTardanza, horasExtras, \
                                        minutosJustificados, diasJustificados, pagoHorasExtras, movilidadTrabajador, bonificacionSuplementaria, \
                                        bonificacionTotal, remuneracionComputable, remuneracionMinima, descuentoFaltas, descuentoTardanzas, \
                                        descuentoTotal, sueldoNeto, sueldoNetoRedondeado = trabajador_boletaImprimir.getTrabajador()

                                        fechaHoraHoy = obtenerFechaActual()  # AAAA-MM-DD
                                        horaActual = obtenerHoraActual()  # Hora:Minuto:Segundo.Microsegundo
                                        IdMesActual, nombMesActual = Mes.obtenerMesActual()

                                        IdBoletaPago = BoletaPago.obtenerCodigoBoleta(IdTrabajador)
                                        nuevaBoletaPago = BoletaPago(IdBoletaPago, fechaHoraHoy, descuentoTotal,
                                                                     bonificacionTotal, sueldoNetoRedondeado)
                                        nuevoDetalleMensualTrabajor = DetalleMensualTrabajador(IdTrabajador,
                                                                                               IdMesActual, 2023,
                                                                                               horasExtras,
                                                                                               minutosTardanza,
                                                                                               minutosJustificados,
                                                                                               diasFalta,
                                                                                               diasJustificados,
                                                                                               sueldoNeto)

                                        print("\nBOLETA DE PAGO")
                                        nuevaBoletaPago.imprimirBoletaPago()

                                        print("\nDETALLE")
                                        nuevoDetalleMensualTrabajor.imprimirDetalleMensualTrabajador()

                                        input()
                                    else:
                                        print("Trabajador no encontrado...")
                                        input()
                                elif opcion == 2:
                                    menuImprimirBoleta = False
                                else:
                                    print("Opción inválida. Intente nuevamente.")
                                    input()
                        elif opc == 6:
                            menuPrincipal = False
                            menuInicioSesion = False
                        else:
                            print("Opción inválida. Intente nuevamente.")
                            input()
        elif op == 2:
            print("\nSaliendo del programa...\n\n")
            exit()
        else:
            print("Opción inválida. Intente nuevamente.")
            input()
