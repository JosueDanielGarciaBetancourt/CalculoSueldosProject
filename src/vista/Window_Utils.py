from PyQt6 import QtWidgets
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QMessageBox


def returnDirectorioGUI():
    directorioGUI = "otros_recursos\\GUI\\"
    return directorioGUI


def center(window):
    qr = window.frameGeometry()
    cp = QGuiApplication.primaryScreen().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())


class MensajesWindow:
    @staticmethod
    def mostrarMensaje(titulo, mensaje, icono):
        msgBox = QMessageBox()
        msgBox.setIcon(icono)
        msgBox.setWindowTitle(titulo)
        msgBox.setText(mensaje)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.exec()

    @staticmethod
    def mostrarMensajeConfirmacion(titulo, mensaje, icon):
        confirmBox = QMessageBox()
        confirmBox.setIcon(icon)
        confirmBox.setWindowTitle(titulo)
        confirmBox.setText(mensaje)
        confirmBox.addButton("Sí", QtWidgets.QMessageBox.ButtonRole.YesRole)
        confirmBox.addButton("No", QtWidgets.QMessageBox.ButtonRole.NoRole)
        confirmBox.exec()
        return confirmBox.clickedButton().text()

    @staticmethod
    def mostrarMensajeRegistroExito(mensaje):
        MensajesWindow.mostrarMensaje("Registro exitoso", mensaje, QMessageBox.Icon.Information)

    @staticmethod
    def mostrarMensajeRegistroError(mensaje):
        MensajesWindow.mostrarMensaje("Registro fallido", mensaje, QMessageBox.Icon.Warning)

    @staticmethod
    def mostrarMensajeBusquedaExito(mensaje):
        MensajesWindow.mostrarMensaje("Búsqueda exitosa", mensaje, QMessageBox.Icon.Information)

    @staticmethod
    def mostrarMensajeBusquedaError(mensaje):
        MensajesWindow.mostrarMensaje("Error en la búsqueda", mensaje, QMessageBox.Icon.Warning)

    @staticmethod
    def mostrarMensajeEliminarExito(mensaje):
        MensajesWindow.mostrarMensaje("Éxito al borrar", mensaje, QMessageBox.Icon.Information)

    @staticmethod
    def mostrarMensajeEliminarError(mensaje):
        MensajesWindow.mostrarMensaje("Error al borrar", mensaje, QMessageBox.Icon.Warning)

    @staticmethod
    def mostrarMensajeErrorInesperado(mensaje):
        MensajesWindow.mostrarMensaje("Error inesperado", mensaje, QMessageBox.Icon.Critical)
