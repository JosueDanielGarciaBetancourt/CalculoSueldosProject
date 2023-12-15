from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate
from vista.Window_Utils import MensajesWindow
from vista.Window_Utils import center, returnDirectorioGUI
from logica.Inserts import Insert, InsertSignal
from logica.Deletes import Delete
from logica.Updates import Update
from logica.Queries import Queries
from logica.CalculoSueldo import CalculoSueldo
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox

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
        # botones
        self.MenuTrabajador.pushButtonRegresar.clicked.connect(self.regresarMenuPrincipal)
        self.MenuTrabajador.pushButton_RegistrarNuevo.clicked.connect(self.irRegistrarTrabajador)
        self.MenuTrabajador.pushButton_BuscarExistente.clicked.connect(self.irBuscarTrabajador)

        # menubar
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
                Insert.insertTrabajador(DNI, ApellidosNombres, SueldoBase, Cargo)
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

    def buscarTrabajadorID(self):
        busquedaDNI = self.BuscarExistenteTrabajador.lineEditDNIBuscar.text()
        trabajadorBuscado = Queries.get_trabajador_by_id(busquedaDNI)
        if busquedaDNI.strip() == "":
            MensajesWindow.mostrarMensajeBusquedaError(f"Por favor ingrese el DNI del trabajador a inspeccionar")
        elif not busquedaDNI.isdigit() or len(busquedaDNI) != 8:
            MensajesWindow.mostrarMensajeBusquedaError("El DNI ingresado debe contener 8 cifras numéricas")
        elif trabajadorBuscado is None:
            MensajesWindow.mostrarMensajeBusquedaError(f"No existe trabajador con DNI: {busquedaDNI}")
        else:
            MensajesWindow.mostrarMensajeBusquedaExito(f"Trabajador con DNI: {busquedaDNI} encontrado")
            self.parent.showInspeccionarTrabajador()

    def fillRowGUITableTrabajadores(self, row, trabajador):
        # Crear items para cada columna y convertirlos a cadena para mostrarlos en la tabla
        id_item = QTableWidgetItem(str(trabajador.IDTrabajador))
        nombre_item = QTableWidgetItem(str(trabajador.trabNombreApellidos))
        cargo_item = QTableWidgetItem(str(trabajador.Cargo))
        sueldo_item = QTableWidgetItem(str(trabajador.trabSueldoBase))
        fecha_creacion_item = QTableWidgetItem(str(trabajador.created_at))

        # Establecer los items en la fila de la tabla
        self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.setItem(row, 0, id_item)
        self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.setItem(row, 1, nombre_item)
        self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.setItem(row, 2, cargo_item)
        self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.setItem(row, 3, sueldo_item)
        self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.setItem(row, 4, fecha_creacion_item)

    def updateGUITableTrabajadores(self):
        todos_los_trabajadores = Queries.get_all_trabajadores()
        # Limpiar la tabla antes de llenarla para evitar duplicados
        self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.setRowCount(0)

        # Llenar la tabla con los trabajadores
        for row, trabajador in enumerate(todos_los_trabajadores):
            self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.insertRow(row)
            self.fillRowGUITableTrabajadores(row, trabajador)

        # Ancho máximo deseado para la tabla
        ancho_maximo = 1040

        # Número de columnas
        num_columnas = 5

        # Calcular el ancho que cada columna debería tener para sumar el ancho máximo
        ancho_columna = int(ancho_maximo / num_columnas)

        # Establecer el ancho de cada columna
        for col in range(num_columnas):
            self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.setColumnWidth(col, ancho_columna)

    def deleteRowGUITableIDTrabajador(self):
        seleccionado = False
        # Obtiene el modelo de selección de la tabla
        selection_model = self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.selectionModel()
        # Verifica si hay alguna celda seleccionada en el modelo de selección
        if selection_model.hasSelection():
            seleccionado = True

        if seleccionado:
            selectedRow = self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.currentRow()
            selectedDNI = self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.item(selectedRow, 0).text()

            print(selectedDNI)
            confirmacionEliminar = MensajesWindow.mostrarMensajeConfirmacion("Confirmación de eliminación",
                                                                             f"Se eliminará el trabajador con DNI {selectedDNI}. "
                                                                             f"¿Está seguro de eliminarlo?",
                                                                             QMessageBox.Icon.Question)
            if confirmacionEliminar == "Sí":
                try:
                    # Eliminar fila seleccionada de la tabla
                    self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.removeRow(selectedRow)
                    # Eliminar trabajador seleccionado de la BD
                    Delete.deleteTrabajador(selectedDNI)
                    MensajesWindow.mostrarMensajeEliminarExito(f"Se eliminó el trabajador con DNI: {selectedDNI}")
                except Exception as e:
                    mensaje = f"Error inesperado al eliminar trabajador: {e}"
                    print(mensaje)
                    MensajesWindow.mostrarMensajeEliminarError(mensaje)
            self.deseleccionarTabla()
        else:
            MensajesWindow.mostrarMensajeEliminarError("No se seleccionó trabajador. "
                                                       "Por favor seleccione un trabajador para eliminarlo")

    def deseleccionarTabla(self):
        self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.clearSelection()

    def initGUI(self):
        # Botones
        self.BuscarExistenteTrabajador.pushButtonRegresar.clicked.connect(self.regresar)
        self.BuscarExistenteTrabajador.pushButtonInspeccionarTrabajador.clicked.connect(self.buscarTrabajadorID)
        self.BuscarExistenteTrabajador.pushButtonEliminarTrabajador.clicked.connect(self.deleteRowGUITableIDTrabajador)
        self.BuscarExistenteTrabajador.dateEditFechaActual.setDate(QDate.currentDate())

        # Tabla trabajadores GUI
        self.updateGUITableTrabajadores()
        Insert.signal.trabajadorInserted.connect(self.updateGUITableTrabajadores)
        Delete.signal.trabajadorDeleted.connect(self.updateGUITableTrabajadores)
        self.BuscarExistenteTrabajador.tableTrabajadoresRegistrados.setEditTriggers(
            QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)

class FormInspeccionarTrabajador:
    def __init__(self, parent):
        self.parent = parent
        self.InspeccionarTrabajador = uic.loadUi(f"{directorio_ui}\\TrabajadorInspeccionar.ui")
        center(self.InspeccionarTrabajador)
        self.initGUI()

    def mostrar(self):
        self.InspeccionarTrabajador.show()

    def ocultar(self):
        self.InspeccionarTrabajador.close()

    def regresar(self):
        self.parent.showBuscarExistenteTrabajador()

    def initGUI(self):
        self.InspeccionarTrabajador.pushButtonRegresar.clicked.connect(self.regresar)
