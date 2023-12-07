from PyQt6 import QtWidgets
from PyQt6.QtGui import QGuiApplication


def returnDirectorioGUI():
    directorioGUI = ("otros recursos\\GUI\\")
    return directorioGUI


def center(window):
    qr = window.frameGeometry()
    cp = QGuiApplication.primaryScreen().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())


class ConfirmacionDialog(QtWidgets.QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Advertencia")
        self.setText("¿Seguro que desea eliminar esta fila?")
        self.addButton("Sí", QtWidgets.QMessageBox.ButtonRole.YesRole)
        self.addButton("No", QtWidgets.QMessageBox.ButtonRole.NoRole)
