from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QMessageBox
from vista.Window_Utils import center, ConfirmacionDialog, returnDirectorioGUI

directorio_ui = returnDirectorioGUI()


class FormMenuBonificacion:
    def __init__(self, parent):
        self.parent = parent
        self.MenuBonificacion = uic.loadUi(f"{directorio_ui}\MenuBonificacion.ui")
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
        self.initGUI()

    def mostrar(self):
        self.BonificacionVerModificar.show()

    def ocultar(self):
        self.BonificacionVerModificar.close()

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

    def modificarBonificacion(self):
        # Hacer que la columna 3 sea editable
        for i in range(self.BonificacionVerModificar.tablaBonificaciones.rowCount()):
            item = QtWidgets.QTableWidgetItem()
            self.BonificacionVerModificar.tablaBonificaciones.setItem(i, 3, item)

    def eliminarBonificacion(self):
        if self.verificarSeleccion():
            # Crea una instancia de la ventana de confirmación
            confirmacion_dialog = ConfirmacionDialog(self.BonificacionVerModificar)

            # Muestra el dialogo y guarda el botón que se presionó
            confirmacion_dialog.exec()

            # Si el botón presionado fue 'Sí', elimina la fila
            if confirmacion_dialog.clickedButton().text() == "Sí":
                selected_row = self.BonificacionVerModificar.tablaBonificaciones.currentRow()
                self.BonificacionVerModificar.tablaBonificaciones.removeRow(selected_row)
                self.deseleccionarTabla()
        else:
            # Muestra un mensaje o realiza alguna acción si no hay fila seleccionada
            QMessageBox.warning(self.BonificacionVerModificar, "Advertencia", "Selecciona una fila antes de eliminar")

    def deseleccionarTabla(self):
        self.BonificacionVerModificar.tablaBonificaciones.clearSelection()

    def regresar(self):
        self.parent.showMenuBonificacion()

    def initGUI(self):
        self.BonificacionVerModificar.dateEditFechaActual.setDate(QDate.currentDate())
        self.BonificacionVerModificar.pushButtonNoSelection.clicked.connect(self.deseleccionarTabla)

        # botones
        self.BonificacionVerModificar.pushButton_AgregarBonificacion.clicked.connect(self.agregarBonificacion)
        self.BonificacionVerModificar.pushButton_ModificarBonificacion.clicked.connect(self.modificarBonificacion)
        self.BonificacionVerModificar.pushButton_EliminarBonificacion.clicked.connect(self.eliminarBonificacion)
        self.BonificacionVerModificar.pushButton_Regresar.clicked.connect(self.regresar)

        # tabla
        self.BonificacionVerModificar.tablaBonificaciones.resizeColumnsToContents()
        self.BonificacionVerModificar.tablaBonificaciones.resizeRowsToContents()
        self.BonificacionVerModificar.tablaBonificaciones.setEditTriggers(
           QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)

