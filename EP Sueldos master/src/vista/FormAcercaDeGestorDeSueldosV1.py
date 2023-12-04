from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt  # Importa Qt desde el módulo QtCore
from vista.Window_Utils import center ,returnDirectorioGUI

directorio_ui = returnDirectorioGUI()


class FormAcercaDeGestorDeSueldosV1(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super().__init__()
        uic.loadUi(f"{directorio_ui}\AcercaDeGestorDeSueldosV1.ui", self)
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

    def initGUI(self):
        self.buttonBoxCerrar.rejected.connect(self.ocultar)
