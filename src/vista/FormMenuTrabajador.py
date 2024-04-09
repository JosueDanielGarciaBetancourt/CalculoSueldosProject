import os
from sqlite3 import DatabaseError
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl, QTimer
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate, Qt, pyqtSignal
from src.vista.Window_Utils import MensajesWindow
from src.vista.Window_Utils import center, returnDirectorioGUI
from src.logica.Inserts import Inserts
from src.logica.Deletes import Deletes
from src.logica.Updates import Updates
from src.logica.Queries import Queries
from src.logica.CalculoSueldo import CalculoSueldo
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QHeaderView
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from src.logica.GeneradorPDF import GeneradorPDF
import sys


def excepthook(type, value, traceback):
    print(f"ERROR no detectado:\n{type}, {value}, {traceback}")


sys.excepthook = excepthook

directorio_ui = returnDirectorioGUI()


class FormMenuTrabajador:
    def __init__(self, parent):
        self.parent = parent
        self.MenuTrabajador = uic.loadUi(f"{directorio_ui}MenuTrabajador.ui")
        center(self.MenuTrabajador)
        self.initGUI()

    def mostrar(self):
        self.MenuTrabajador.show()

    def ocultar(self):
        self.MenuTrabajador.close()

    def deshabilitarBarraMenu(self):
        self.MenuTrabajador.menubarMenuTrabajador.setEnabled(False)

    def deshabilitarBotones(self):
        self.MenuTrabajador.pushButton_RegistrarNuevo.setEnabled(False)
        self.MenuTrabajador.pushButton_BuscarExistente.setEnabled(False)
        self.MenuTrabajador.pushButtonRegresar.setEnabled(False)

    def habilitarBarraMenu(self):
        self.MenuTrabajador.menubarMenuTrabajador.setEnabled(True)

    def habilitarBotones(self):
        self.MenuTrabajador.pushButton_RegistrarNuevo.setEnabled(True)
        self.MenuTrabajador.pushButton_BuscarExistente.setEnabled(True)
        self.MenuTrabajador.pushButtonRegresar.setEnabled(True)

    def salir(self):
        self.parent.deshabilitarLosBotones()
        self.parent.deshabilitarLaBarraMenu()
        self.parent.showMenuPrincipalSalir()

    def regresarMenuPrincipal(self):
        self.parent.showMenuPrincipal()

    def irMenuBonificacion(self):
        self.parent.showMenuBonificacion()

    def irMenuDetallesSW(self):
        self.parent.showMenuDetallesSW()

    def irRegistrarTrabajador(self):
        self.parent.showRegistrarNuevoTrabajador()

    def irBuscarTrabajador(self):
        self.parent.showBuscarExistenteTrabajador()

    def viewFormAcercaDeGestorDeSueldosV1(self):
        self.parent.deshabilitarLosBotones()
        self.parent.deshabilitarLaBarraMenu()
        self.parent.showFormAcercaDeGestorDeSueldosV1()

    def viewFormAcercaDeNosotros(self):
        self.parent.deshabilitarLosBotones()
        self.parent.deshabilitarLaBarraMenu()
        self.parent.showFormAcercaDeNosotros()

    def initGUI(self):
        # Botones
        self.MenuTrabajador.pushButtonRegresar.clicked.connect(self.regresarMenuPrincipal)
        self.MenuTrabajador.pushButton_RegistrarNuevo.clicked.connect(self.irRegistrarTrabajador)
        self.MenuTrabajador.pushButton_BuscarExistente.clicked.connect(self.irBuscarTrabajador)

        # Menubar
        self.MenuTrabajador.actionInicio.triggered.connect(self.regresarMenuPrincipal)
        self.MenuTrabajador.actionBonificaciones.triggered.connect(self.irMenuBonificacion)
        self.MenuTrabajador.actionAcercaDeGestorDeSueldosV1.triggered.connect(self.viewFormAcercaDeGestorDeSueldosV1)
        self.MenuTrabajador.actionAcercaDeNosotros.triggered.connect(self.viewFormAcercaDeNosotros)
        self.MenuTrabajador.actionSalir.triggered.connect(self.salir)


class FormRegistrarNuevoTrabajador:
    def __init__(self, parent):
        self.parent = parent
        self.RegistrarNuevoTrabajador = uic.loadUi(f"{directorio_ui}\\TrabajadorRegistrar.ui")
        center(self.RegistrarNuevoTrabajador)
        self.initGUI()

    def mostrar(self):
        self.RegistrarNuevoTrabajador.show()

    def ocultar(self):
        self.RegistrarNuevoTrabajador.close()

    def registrar(self):
        try:
            DNI = self.RegistrarNuevoTrabajador.inputDNI.text()
            ApellidosNombres = self.RegistrarNuevoTrabajador.inputNombres.text()
            SueldoBase = self.RegistrarNuevoTrabajador.inputSueldoBasico.text()
            Cargo = self.RegistrarNuevoTrabajador.inputCargo.text()

            # Validar campos vacíos y otras condiciones
            campos_vacios = []

            if DNI.strip() == "":
                campos_vacios.append("DNI")
            elif not DNI.isdigit() or len(DNI) != 8:
                MensajesWindow.mostrarMensajeRegistroError("El DNI debe contener 8 cifras numéricas")
                return

            if ApellidosNombres.strip() == "":
                campos_vacios.append("Apellidos y Nombres")
            elif len(ApellidosNombres) > 50:
                MensajesWindow.mostrarMensajeRegistroError("El campo 'Apellidos y Nombres' no puede tener más de 50 "
                                                           "caracteres.Por favor, ingrese una información más corta.")
                return

            if Cargo.strip() == "":
                campos_vacios.append("Cargo")
            elif len(Cargo) > 100:
                MensajesWindow.mostrarMensajeRegistroError("El campo 'Cargo' no puede tener más de 100 caracteres."
                                                           "Por favor, ingrese un cargo más corto.")
                return

            if SueldoBase.strip() == "":
                campos_vacios.append("Sueldo Básico")
            else:
                try:
                    SueldoBase = float(SueldoBase)
                    if SueldoBase > 15000:
                        MensajesWindow.mostrarMensajeRegistroError("El Sueldo Básico no debe ser mayor a 15000.00")
                        return
                except ValueError:
                    MensajesWindow.mostrarMensajeRegistroError("El campo 'Sueldo Básico' debe contener un número")
                    return

            if campos_vacios:
                if len(campos_vacios) == 1:
                    mensaje = f"El campo {''.join(campos_vacios)} está vacío"
                else:
                    mensaje = f"Los campos: {', '.join(campos_vacios)} están vacíos"
                MensajesWindow.mostrarMensajeRegistroError(mensaje)
            else:
                Inserts.insertTrabajador(DNI, ApellidosNombres, SueldoBase, Cargo)
        except Exception as e:
            MensajesWindow.mostrarError("Error inesperado",
                                        f"Surgió un error al registrar trabajador: {e}")
            print(f"Surgió un error al registrar trabajador: {e}")

    def cancelar(self):
        self.parent.showMenuTrabajador()

    def initGUI(self):
        # botones
        self.RegistrarNuevoTrabajador.pushButton_Registrar.clicked.connect(self.registrar)
        self.RegistrarNuevoTrabajador.pushButton_Cancelar.clicked.connect(self.cancelar)
        self.RegistrarNuevoTrabajador.dateEditFechaActual.setDate(QDate.currentDate())


