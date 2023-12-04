from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt  # Importa Qt desde el módulo QtCore
from vista.Window_Utils import center, returnDirectorioGUI

directorio_ui = returnDirectorioGUI()


class FormMenuPrincipalSalir(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super().__init__()
        uic.loadUi(f"{directorio_ui}\MenuPrincipalSalir.ui", self)
        self.parent = parent
        center(self)
        self.initGUI()
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)  # Mantener por encima de otras ventanas
        self.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, False)  # Desactivar el botón de minimizar

    def mostrar(self):
        self.show()

    def ocultar(self):
        self.parent.habilitarLosBotones()
        self.parent.habilitarLaBarraMenu()
        self.close()

    def closeEvent(self, event):
        self.ocultar()

    def aceptarSalir(self):
        self.parent.salirApp()

    def cancelarSalir(self):
        self.ocultar()

    def initGUI(self):
        self.buttonBoxAceptarCancelar.accepted.connect(self.aceptarSalir)
        self.buttonBoxAceptarCancelar.rejected.connect(self.cancelarSalir)

