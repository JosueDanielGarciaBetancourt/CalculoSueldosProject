from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QGuiApplication
from vista.Window_Utils import center, returnDirectorioGUI
import os

ruta_absoluta = os.path.abspath(os.path.join(returnDirectorioGUI(), "MenuPrincipal.ui"))


class FormMenuPrincipal:
    def __init__(self, parent):
        self.parent = parent
        if os.path.exists(ruta_absoluta):
            self.MenuPrincipal = uic.loadUi(ruta_absoluta)

            center(self.MenuPrincipal)
            self.initGUI()
        else:
            print(f"Error: Archivo UI no encontrado en {ruta_absoluta}")

    def center(self):
        qr = self.MenuPrincipal.frameGeometry()
        cp = QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.MenuPrincipal.move(qr.topLeft())



    def mostrar(self):
        self.MenuPrincipal.show()

    def ocultar(self):
        self.MenuPrincipal.close()

    def deshabilitarBarraMenu(self):
        self.MenuPrincipal.menubarMenuPrincipal.setEnabled(False)

    def deshabilitarBotones(self):
        self.MenuPrincipal.pushButton_Trabajador.setEnabled(False)
        self.MenuPrincipal.pushButton_Bonificaciones.setEnabled(False)
        self.MenuPrincipal.pushButton_DetallesSW.setEnabled(False)
        self.MenuPrincipal.pushButton_Salir.setEnabled(False)

    def habilitarBarraMenu(self):
        self.MenuPrincipal.menubarMenuPrincipal.setEnabled(True)

    def habilitarBotones(self):
        self.MenuPrincipal.pushButton_Trabajador.setEnabled(True)
        self.MenuPrincipal.pushButton_Bonificaciones.setEnabled(True)
        self.MenuPrincipal.pushButton_DetallesSW.setEnabled(True)
        self.MenuPrincipal.pushButton_Salir.setEnabled(True)

    def salir(self):
        self.parent.deshabilitarLosBotones()
        self.parent.deshabilitarLaBarraMenu()
        self.parent.showMenuPrincipalSalir()

    def irInicio(self):
        pass

    def irMenuTrabajador(self):
        self.parent.showMenuTrabajador()

    def irMenuBonificacion(self):
        self.parent.showMenuBonificacion()

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
        self.MenuPrincipal.pushButton_Trabajador.clicked.connect(self.irMenuTrabajador)
        self.MenuPrincipal.pushButton_Bonificaciones.clicked.connect(self.irMenuBonificacion)
        self.MenuPrincipal.pushButton_Salir.clicked.connect(self.salir)
        self.MenuPrincipal.pushButton_DetallesSW.clicked.connect(self.irMenuDetallesSW)

        # menubar
        self.MenuPrincipal.actionInicio.triggered.connect(self.irInicio)
        self.MenuPrincipal.actionTrabajador.triggered.connect(self.irMenuTrabajador)
        self.MenuPrincipal.actionBonificaciones.triggered.connect(self.irMenuBonificacion)
        self.MenuPrincipal.actionAcercaDeGestorDeSueldosV1.triggered.connect(self.viewFormAcercaDeGestorDeSueldosV1)
        self.MenuPrincipal.actionAcercaDeNosotros.triggered.connect(self.viewFormAcercaDeNosotros)
        self.MenuPrincipal.actionSalir.triggered.connect(self.salir)