class FormBuscarExistenteTrabajador:
    def __init__(self, parent):
        self.parent = parent
        self.BuscarExistenteTrabajador = uic.loadUi(f"{directorio_ui}\\TrabajadorBuscar.ui")
        center(self.BuscarExistenteTrabajador)
        self.initGUI()

    def mostrar(self):
        self.BuscarExistenteTrabajador.show()

    def ocultar(self):
        self.BuscarExistenteTrabajador.close()

    def regresar(self):
        self.parent.showMenuTrabajador()

    def mostrarGUITableTrabajadoresBuscados(self, trabajadoresBuscados):
        # Limpiar la tabla antes de llenarla para evitar duplicados
        self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.setRowCount(0)
        # Llenar la tabla con los trabajadores
        for row, trabajador in enumerate(trabajadoresBuscados):
            self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.insertRow(row)
            self.fillRowGUITableTrabajadores(row, trabajador)

    def buscarTrabajador_by_ID_nombre(self):
        try:
            busquedaDNI_Nombre = self.BuscarExistenteTrabajador.lineEditDNIBuscar.text()

            if busquedaDNI_Nombre.strip() == "":
                self.actualizarGUITableAllTrabajadores()
                MensajesWindow.mostrarMensajeBusquedaError("Por favor ingrese el DNI/Nombre del trabajador a buscar")
            elif busquedaDNI_Nombre.isdigit():
                if len(busquedaDNI_Nombre) > 8:
                    MensajesWindow.mostrarMensajeBusquedaError("El DNI ingresado debe contener 8 cifras numéricas "
                                                               "como máximo")
                else:
                    trabajadoresBuscados_by_DNI = Queries.get_trabajadores_by_idPrefijo(busquedaDNI_Nombre)
                    print(trabajadoresBuscados_by_DNI)
                    if not trabajadoresBuscados_by_DNI:
                        MensajesWindow.mostrarMensajeBusquedaError(
                            f"No existen trabajadores con DNI: {busquedaDNI_Nombre}")
                    else:
                        self.mostrarGUITableTrabajadoresBuscados(trabajadoresBuscados_by_DNI)
            elif not busquedaDNI_Nombre.isdigit():
                if len(busquedaDNI_Nombre) > 60:
                    MensajesWindow.mostrarMensajeBusquedaError("El nombre ingresado no puede sobrepasar el límite de "
                                                               "60 caracteres. Por favor ingresa un nombre más corto")
                else:
                    trabajadoresBuscados_by_name = Queries.get_trabajadores_by_namePrefijo(busquedaDNI_Nombre)
                    print(trabajadoresBuscados_by_name)
                    if not trabajadoresBuscados_by_name:
                        MensajesWindow.mostrarMensajeBusquedaError(
                            f"No existen trabajadores con Nombre: {busquedaDNI_Nombre}")
                    else:
                        self.mostrarGUITableTrabajadoresBuscados(trabajadoresBuscados_by_name)
            else:
                MensajesWindow.mostrarMensajeBusquedaError(
                    f"No existen trabajadores con DNI/Nombre: {busquedaDNI_Nombre}")
        except ValueError as ve:
            print(f"Error de valor al buscar el trabajador: {ve}")
        except SQLAlchemyError as sae:
            print(f"Error de SQLAlchemy al buscar el trabajador: {sae}")
        except DatabaseError as de:
            print(f"Error de base de datos al buscar el trabajador: {de}")
        except Exception as e:
            print(f"Ocurrió un error inesperado al buscar el trabajador: {e}")

    def fillRowGUITableTrabajadores(self, row, trabajador):
        # Crear items para cada columna y convertirlos a cadena para mostrarlos en la tabla
        id_item = QTableWidgetItem(str(trabajador.IDTrabajador))
        nombre_item = QTableWidgetItem(str(trabajador.trabNombreApellidos))
        cargo_item = QTableWidgetItem(str(trabajador.trabCargo))
        sueldo_item = QTableWidgetItem(str(trabajador.trabSueldoBase))
        fecha_creacion_item = QTableWidgetItem(str(trabajador.created_at))

        # Establecer los items en la fila de la tabla
        self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.setItem(row, 0, id_item)
        self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.setItem(row, 1, nombre_item)
        self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.setItem(row, 2, cargo_item)
        self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.setItem(row, 3, sueldo_item)
        self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.setItem(row, 4, fecha_creacion_item)

    def actualizarGUITableAllTrabajadores(self):
        todos_los_trabajadores = Queries.get_all_trabajadores()
        # Limpiar la tabla antes de llenarla para evitar duplicados
        self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.setRowCount(0)

        # Llenar la tabla con los trabajadores
        for row, trabajador in enumerate(todos_los_trabajadores):
            self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.insertRow(row)
            self.fillRowGUITableTrabajadores(row, trabajador)

    def returnRowDNISelected(self):
        try:
            seleccionado = False
            selectedRow = None
            selectedDNI = ""
            # Obtiene el modelo de selección de la tabla
            selection_model = self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.selectionModel()
            # Verifica si hay alguna celda seleccionada en el modelo de selección
            if selection_model.hasSelection():
                seleccionado = True
                selectedRow = self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.currentRow()
                selectedDNI = self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.item(selectedRow, 0).text()
            return seleccionado, selectedRow, selectedDNI
        except Exception as e:
            print(e)

    def deleteRowGUITableTrabajador(self):
        seleccionado, selectedRow, selectedDNI = self.returnRowDNISelected()
        if seleccionado:
            confirmacionEliminar = MensajesWindow.mostrarMensajeConfirmacion("Confirmación de eliminación",
                                                                             f"Se eliminará el trabajador con DNI {selectedDNI}. "
                                                                             f"¿Está seguro de eliminarlo?",
                                                                             QMessageBox.Icon.Question)
            if confirmacionEliminar == "Sí":
                try:
                    # Eliminar fila seleccionada de la tabla
                    self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.removeRow(selectedRow)
                    # Eliminar trabajador seleccionado de la BD
                    Deletes.deleteTrabajador(selectedDNI)
                    MensajesWindow.mostrarMensajeEliminarExito(f"Se eliminó el trabajador con DNI: {selectedDNI}")
                except Exception as e:
                    mensaje = f"Error inesperado al eliminar trabajador: {e}"
                    print(mensaje)
                    MensajesWindow.mostrarMensajeEliminarError(mensaje)
        else:
            MensajesWindow.mostrarMensajeEliminarError("No se seleccionó trabajador. "
                                                       "Por favor seleccione un trabajador para eliminarlo")

    def inspectRowGUITableTrabajador(self):
        seleccionado, selectedRow, selectedDNI = self.returnRowDNISelected()
        if seleccionado:
            try:
                trabajador = Queries.get_trabajador_by_id(selectedDNI)
                MensajesWindow.mostrarMensajeBusquedaExito(
                    f"Trabajador a inspeccionar: {trabajador.IDTrabajador} {trabajador.trabNombreApellidos}")
                print(f"Trabajador a inspeccionar: {trabajador.IDTrabajador}")
                self.parent.showInspeccionarTrabajador(trabajador)
            except Exception as e:
                mensaje = f"Ocurrió el siguiente error inesperado al inspeccionar trabajador: {e}"
                print(mensaje)
                MensajesWindow.mostrarMensajeErrorInesperado(mensaje)
        else:
            MensajesWindow.mostrarMensajeEliminarError("No se seleccionó trabajador. "
                                                       "Por favor seleccione un trabajador a inspeccionar")

    def deseleccionarTabla(self):
        self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.clearSelection()

    def initGUI(self):
        # Botones
        self.BuscarExistenteTrabajador.pushButtonRegresar.clicked.connect(self.regresar)
        self.BuscarExistenteTrabajador.pushButtonEliminarTrabajador.clicked.connect(self.deleteRowGUITableTrabajador)
        self.BuscarExistenteTrabajador.pushButtonInspeccionarTrabajador.clicked.connect(
            self.inspectRowGUITableTrabajador)

        self.BuscarExistenteTrabajador.dateEditFechaActual.setDate(QDate.currentDate())
        self.BuscarExistenteTrabajador.lineEditDNIBuscar.returnPressed.connect(self.buscarTrabajador_by_ID_nombre)

        # Tabla trabajadores GUI
        ancho_maximo = 1040
        num_columnas = 5
        # Calcular el ancho de cada columna
        ancho_columna = int(ancho_maximo / num_columnas)
        # Establecer el ancho de cada columna
        for col in range(num_columnas):
            self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.setColumnWidth(col, ancho_columna)

        self.actualizarGUITableAllTrabajadores()
        Inserts.signal.trabajadorInserted.connect(self.actualizarGUITableAllTrabajadores)
        Deletes.signal.trabajadorDeleted.connect(self.actualizarGUITableAllTrabajadores)
        self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)


