import re
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate, Qt
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
from vista.Window_Utils import center, MensajesWindow, returnDirectorioGUI
from logica.Queries import Queries
from logica.Updates import Update

directorio_ui = returnDirectorioGUI()


class FormMenuBonificacion:
    def __init__(self, parent):
        self.parent = parent
        self.MenuBonificacion = uic.loadUi(f"{directorio_ui}MenuBonificacion.ui")
        center(self.MenuBonificacion)
        self.initGUI()

    def mostrar(self):
        self.MenuBonificacion.show()

    def ocultar(self):
        self.MenuBonificacion.close()

    def deshabilitarBarraMenu(self):
        self.MenuBonificacion.menubarMenuBonificacion.setEnabled(False)

    def deshabilitarBotones(self):
        self.MenuBonificacion.pushButtonBuscarBonificaciones.setEnabled(False)
        self.MenuBonificacion.pushButtonRegresar.setEnabled(False)

    def habilitarBarraMenu(self):
        self.MenuBonificacion.menubarMenuBonificacion.setEnabled(True)

    def habilitarBotones(self):
        self.MenuBonificacion.pushButtonBuscarBonificaciones.setEnabled(True)
        self.MenuBonificacion.pushButtonRegresar.setEnabled(True)

    def salir(self):
        self.parent.deshabilitarLosBotones()
        self.parent.deshabilitarLaBarraMenu()
        self.parent.showMenuPrincipalSalir()

    def irBonificacionVerModificar(self):
        self.parent.showBonificacionVerModificar()

    def regresarMenuPrincipal(self):
        self.parent.showMenuPrincipal()

    def irMenuTrabajador(self):
        self.parent.showMenuTrabajador()

    def irMenuDetallesSW(self):
        self.parent.showMenuDetallesSW()

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
        self.MenuBonificacion.pushButtonRegresar.clicked.connect(self.regresarMenuPrincipal)
        self.MenuBonificacion.pushButtonBuscarBonificaciones.clicked.connect(self.irBonificacionVerModificar)

        # menubar
        self.MenuBonificacion.actionInicio.triggered.connect(self.regresarMenuPrincipal)
        self.MenuBonificacion.actionTrabajador.triggered.connect(self.irMenuTrabajador)
        self.MenuBonificacion.actionAcercaDeGestorDeSueldosV1.triggered.connect(self.viewFormAcercaDeGestorDeSueldosV1)
        self.MenuBonificacion.actionAcercaDeNosotros.triggered.connect(self.viewFormAcercaDeNosotros)
        self.MenuBonificacion.actionSalir.triggered.connect(self.salir)


