from PyQt6 import QtWidgets
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QMessageBox
import os


def returnDirectorioGUI():
    directorio_trabajo = os.getcwd()
    directorioGUI = ("otros_recursos\\GUI\\")
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


class Mensajes:
    @staticmethod
    def mostrarMensaje(titulo, mensaje, icono):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(titulo)
        msgBox.setText(mensaje)
        msgBox.setIcon(icono)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.exec()

    @staticmethod
    def mostrarMensajeRegistroExito(mensaje):
        Mensajes.mostrarMensaje("Registro exitoso", mensaje, QMessageBox.Icon.Information)

    @staticmethod
    def mostrarMensajeRegistroError(titulo, mensaje):
        Mensajes.mostrarMensaje(titulo, mensaje, QMessageBox.Icon.Warning)

    @staticmethod
    def mostrarMensajeBusquedaExito(mensaje):
        Mensajes.mostrarMensaje("Búsqueda exitosa", mensaje, QMessageBox.Icon.Information)

    @staticmethod
    def mostrarMensajeBusquedaError(mensaje):
        Mensajes.mostrarMensaje("Error en la búsqueda", mensaje, QMessageBox.Icon.Warning)