class FormInspeccionarTrabajador:
    def __init__(self, parent):
        self.ruta_absoluta = ""
        self.detalle_calculo_sueldo = None
        self.IDDetalleCalculoSueldo = ""
        self.parent = parent
        self.listaDetallesMensuales = []
        self.mes_seleccionado_Obj = None
        self.numMesSelec = None
        self.IDMesSelec = ""
        self.numBoleta = 0
        self.detalleMensual = None
        self.registroDetalleMensualObj = None
        self.calcularSueldoTrabObj = None

        self.fecha_hora_actual = datetime.now()
        self.anio_actual = self.fecha_hora_actual.year
        self.mes_actual = "{:02d}".format(
            self.fecha_hora_actual.month)  # Se obtiene el número de mes actual con un 0 al inicio de ser necesario
        self.fecha_hora_simulada = None
        self.IDMes_actual = "MES" + self.mes_actual
        self.mes_actual_Obj = None

        self.boniHorasExtra = Queries.get_bonificacion_by_id("BONI01")
        self.valorHorasExtra = self.boniHorasExtra.bonValor
        self.boniMovilidad = Queries.get_bonificacion_by_id("BONI02")
        self.valorMovilidad = self.boniMovilidad.bonValor
        self.boniSuplementaria = Queries.get_bonificacion_by_id("BONI03")
        self.valorSuplementaria = self.boniSuplementaria.bonValor

        self.totalDctos = None
        self.totalBonificaciones = None

        self.trabajador = None
        self.IDTrabajador = ""
        self.nombresApellidos = ""
        self.cargo = ""
        self.sueldoBase = 0
        self.created_at = ""

        self.horasExtras = 0
        self.minutosTardanzas = 0
        self.minutosJustificados = 0
        self.diasFalta = 0
        self.diasJustificados = 0
        self.sueldoNeto = 0

        self.InspeccionarTrabajador = uic.loadUi(f"{directorio_ui}\\TrabajadorInspeccionar.ui")
        center(self.InspeccionarTrabajador)
        self.InspeccionarTrabajador.tablaResumen.cellClicked.connect(self.toggleRowSelectionTablaResumen)
        self.InspeccionarTrabajador.tablaDetallada.cellClicked.connect(self.toggleRowSelectionTablaDetallada)
        self.InspeccionarTrabajador.tablaHistorialPagos.cellClicked.connect(self.toggleRowSelectionTablaHistorialPagos)
        self.lastClickedRowResumen = None
        self.lastClickedRowDetallada= None
        self.lastClickedRowHistorialPagos = None
        self.lastClickedColumnHistorialPagos = None
        self.initGUI()

    def toggleRowSelectionTablaResumen(self, row, column):
        if row == self.lastClickedRowResumen:
            self.InspeccionarTrabajador.tablaResumen.clearSelection()
            self.lastClickedRowResumen = None
            print("Limpiar selección")
        else:
            self.lastClickedRowResumen = row
            print("Seleccionar fila")

    def toggleRowSelectionTablaDetallada(self, row, column):
        if row == self.lastClickedRowDetallada:
            self.InspeccionarTrabajador.tablaDetallada.clearSelection()
            self.lastClickedRowDetallada = None
            print("Limpiar selección")
        else:
            self.lastClickedRowDetallada = row
            print("Seleccionar fila")

    def toggleRowSelectionTablaHistorialPagos(self, row, column):
        if row == self.lastClickedRowHistorialPagos and column == self.lastClickedColumnHistorialPagos:
            self.InspeccionarTrabajador.tablaHistorialPagos.clearSelection()
            self.lastClickedRowHistorialPagos = None
            self.lastClickedColumnHistorialPagos = None
            print("Limpiar selección")
        else:
            self.lastClickedRowHistorialPagos = row
            self.lastClickedColumnHistorialPagos = column
            print("Seleccionar fila")

            if column == 4:
                # Obtiene la fila y el ID de la boleta de pago desde la tabla
                idBoletaPago = self.InspeccionarTrabajador.tablaHistorialPagos.item(row, 2).text()

                # Genera el nombre de archivo PDF correspondiente
                ruta_pdf = os.path.abspath(f'otros_recursos\\Comprobantes de pago generados\\{idBoletaPago}.pdf')

                # Abre el archivo PDF
                self.open_file(ruta_pdf)

    def actualizarTrabajador(self, trabajador_actual):
        try:
            if trabajador_actual:
                self.trabajador = trabajador_actual
                self.IDTrabajador = self.trabajador.IDTrabajador
                self.nombresApellidos = self.trabajador.trabNombreApellidos
                self.cargo = self.trabajador.trabCargo
                self.sueldoBase = self.trabajador.trabSueldoBase
                self.created_at = self.trabajador.created_at
                self.actualizarDetalleMensual()
            else:
                print("No se encontró trabajador para actualizar self.trabajador")
        except Exception as e:
            print(f"Error inesperado al inspeccionar trabajador (actualizar obj trabajador): {e}")

    def actualizarDetalleMensual(self):
        try:
            # Vaciar todas las tablas
            self.InspeccionarTrabajador.tablaResumen.clearContents()
            self.InspeccionarTrabajador.tablaDetallada.clearContents()
            self.InspeccionarTrabajador.tablaHistorialPagos.clearContents()

            self.listaDetallesMensuales = Queries.get_all_detalle_mensual_trabajador_by_id(self.IDTrabajador)
            
            if self.listaDetallesMensuales is None or not self.listaDetallesMensuales:
                print(f"Aún no se registró algún detalle mensual del trabajador con ID {self.IDTrabajador} en "
                      f"la lista detalles.")
            else:
                for detalleMensualRegistrado in self.listaDetallesMensuales:
                    # Actualizar detalles
                    self.detalleMensual = detalleMensualRegistrado
                    self.mes_seleccionado_Obj = Queries.get_mes_by_id(self.detalleMensual.IDMes)
                    self.detalle_calculo_sueldo = Queries.get_detalle_calculo_sueldo_by_id(
                        self.detalleMensual.IDTrabajador,
                        self.detalleMensual.IDMes)
                    # Rellenar las tablas para cada detalle registrado
                    numMesRegistrado = self.obtenerNumMes(self.mes_seleccionado_Obj.mesNombre)
                    self.fillRowGUITablaResumen(numMesRegistrado - 1)
                    self.fillRowGUITablaDetallada(numMesRegistrado - 1)

                print("Lista de detalles mensuales registrados:")
                num = 0
                for detalle in self.listaDetallesMensuales:
                    num += 1
                    print(f"{num} → {detalle.IDTrabajador}, {detalle.IDMes}")
        except Exception as e:
            print(f"ActualizarDetalleMensual(def). Error inesperado al actualizar detalle mensual: {e}")

    def mostrar(self):
        # Inicializar etiquetas con la información del trabajador
        self.InspeccionarTrabajador.labelDNI.setText(self.IDTrabajador)
        self.InspeccionarTrabajador.labelApeNomb.setText(self.nombresApellidos)
        self.InspeccionarTrabajador.labelCargo.setText(self.cargo)
        self.InspeccionarTrabajador.labelSueldoBase.setText(str(self.sueldoBase))
        self.InspeccionarTrabajador.labelFechaCreacion.setText(str(self.created_at))
        self.InspeccionarTrabajador.show()

    def irFormRegistroDetalleMensual(self):
        nombMes = self.InspeccionarTrabajador.comboBoxSimularMes.currentText()
        self.registroDetalleMensualObj = FormRegistroDetalleMensual(self, nombMes)
        self.registroDetalleMensualObj.mostrar()

    def fillRowGUITablaResumen(self, row):
        self.detalle_calculo_sueldo = Queries.get_detalle_calculo_sueldo_by_id(self.IDTrabajador, self.IDMesSelec)
        print(f"Tabla resumen. Detalle calculo sueldo: {self.detalle_calculo_sueldo}")

        self.detalleMensual = Queries.get_detalle_mensual_trabajador_by_id(self.IDTrabajador, self.IDMesSelec)
        print(f"\nTabla resumen. Detalle mensual: {self.detalleMensual}")

        try:
            mes_nombre_item = QTableWidgetItem(str(self.mes_seleccionado_Obj.mesNombre))
            fecha_hora_item = QTableWidgetItem(str(self.detalleMensual.detalleFecha))
            sueldo_base_item = QTableWidgetItem(str(self.trabajador.trabSueldoBase))
            totalBonificaciones_item = QTableWidgetItem(str(self.detalle_calculo_sueldo.calcSueldoTotalBonificaciones))
            totalDescuentos_item = QTableWidgetItem(str(self.detalle_calculo_sueldo.calcSueldoTotalDctos))
            sueldoNeto_item = QTableWidgetItem(str(self.detalleMensual.detalleSueldoNeto))

            """print("\nMes Nombre:", self.mes_seleccionado_Obj.mesNombre)
            print("Fecha y Hora:", self.detalleMensual.detalleFecha.strftime("%Y-%m-%d %H:%M:%S"))
            print("Sueldo Base:", self.trabajador.trabSueldoBase)
            print("Total Bonificaciones:", self.bonificaciones)
            print("Total Descuentos:", self.descuentos)
            print("Sueldo Neto:", self.sueldoNeto)"""

            listaItems = [mes_nombre_item, fecha_hora_item, sueldo_base_item, totalBonificaciones_item,
                          totalDescuentos_item, sueldoNeto_item]
            for item in listaItems:
                item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

            # Establecer los items en la fila de la tabla
            self.InspeccionarTrabajador.tablaResumen.setItem(row, 0, mes_nombre_item)
            self.InspeccionarTrabajador.tablaResumen.setItem(row, 1, fecha_hora_item)
            self.InspeccionarTrabajador.tablaResumen.setItem(row, 2, sueldo_base_item)
            self.InspeccionarTrabajador.tablaResumen.setItem(row, 3, totalBonificaciones_item)
            self.InspeccionarTrabajador.tablaResumen.setItem(row, 4, totalDescuentos_item)
            self.InspeccionarTrabajador.tablaResumen.setItem(row, 5, sueldoNeto_item)
        except Exception as e:
            print(f"Error inesperado al llenar la tabla resumen: {e}")

    def fillRowGUITablaDetallada(self, row):

        self.detalleMensual = Queries.get_detalle_mensual_trabajador_by_id(self.IDTrabajador, self.IDMesSelec)
        print(f"\nTabla detallada. Detalle mensual: {self.detalleMensual}")

        self.detalle_calculo_sueldo = Queries.get_detalle_calculo_sueldo_by_id(self.IDTrabajador, self.IDMesSelec)
        print(f"Tabla detallada. Detalle calculo sueldo: {self.detalle_calculo_sueldo}")

        try:
            # Crear items para cada columna y convertirlos a cadena para mostrarlos en la tabla
            mes_nombre_item = QTableWidgetItem(str(self.mes_seleccionado_Obj.mesNombre))
            fecha_hora_item = QTableWidgetItem(str(self.detalleMensual.detalleFecha))
            apell_nomb_item = QTableWidgetItem(str(self.trabajador.trabNombreApellidos))
            min_tardanza_item = QTableWidgetItem(str(self.detalleMensual.detalleMinutosTardanzas))
            dias_falta_item = QTableWidgetItem(str(self.detalleMensual.detalleDiasFalta))
            min_justificados_item = QTableWidgetItem(str(self.detalleMensual.detalleMinutosJustificados))
            dias_justificados_item = QTableWidgetItem(str(self.detalleMensual.detalleDiasJustificados))
            horas_extras_item = QTableWidgetItem(str(self.detalleMensual.detalleHorasExtras))
            total_movilidad = QTableWidgetItem(str(self.detalle_calculo_sueldo.calcSueldoMontoMovilidad))
            total_suplementario = QTableWidgetItem(str(self.detalle_calculo_sueldo.calcSueldoMontoSuplementario))
            total_horaExtra = QTableWidgetItem(str(self.detalle_calculo_sueldo.calcSueldoMontoHorasExtras))
            monto_remunComputable = QTableWidgetItem(str(self.detalle_calculo_sueldo.calcSueldoMontoRemunComputable))
            monto_dctoFaltas = QTableWidgetItem(str(round(self.detalle_calculo_sueldo.calcSueldoMontoDctoFalta, 2)))
            monto_dctoTardanzas = QTableWidgetItem(
                str(round(self.detalle_calculo_sueldo.calcSueldoMontoDctoTardanzas, 2)))
            sueldo_base_item = QTableWidgetItem(str(self.trabajador.trabSueldoBase))
            totalBonificaciones_item = QTableWidgetItem(str(self.detalle_calculo_sueldo.calcSueldoTotalBonificaciones))
            totalDescuentos_item = QTableWidgetItem(str(self.detalle_calculo_sueldo.calcSueldoTotalDctos))
            sueldoNeto_item = QTableWidgetItem(str(self.detalleMensual.detalleSueldoNeto))

            listaItems = [mes_nombre_item, fecha_hora_item, apell_nomb_item, min_tardanza_item,
                          dias_falta_item, min_justificados_item, dias_justificados_item,
                          horas_extras_item, total_movilidad, total_suplementario, total_horaExtra,
                          monto_remunComputable, monto_dctoFaltas, monto_dctoTardanzas,
                          sueldo_base_item, totalBonificaciones_item, totalDescuentos_item,
                          sueldoNeto_item]

            for item in listaItems:
                item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

            # Establecer los items en la fila de la tabla
            for col, item in enumerate(listaItems):
                self.InspeccionarTrabajador.tablaDetallada.setItem(row, col, item)
        except Exception as e:
            print(f"Error inesperado al llenar la tabla detallada: {e}")

    def fillRowGUITablaHistorialPagos(self, row, idBoletaPago):
        try:
            # Crear items para cada columna y convertirlos a cadena para mostrarlos en la tabla
            mesPago_item = QTableWidgetItem(str(self.mes_seleccionado_Obj.mesNombre))
            fechaHoraPago_item = QTableWidgetItem(str(self.detalleMensual.detalleFecha))
            idBoletaPago_item = QTableWidgetItem(str(idBoletaPago))
            sueldoNeto_item = QTableWidgetItem(str(self.sueldoNeto))
            enlace_item = QTableWidgetItem(str("Click aquí"))

            listaItems = [mesPago_item, fechaHoraPago_item, idBoletaPago_item, sueldoNeto_item, enlace_item]

            for item in listaItems:
                item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

            print("FILAAAAA: ", row)
            # Establecer los items en la fila de la tabla
            for col, item in enumerate(listaItems):
                self.InspeccionarTrabajador.tablaHistorialPagos.setItem(row, col, item)
        except Exception as e:
            print(f"Error inesperado al llenar la tabla resumen: {e}")

    @staticmethod
    def obtenerNumMes(nombMes):
        try:
            meses = {
                "enero": 1,
                "febrero": 2,
                "marzo": 3,
                "abril": 4,
                "mayo": 5,
                "junio": 6,
                "julio": 7,
                "agosto": 8,
                "septiembre": 9,
                "octubre": 10,
                "noviembre": 11,
                "diciembre": 12
            }
            # Convertir a minúsculas antes de buscar en el diccionario
            nombMes = nombMes.lower()
            return meses.get(nombMes, 0)  # 0 es el valor por default
        except Exception as e:
            print(f"Error inesperado durante el registro del mes ingresado: {e}")

    def obtenerDetalles(self, horasExtras, minTardanza, diasFaltados, nombMesSelec):
        try:
            if self.trabajador:
                self.horasExtras = float(horasExtras)
                self.minutosTardanzas = float(minTardanza)
                self.diasFalta = float(diasFaltados)
                self.numMesSelec = self.obtenerNumMes(str(nombMesSelec))
                self.IDMesSelec = "MES" + "{:02d}".format(self.numMesSelec)
                self.mes_seleccionado_Obj = Queries.get_mes_by_id(self.IDMesSelec)
                self.registrarDetalleMensual()
            else:
                print("No existe trabajador para continuar con la obtención de detalles")
        except Exception as e:
            print(f"Error inesperado al obtener detalles: {e}")

    def registrarDetalleMensual(self):
        # En este caso se registrarán manualmante los detalles mensuales del trabajador
        # debido a que no se cuenta con otro módulo de donde se pueda obtener los días de falta,
        # minutos de tardanza y horas extra de manera automática
        try:
            self.calcularDetallesSueldo()

            if self.detalle_calculo_sueldo:
                self.detalleMensual = Queries.get_detalle_mensual_trabajador_by_id(self.IDTrabajador, self.IDMesSelec)

                # Almacenar en la BD
                if self.detalleMensual:
                    Updates.updateDetalleMensualTrabajador(self.IDTrabajador, self.IDMesSelec,
                                                           self.IDDetalleCalculoSueldo,
                                                           self.horasExtras, self.minutosTardanzas,
                                                           self.minutosJustificados,
                                                           self.diasFalta, self.diasJustificados, self.sueldoNeto)
                else:
                    Inserts.insertDetalleMensualTrabajador(self.IDTrabajador, self.IDMesSelec,
                                                           self.IDDetalleCalculoSueldo,
                                                           self.horasExtras, self.minutosTardanzas,
                                                           self.minutosJustificados,
                                                           self.diasFalta, self.diasJustificados, self.sueldoNeto)

                self.listaDetallesMensuales.append(self.detalleMensual)

                # Imprimir en consola
                print("\nDETALLE MENSUAL")
                print(f"ID trabajador: {self.IDTrabajador}\n"
                      f"ID mes: {self.IDMesSelec}\n"
                      f"Año: {self.anio_actual}\n"
                      f"Horas Extras: {self.horasExtras}\n"
                      f"Minutos de tardanza: {self.minutosTardanzas}\n"
                      f"Minutos justificados: {self.minutosJustificados}\n"
                      f"Días de falta: {self.diasFalta}\n"
                      f"Días justificados: {self.diasJustificados}\n"
                      f"Sueldo Neto: {self.sueldoNeto}\n"
                      f"Fecha y hora: {self.fecha_hora_actual}\n")

                # Almacenar en las tablas de la GUI
                # Tabla resumen
                self.fillRowGUITablaResumen(int(self.numMesSelec) - 1)
                # Tabla detallada
                self.fillRowGUITablaDetallada(int(self.numMesSelec) - 1)
            else:
                print(
                    f"Registrar detalle mensual. No se encontró detalle del cálculo de sueldo: {self.detalle_calculo_sueldo:}")
        except Exception as e:
            print(f"Error inesperado al registrar el detalle mensual: {e}")

    def calcularDetallesSueldo(self):
        try:
            print("Calculando sueldo")
            self.calcularSueldoTrabObj = CalculoSueldo(
                self.sueldoBase, self.horasExtras, self.diasFalta, self.minutosTardanzas,
                self.valorHorasExtra, self.valorMovilidad, self.valorSuplementaria)

            self.totalBonificaciones = self.calcularSueldoTrabObj.calcularBonificaciones()
            self.totalDctos = self.calcularSueldoTrabObj.calcularDescuentos()
            self.sueldoNeto = self.calcularSueldoTrabObj.calcularSueldoNeto()

            self.detalle_calculo_sueldo = Queries.get_detalle_calculo_sueldo_by_id(self.IDTrabajador, self.IDMesSelec)

            self.IDDetalleCalculoSueldo = str(self.IDTrabajador + self.IDMesSelec)

            if self.detalle_calculo_sueldo:
                Updates.updateDetalleCalculoSueldo(self.IDTrabajador, self.IDMesSelec, self.IDDetalleCalculoSueldo,
                                                   self.calcularSueldoTrabObj.montoMovilidad,
                                                   self.calcularSueldoTrabObj.totalSuplementaria,
                                                   self.calcularSueldoTrabObj.totalHorasExtra,
                                                   self.calcularSueldoTrabObj.remuneracionComputable,
                                                   self.calcularSueldoTrabObj.DescuentoFaltas,
                                                   self.calcularSueldoTrabObj.DescuentoTardanzas,
                                                   self.calcularSueldoTrabObj.bonificacionesTotal,
                                                   self.calcularSueldoTrabObj.descuentosTotal)
            else:
                Inserts.insertDetalleCalculoSueldo(self.IDTrabajador, self.IDMesSelec, self.IDDetalleCalculoSueldo,
                                                   self.calcularSueldoTrabObj.montoMovilidad,
                                                   self.calcularSueldoTrabObj.totalSuplementaria,
                                                   self.calcularSueldoTrabObj.totalHorasExtra,
                                                   self.calcularSueldoTrabObj.remuneracionComputable,
                                                   self.calcularSueldoTrabObj.DescuentoFaltas,
                                                   self.calcularSueldoTrabObj.DescuentoTardanzas,
                                                   self.calcularSueldoTrabObj.bonificacionesTotal,
                                                   self.calcularSueldoTrabObj.descuentosTotal)

            self.detalle_calculo_sueldo = Queries.get_detalle_calculo_sueldo_by_id(self.IDTrabajador, self.IDMesSelec)

            print(f"Detalle calculo sueldo: {self.detalle_calculo_sueldo}")
            print(f"El sueldo base es: {self.sueldoBase}")
            print(f"El monto de bonificaciones es: {self.totalBonificaciones}")
            print(f"El monto de descuentos es: {self.totalDctos}")
            print(f"El sueldo NETO es: {self.sueldoNeto}\n")
        except Exception as e:
            print(f"Error al calcular el sueldo: {e}")

    def generarIDBoletaPago(self, anio, numMes):
        try:
            self.numBoleta = self.numBoleta + 1
            idBoleta = f"BOLE{self.IDTrabajador}-{anio}{numMes:02d}-{self.numBoleta:03d}"
            return idBoleta
        except Exception as e:
            print(f"Ocurrió un error inesperado al generar el ID de la nueva boleta de pago: {e}")

    def generarPDF(self, idBoleta):
        boleta_obj = Queries.get_boleta_pago_by_id(idBoleta)
        self.ruta_absoluta = os.path.abspath(f'otros_recursos\\Comprobantes de pago generados\\{idBoleta}.pdf')
        GeneradorPDF.generar_pdf_comprobante_pago(boleta_obj, self.ruta_absoluta)
        self.open_file(self.ruta_absoluta)

    @staticmethod
    def open_file(path):
        try:
            ruta_archivo = path  # Reemplaza con la ruta de tu archivo
            with open(ruta_archivo, 'r') as archivo:
                contenido = archivo.read()

            # Abre el archivo PDF en el visor predeterminado del sistema
            QDesktopServices.openUrl(QUrl.fromLocalFile(ruta_archivo))
        except FileNotFoundError:
            print(f"El archivo en la ruta '{ruta_archivo}' no fue encontrado.")
            return None  # Puedes devolver None o algún otro valor que indique que el archivo no fue encontrado
        except Exception as e:
            print(f"Ocurrió un error al abrir archivo: {e}")
            return None  # Puedes devolver None o algún otro valor que indique un error

    def returnRowDatetimeSelected(self):
        try:
            selected = False
            selectedDatetime = ""

            # Obtiene el modelo de selección de las tablas
            selection_modelResumen = self.InspeccionarTrabajador.tablaResumen.selectionModel()
            selection_modelDetallada = self.InspeccionarTrabajador.tablaDetallada.selectionModel()

            # Verifica si hay alguna celda seleccionada en los modelos de selección
            if selection_modelResumen.hasSelection() and selection_modelDetallada.hasSelection():
                selected = True
                selectedResumenRow = self.InspeccionarTrabajador.tablaResumen.currentRow()
                selectedDetalladaRow = self.InspeccionarTrabajador.tablaDetallada.currentRow()
                selectedResumenItem = self.InspeccionarTrabajador.tablaResumen.item(selectedResumenRow, 1)
                selectedDetalladaItem = self.InspeccionarTrabajador.tablaDetallada.item(selectedDetalladaRow, 1)

                if selectedResumenRow == selectedDetalladaRow:
                    if selectedResumenItem is None or selectedDetalladaItem is None:
                        MensajesWindow.mostrarMensajeBusquedaError("Aún no existe el detalle del mes seleccionado")
                    else:
                        selectedDatetime = selectedResumenItem.text()
                else:
                    MensajesWindow.mostrarMensajeBusquedaError("Por favor, asegúrese de seleccionar los mismos meses "
                                                               "tanto en la tabla resumen y en la tabla detallada")
            elif selection_modelResumen.hasSelection():
                selected = True
                selectedRow = self.InspeccionarTrabajador.tablaResumen.currentRow()
                selected_item = self.InspeccionarTrabajador.tablaResumen.item(selectedRow, 1)
                if selected_item is not None:
                    selectedDatetime = selected_item.text()
                else:
                    MensajesWindow.mostrarMensajeBusquedaError("Aún no existe detalle del mes seleccionado en la "
                                                               "tabla resumen")
            elif selection_modelDetallada.hasSelection():
                selected = True
                selectedRow = self.InspeccionarTrabajador.tablaDetallada.currentRow()
                selected_item = self.InspeccionarTrabajador.tablaDetallada.item(selectedRow, 1)
                if selected_item is not None:
                    selectedDatetime = selected_item.text()
                else:
                    MensajesWindow.mostrarMensajeBusquedaError("Aún no existe detalle del mes seleccionado en la "
                                                               "tabla detallada")
            print(f"\nFecha seleccionada a pagar: {selectedDatetime}")
            return selected, selectedDatetime
        except Exception as e:
            print(f"Error inesperado al intentar retornar datos de la fila seleccionada: {e}")

    def pagarSueldo(self):
        try:
            selected, selectedDatetime = self.returnRowDatetimeSelected()
            if selected:
                print(self.detalleMensual.detalleFecha)
                detalleMensualPagar = Queries.get_detalle_mensual_trabajador_by_date(selectedDatetime)
                detalleCalculoSueldoPagar = Queries.get_detalle_calculo_sueldo_by_id(detalleMensualPagar.IDTrabajador,
                                                                                     detalleMensualPagar.IDMes)
                if detalleMensualPagar and detalleCalculoSueldoPagar:
                    idBoleta = self.generarIDBoletaPago(detalleMensualPagar.detalleFecha.year,
                                                        detalleMensualPagar.detalleFecha.month)
                    idTrabajador = detalleMensualPagar.IDTrabajador
                    suedoNeto = detalleMensualPagar.detalleSueldoNeto
                    descuentoTotal = detalleCalculoSueldoPagar.calcSueldoTotalDctos
                    bonificacionTotal = detalleCalculoSueldoPagar.calcSueldoTotalBonificaciones

                    # Almacenar en la BD
                    Inserts.insertBoletaPago(idBoleta, idTrabajador, suedoNeto, descuentoTotal, bonificacionTotal)

                    # Generar enlace PDF
                    self.generarPDF(idBoleta)
                    print(int(detalleMensualPagar.detalleFecha.month) - 1)
                    # Llenar la fila de la tabla Historial de pagos de la GUI
                    self.fillRowGUITablaHistorialPagos(int(detalleMensualPagar.detalleFecha.month) - 1, idBoleta)
                    print(f"Mes a llenar en historial pagos: {detalleMensualPagar.detalleFecha.month - 1}")
                else:
                    mensaje = "Aún no existe detalle del mes actual en la BD"
                    print(mensaje)
                    MensajesWindow.mostrarMensajeBusquedaError(mensaje)
            else:
                mensaje = "Aún no se seleccionó una fila de la tabla resumen o tabla detallada para registrar el pago"
                print(mensaje)
                MensajesWindow.mostrarMensajeBusquedaError(mensaje)

        except Exception as e:
            print(f"Ocurrió un error durante el pago de sueldo: {e}")

    def ocultar(self):
        self.InspeccionarTrabajador.close()

    def regresar(self):
        self.parent.showBuscarExistenteTrabajador()

    def actualizarFechaSimulada(self, indice):
        # Añade 1 al índice para obtener el número del mes
        numMes = indice + 1
        # Obtiene la fecha actual
        fechaSimulada = QDate.currentDate()
        # Establece la nueva fecha con el mes seleccionado
        fechaSimulada.setDate(fechaSimulada.year(), numMes, fechaSimulada.day())
        # Establece la fecha en el widget dateEditFechaActual
        self.InspeccionarTrabajador.dateEditFechaActual.setDate(fechaSimulada)

    def initGUI(self):

        # Otros
        self.InspeccionarTrabajador.dateEditFechaActual.setDate(QDate.currentDate())
        self.InspeccionarTrabajador.comboBoxSimularMes.currentIndexChanged.connect(self.actualizarFechaSimulada)

        # Botones
        self.InspeccionarTrabajador.pushButtonRegresar.clicked.connect(self.regresar)
        self.InspeccionarTrabajador.pushButtonRegistrarDatosMensuales.clicked.connect(self.irFormRegistroDetalleMensual)
        self.InspeccionarTrabajador.pushButtonPagarSueldo.clicked.connect(self.pagarSueldo)

        # Tablas
        ancho_maximo = 1080
        num_columnas_TablaResumen = 6
        num_columnas_TablaHistorialPagos = 5

        ancho_columna_TablaResumen = int(ancho_maximo / num_columnas_TablaResumen)
        ancho_columna_TablaHistorialPagos = int(ancho_maximo / num_columnas_TablaHistorialPagos)

        for col in range(num_columnas_TablaResumen):
            self.InspeccionarTrabajador.tablaResumen.setColumnWidth(col, ancho_columna_TablaResumen)

        for column in range(num_columnas_TablaHistorialPagos):
            self.InspeccionarTrabajador.tablaHistorialPagos.setColumnWidth(column, ancho_columna_TablaHistorialPagos)

        self.InspeccionarTrabajador.tablaDetallada.resizeColumnsToContents()
        self.InspeccionarTrabajador.tablaBonificaciones.resizeColumnToContents(1)

        self.InspeccionarTrabajador.tablaResumen.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.InspeccionarTrabajador.tablaDetallada.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.InspeccionarTrabajador.tablaHistorialPagos.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)