class FormBonificacionVerModificar:
    def __init__(self, parent):
        self.parent = parent
        self.BonificacionVerModificar = uic.loadUi(f"{directorio_ui}\BonificacionVerModificar.ui")
        center(self.BonificacionVerModificar)
        self.tableColumnValorBoniEditable = False  # Variable para rastrear el estado de edición
        self.original_values = []
        self.initGUI()

    def mostrar(self):
        self.BonificacionVerModificar.show()

    def ocultar(self):
        self.BonificacionVerModificar.close()

    def regresar(self):
        self.parent.showMenuBonificacion()

    def verificarSeleccion(self):
        seleccionado = False
        # Obtiene el modelo de selección de la tabla
        selection_model = self.BonificacionVerModificar.tablaBonificaciones.selectionModel()
        # Verifica si hay alguna celda seleccionada en el modelo de selección
        if selection_model.hasSelection():
            seleccionado = True
        return seleccionado

    def agregarBonificacion(self):
        pass

    def enable_disable_edit_tableBonificacionescolumn3(self):
        try:
            self.tableColumnValorBoniEditable = not self.tableColumnValorBoniEditable
            num_filas = self.BonificacionVerModificar.tablaBonificaciones.rowCount()
            for fila in range(num_filas):
                item = self.BonificacionVerModificar.tablaBonificaciones.item(fila, 3)
                if self.tableColumnValorBoniEditable:
                    item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)
                else:
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
        except Exception as e:
            mensaje = f"Ocurrió un error inesperado al intentar habilitar/deshabilitar la columna Valor, {e}"
            print(mensaje)
            MensajesWindow.mostrarMensajeErrorInesperado(mensaje)

    def modificarGUITableBonificacionesColumn3(self):
        self.enable_disable_edit_tableBonificacionescolumn3()
        # Guarda el valor original antes de intentar la modificación
        print(self.tableColumnValorBoniEditable)
        print()
        num_filas = self.BonificacionVerModificar.tablaBonificaciones.rowCount()
        try:
            if self.tableColumnValorBoniEditable:
                self.original_values = []
                for fila in range(num_filas):
                    valorAlmacenadoBonificacion = self.BonificacionVerModificar.tablaBonificaciones.item(fila, 3).text()
                    print(valorAlmacenadoBonificacion)
                    self.original_values.append(valorAlmacenadoBonificacion)
            print(self.original_values)
        except Exception as e:
            print(f"Error inesperado al guardar valores iniciales {e}")

        if not self.tableColumnValorBoniEditable:
            try:
                for fila in range(num_filas):
                    valorBonificacion = self.BonificacionVerModificar.tablaBonificaciones.item(fila, 3).text()
                    try:
                        valorBonificacion = float(valorBonificacion)
                    except ValueError:
                        print("No se puede convertir a número")
                        raise ValueError("No se puede convertir a número")

                    if valorBonificacion <= 0:
                        print("No se permiten valores menores o iguales a 0")
                        raise ValueError("No se permiten valores menores o iguales a 0")

                    if not re.match(r'^[0-9.]+$', str(valorBonificacion)):
                        print("No se permiten valores que contengan letras")
                        raise ValueError("No se permiten valores que contengan letras")

                    print(f"Valor {valorBonificacion} de fila {fila + 1} bonificación almacenado correctamente")

            except ValueError as e:
                self.tableColumnValorBoniEditable = False
                self.enable_disable_edit_tableBonificacionescolumn3()
                try:
                    print(self.original_values)
                    for fila in range(num_filas):
                        original_value_item = QTableWidgetItem(str(self.original_values[fila]))
                        self.BonificacionVerModificar.tablaBonificaciones.setItem(fila, 3, original_value_item)
                except Exception as e:
                    print(e)
                mensaje = f"Error inesperado al procesar los valores {valorBonificacion}: {e}, " \
                          f"por favor ingreses valores numéricos"
                print(mensaje)
                MensajesWindow.mostrarMensajeErrorInesperado(mensaje)
            except Exception as e:
                self.tableColumnValorBoniEditable = False
                self.enable_disable_edit_tableBonificacionescolumn3()
                try:
                    print(self.original_values)
                    for fila in range(num_filas):
                        original_value_item = QTableWidgetItem(str(self.original_values[fila]))
                        self.BonificacionVerModificar.tablaBonificaciones.setItem(fila, 3, original_value_item)
                except Exception as e:
                    print(e)
                mensaje = f"Error inesperado al procesar los valores {valorBonificacion}: {e}, " \
                          f"por favor ingreses valores numéricos"
                print(mensaje)
                MensajesWindow.mostrarMensajeErrorInesperado(mensaje)

    def eliminarBonificacion(self):
        try:
            if self.verificarSeleccion():
                selectedRow = self.BonificacionVerModificar.tablaBonificaciones.currentRow()
                selectedTipoBonificacion = self.BonificacionVerModificar.tablaBonificaciones.item(selectedRow, 1).text()
                confirmacionEliminar = MensajesWindow.mostrarMensajeConfirmacion("Confirmación de eliminación",
                                                                                 f"Se eliminará la bonificación {selectedTipoBonificacion}. "
                                                                                 f"¿Está seguro de eliminarla?",
                                                                                 QMessageBox.Icon.Question)
                if confirmacionEliminar == "Sí":
                    selected_row = self.BonificacionVerModificar.tablaBonificaciones.currentRow()
                    self.BonificacionVerModificar.tablaBonificaciones.removeRow(selected_row)
                    self.deseleccionarTabla()
            else:
                MensajesWindow.mostrarMensajeEliminarError("Selecciona una fila antes de eliminar")
        except Exception as e:
            mensaje = f"Error inesperado al eliminar bonificación: {e}"
            print(mensaje)
            MensajesWindow.mostrarMensajeEliminarError(mensaje)

    def deseleccionarTabla(self):
        self.BonificacionVerModificar.tablaBonificaciones.clearSelection()

    def initGUI(self):
        self.BonificacionVerModificar.dateEditFechaActual.setDate(QDate.currentDate())
        self.BonificacionVerModificar.pushButtonNoSelection.clicked.connect(self.deseleccionarTabla)

        # botones
        self.BonificacionVerModificar.pushButton_AgregarBonificacion.clicked.connect(self.agregarBonificacion)
        self.BonificacionVerModificar.pushButton_ModificarBonificacion.clicked.connect(
            self.modificarGUITableBonificacionesColumn3)
        self.BonificacionVerModificar.pushButton_EliminarBonificacion.clicked.connect(self.eliminarBonificacion)
        self.BonificacionVerModificar.pushButton_Regresar.clicked.connect(self.regresar)

        # tabla
        self.BonificacionVerModificar.tablaBonificaciones.resizeColumnsToContents()
        self.BonificacionVerModificar.tablaBonificaciones.resizeRowsToContents()

        # En Qt Designer ya se realizó la deshabilitación de edición de todas las celdas
