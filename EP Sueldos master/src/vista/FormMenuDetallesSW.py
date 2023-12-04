from PyQt6 import QtWidgets, uic
from vista.Window_Utils import center, returnDirectorioGUI

directorio_ui = returnDirectorioGUI()


class FormMenuDetallesSW:
    def __init__(self, parent):
        self.parent = parent
        self.MenuDetallesSW = uic.loadUi(f"{directorio_ui}\MenuDetallesSW.ui")
        center(self.MenuDetallesSW)
        self.initGUI()

    def mostrar(self):
        self.MenuDetallesSW.show()

    def ocultar(self):
        self.MenuDetallesSW.close()

    def deshabilitarBarraMenu(self):
        self.MenuDetallesSW.menubarMenuDetallesSW.setEnabled(False)

    def deshabilitarBotones(self):
        self.MenuDetallesSW.pushButtonAcercaDeGestorDeSueldosV1.setEnabled(False)
        self.MenuDetallesSW.pushButtonAcercaDeNosotros.setEnabled(False)
        self.MenuDetallesSW.pushButtonRegresar.setEnabled(False)

    def habilitarBarraMenu(self):
        self.MenuDetallesSW.menubarMenuDetallesSW.setEnabled(True)

    def habilitarBotones(self):
        self.MenuDetallesSW.pushButtonAcercaDeGestorDeSueldosV1.setEnabled(True)
        self.MenuDetallesSW.pushButtonAcercaDeNosotros.setEnabled(True)
        self.MenuDetallesSW.pushButtonRegresar.setEnabled(True)

    def salir(self):
        self.parent.deshabilitarLosBotones()
        self.parent.deshabilitarLaBarraMenu()
        self.parent.showMenuPrincipalSalir()

    def regresarMenuPrincipal(self):
        self.parent.showMenuPrincipal()

    def irMenuTrabajador(self):
        self.parent.showMenuTrabajador()

    def irMenuBonificacion(self):
        self.parent.showMenuBonificacion()

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
        self.MenuDetallesSW.pushButtonRegresar.clicked.connect(self.regresarMenuPrincipal)
        self.MenuDetallesSW.pushButtonAcercaDeNosotros.clicked.connect(self.viewFormAcercaDeNosotros)
        self.MenuDetallesSW.pushButtonAcercaDeGestorDeSueldosV1.clicked.connect(self.viewFormAcercaDeGestorDeSueldosV1)
        # menubar
        self.MenuDetallesSW.actionInicio.triggered.connect(self.regresarMenuPrincipal)
        self.MenuDetallesSW.actionTrabajador.triggered.connect(self.irMenuTrabajador)
        self.MenuDetallesSW.actionBonificaciones.triggered.connect(self.irMenuBonificacion)
        self.MenuDetallesSW.actionAcercaDeNosotros.triggered.connect(self.viewFormAcercaDeNosotros)
        self.MenuDetallesSW.actionSalir.triggered.connect(self.salir)
        self.MenuDetallesSW.actionAcercaDeGestorDeSueldosV1.triggered.connect(self.viewFormAcercaDeGestorDeSueldosV1)