class FormRegistroDetalleMensual(QMainWindow):
    def __init__(self, parent, nombMes):
        super().__init__()
        self.registroDetalleMensual = uic.loadUi(f"{directorio_ui}TrabajadorRegistrarDetalleMensual.ui",
                                                 self)  # Asignar la interfaz al objeto actual
        self.parent = parent
        self.nombMesSeleccionado = nombMes
        center(self.registroDetalleMensual)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)  # Mantener por encima de otras ventanas
        self.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, False)  # Desactivar el botón de minimizar
        self.initGUI()

    def mostrar(self):
        self.registroDetalleMensual.show()

    def ocultar(self):
        self.registroDetalleMensual.close()

    def closeEvent(self, event):
        self.registroDetalleMensual.ocultar()

    def guardar(self):
        try:
            horasExtras = self.registroDetalleMensual.lineEditHorasExtras.text()
            minTardanza = self.registroDetalleMensual.lineEditMinutosTardanza.text()
            diasFaltados = self.registroDetalleMensual.lineEditDiasFaltados.text()
            #mesSeleccionado = self.registroDetalleMensual.comboBoxMeses.currentText()
            # Pasar las variables a la instancia de FormInspeccionarTrabajador
            self.parent.obtenerDetalles(horasExtras, minTardanza, diasFaltados, self.nombMesSeleccionado)
            self.ocultar()
        except Exception as e:
            print(f"Error al leer los detalles: {e}")

    def cancelar(self):
        self.ocultar()

    def initGUI(self):

        self.registroDetalleMensual.lineEditMes.setText(self.nombMesSeleccionado)

        # Botones
        self.registroDetalleMensual.buttonBoxGuardarCancelar.accepted.connect(self.guardar)
        self.registroDetalleMensual.buttonBoxGuardarCancelar.rejected.connect(self.cancelar)

        # Cambiar el texto de los botones
        self.registroDetalleMensual.buttonBoxGuardarCancelar.button(
            QtWidgets.QDialogButtonBox.StandardButton.Save).setText("Guardar")
        self.registroDetalleMensual.buttonBoxGuardarCancelar.button(
            QtWidgets.QDialogButtonBox.StandardButton.Cancel).setText("Cancelar")
