from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt  # Importa Qt desde el módulo QtCore
from vista.Window_Utils import center, returnDirectorioGUI

directorio_ui = returnDirectorioGUI()


class FormRegistroDetalleMensual(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super().__init__()
        uic.loadUi(f"{directorio_ui}TrabajadorRegistrarDetalleMensual.ui", self) # Asignar la interfaz al objeto actual
        self.parent = parent
        center(self)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)  # Mantener por encima de otras ventanas
        self.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, False)  # Desactivar el botón de minimizar
        self.initGUI()

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.close()

    def closeEvent(self, event):
        self.ocultar()

    def guardar(self):
        print("Guardar registro detalle mensual")
        self.parent.salirApp()

    def cancelar(self):
        self.ocultar()

    def initGUI(self):
        # Botones
        self.buttonBoxGuardarCancelar.accepted.connect(self.guardar)
        self.buttonBoxGuardarCancelar.rejected.connect(self.cancelar)

        # Cambiar el texto de los botones
        self.buttonBoxGuardarCancelar.button(QtWidgets.QDialogButtonBox.StandardButton.Save).setText("Guardar")
        self.buttonBoxGuardarCancelar.button(QtWidgets.QDialogButtonBox.StandardButton.Cancel).setText("Cancelar")
