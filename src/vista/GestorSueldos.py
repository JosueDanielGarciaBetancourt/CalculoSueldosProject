from vista.FormMenuPrincipal import FormMenuPrincipal
from vista.FormMenuPrincipalSalir import FormMenuPrincipalSalir
from vista.FormMenuTrabajador import FormMenuTrabajador, FormRegistrarNuevoTrabajador, FormBuscarExistenteTrabajador, \
    FormInspeccionarTrabajador
from vista.FormMenuBonificacion import FormMenuBonificacion, FormBonificacionVerModificar
from vista.FormMenuDetallesSW import FormMenuDetallesSW
from vista.FormRegistroDetalleMensual import FormRegistroDetalleMensual
from vista.FormAcercaDeNosotros import FormAcercaDeNosotros
from vista.FormAcercaDeGestorDeSueldosV1 import FormAcercaDeGestorDeSueldosV1


class GestorSueldos:
    def __init__(self, app):
        self.app = app

        self.MenuPrincipal = FormMenuPrincipal(self)
        self.MenuTrabajador = FormMenuTrabajador(self)
        self.RegistrarNuevoTrabajador = FormRegistrarNuevoTrabajador(self)
        self.BuscarExistenteTrabajador = FormBuscarExistenteTrabajador(self)
        self.InspeccionarTrabajador = FormInspeccionarTrabajador(self, None)
        self.MenuBonificacion = FormMenuBonificacion(self)
        self.BonificacionVerModificar = FormBonificacionVerModificar(self)
        self.MenuDetallesSW = FormMenuDetallesSW(self)
        self.RegistroDetalleMensual = FormRegistroDetalleMensual(self)
        self.MenuPrincipalSalir = FormMenuPrincipalSalir(self)
        self.AcercaDeNosotros = FormAcercaDeNosotros(self)
        self.AcercaDeGestorDeSueldosV1 = FormAcercaDeGestorDeSueldosV1(self)

        self.MenuPrincipal.mostrar()
        self.MenuTrabajador.ocultar()
        self.RegistrarNuevoTrabajador.ocultar()
        self.BuscarExistenteTrabajador.ocultar()
        self.InspeccionarTrabajador.ocultar()
        self.MenuBonificacion.ocultar()
        self.BonificacionVerModificar.ocultar()
        self.MenuDetallesSW.ocultar()
        self.MenuPrincipalSalir.ocultar()
        self.AcercaDeNosotros.ocultar()
        self.AcercaDeGestorDeSueldosV1.ocultar()
        self.app.exec()

    def salirApp(self):
        self.app.quit()

    def showMenuPrincipal(self):
        if self.MenuTrabajador is not None:
            self.MenuTrabajador.ocultar()
        if self.MenuBonificacion is not None:
            self.MenuBonificacion.ocultar()
        if self.MenuDetallesSW is not None:
            self.MenuDetallesSW.ocultar()
        if self.MenuPrincipalSalir is not None:
            self.MenuPrincipalSalir.ocultar()
        if self.AcercaDeGestorDeSueldosV1 is not None:
            self.AcercaDeGestorDeSueldosV1.ocultar()

        if self.MenuPrincipal is None:
            self.MenuPrincipal = FormMenuPrincipal(self)
        else:
            self.MenuPrincipal.mostrar()

    def showMenuTrabajador(self):
        if self.MenuPrincipal is not None:
            self.MenuPrincipal.ocultar()
        if self.MenuBonificacion is not None:
            self.MenuBonificacion.ocultar()
        if self.MenuDetallesSW is not None:
            self.MenuDetallesSW.ocultar()
        if self.MenuPrincipalSalir is not None:
            self.MenuPrincipalSalir.ocultar()
        if self.AcercaDeGestorDeSueldosV1 is not None:
            self.AcercaDeGestorDeSueldosV1.ocultar()
        if self.BuscarExistenteTrabajador is not None:
            self.BuscarExistenteTrabajador.ocultar()
        if self.RegistrarNuevoTrabajador is not None:
            self.RegistrarNuevoTrabajador.ocultar()

        if self.MenuTrabajador is None:
            self.MenuTrabajador = FormMenuTrabajador(self)
        else:
            self.MenuTrabajador.mostrar()

    def showRegistrarNuevoTrabajador(self):
        if self.MenuPrincipal is not None:
            self.MenuPrincipal.ocultar()
        if self.MenuBonificacion is not None:
            self.MenuBonificacion.ocultar()
        if self.MenuDetallesSW is not None:
            self.MenuDetallesSW.ocultar()
        if self.MenuPrincipalSalir is not None:
            self.MenuPrincipalSalir.ocultar()
        if self.AcercaDeGestorDeSueldosV1 is not None:
            self.AcercaDeGestorDeSueldosV1.ocultar()
        if self.MenuTrabajador is not None:
            self.MenuTrabajador.ocultar()
        if self.InspeccionarTrabajador is not None:
            self.InspeccionarTrabajador.ocultar()
        if self.BuscarExistenteTrabajador is None:
            self.BuscarExistenteTrabajador.ocultar()

        if self.RegistrarNuevoTrabajador is None:
            self.RegistrarNuevoTrabajador = FormRegistrarNuevoTrabajador(self)
        else:
            self.RegistrarNuevoTrabajador.mostrar()

    def showBuscarExistenteTrabajador(self):
        if self.MenuPrincipal is not None:
            self.MenuPrincipal.ocultar()
        if self.MenuBonificacion is not None:
            self.MenuBonificacion.ocultar()
        if self.MenuDetallesSW is not None:
            self.MenuDetallesSW.ocultar()
        if self.MenuPrincipalSalir is not None:
            self.MenuPrincipalSalir.ocultar()
        if self.AcercaDeGestorDeSueldosV1 is not None:
            self.AcercaDeGestorDeSueldosV1.ocultar()
        if self.MenuTrabajador is not None:
            self.MenuTrabajador.ocultar()
        if self.RegistrarNuevoTrabajador is not None:
            self.RegistrarNuevoTrabajador.ocultar()
        if self.InspeccionarTrabajador is not None:
            self.InspeccionarTrabajador.ocultar()

        if self.BuscarExistenteTrabajador is None:
            self.BuscarExistenteTrabajador = FormBuscarExistenteTrabajador(self)
        else:
            self.BuscarExistenteTrabajador.mostrar()

    def showInspeccionarTrabajador(self, trabajador):
        if self.MenuPrincipal is not None:
            self.MenuPrincipal.ocultar()
        if self.MenuBonificacion is not None:
            self.MenuBonificacion.ocultar()
        if self.MenuDetallesSW is not None:
            self.MenuDetallesSW.ocultar()
        if self.MenuPrincipalSalir is not None:
            self.MenuPrincipalSalir.ocultar()
        if self.AcercaDeGestorDeSueldosV1 is not None:
            self.AcercaDeGestorDeSueldosV1.ocultar()
        if self.MenuTrabajador is not None:
            self.MenuTrabajador.ocultar()
        if self.RegistrarNuevoTrabajador is not None:
            self.RegistrarNuevoTrabajador.ocultar()
        if self.BuscarExistenteTrabajador is not None:
            self.BuscarExistenteTrabajador.ocultar()

        if self.InspeccionarTrabajador is None:
            self.InspeccionarTrabajador = FormInspeccionarTrabajador(self, trabajador)
        else:
            self.InspeccionarTrabajador = FormInspeccionarTrabajador(self, trabajador)
            self.InspeccionarTrabajador.mostrar()

    def showMenuBonificacion(self):
        if self.MenuPrincipal is not None:
            self.MenuPrincipal.ocultar()
        if self.MenuTrabajador is not None:
            self.MenuTrabajador.ocultar()
        if self.MenuDetallesSW is not None:
            self.MenuDetallesSW.ocultar()
        if self.MenuPrincipalSalir is not None:
            self.MenuPrincipalSalir.ocultar()
        if self.AcercaDeGestorDeSueldosV1 is not None:
            self.AcercaDeGestorDeSueldosV1.ocultar()
        if self.BonificacionVerModificar is not None:
            self.BonificacionVerModificar.ocultar()

        if self.MenuBonificacion is None:
            self.MenuBonificacion = FormMenuBonificacion(self)
        else:
            self.MenuBonificacion.mostrar()

    def showBonificacionVerModificar(self):
        if self.MenuPrincipal is not None:
            self.MenuPrincipal.ocultar()
        if self.MenuTrabajador is not None:
            self.MenuTrabajador.ocultar()
        if self.MenuDetallesSW is not None:
            self.MenuDetallesSW.ocultar()
        if self.MenuPrincipalSalir is not None:
            self.MenuPrincipalSalir.ocultar()
        if self.AcercaDeGestorDeSueldosV1 is not None:
            self.AcercaDeGestorDeSueldosV1.ocultar()
        if self.MenuBonificacion is not None:
            self.MenuBonificacion.ocultar()

        if self.BonificacionVerModificar is None:
            self.BonificacionVerModificar = FormBonificacionVerModificar(self)
        else:
            self.BonificacionVerModificar.mostrar()

    def showMenuDetallesSW(self):
        if self.MenuPrincipal is not None:
            self.MenuPrincipal.ocultar()
        if self.MenuTrabajador is not None:
            self.MenuTrabajador.ocultar()
        if self.MenuBonificacion is not None:
            self.MenuBonificacion.ocultar()
        if self.MenuPrincipalSalir is not None:
            self.MenuPrincipalSalir.ocultar()
        if self.AcercaDeGestorDeSueldosV1 is not None:
            self.AcercaDeGestorDeSueldosV1.ocultar()

        if self.MenuDetallesSW is None:
            self.MenuDetallesSW = FormMenuDetallesSW(self)
        else:
            self.MenuDetallesSW.mostrar()

    def showRegistroDetalleMensual(self):
        if self.RegistroDetalleMensual is None:
            self.RegistroDetalleMensual = FormRegistroDetalleMensual(self)
        else:
            self.RegistroDetalleMensual.mostrar()

    def showMenuPrincipalSalir(self):
        if self.MenuPrincipalSalir is None:
            self.MenuPrincipalSalir = FormMenuPrincipalSalir(self)
        else:
            self.MenuPrincipalSalir.mostrar()

    def showFormAcercaDeNosotros(self):
        if self.AcercaDeNosotros is None:
            self.AcercaDeNosotros = FormAcercaDeNosotros(self)
        else:
            self.AcercaDeNosotros.mostrar()

    def showFormAcercaDeGestorDeSueldosV1(self):
        if self.AcercaDeGestorDeSueldosV1 is None:
            self.AcercaDeGestorDeSueldosV1 = FormAcercaDeGestorDeSueldosV1(self)
        else:
            self.AcercaDeGestorDeSueldosV1.mostrar()

    def deshabilitarVentana(self):
        self.MenuPrincipal.habilitarBotones()

    def habilitarLosBotones(self):
        self.MenuPrincipal.habilitarBotones()
        self.MenuTrabajador.habilitarBotones()
        self.MenuBonificacion.habilitarBotones()
        self.MenuDetallesSW.habilitarBotones()

    def deshabilitarLosBotones(self):
        self.MenuPrincipal.deshabilitarBotones()
        self.MenuTrabajador.deshabilitarBotones()
        self.MenuBonificacion.deshabilitarBotones()
        self.MenuDetallesSW.deshabilitarBotones()

    def habilitarLaBarraMenu(self):
        self.MenuPrincipal.habilitarBarraMenu()
        self.MenuTrabajador.habilitarBarraMenu()
        self.MenuBonificacion.habilitarBarraMenu()
        self.MenuDetallesSW.habilitarBarraMenu()

    def deshabilitarLaBarraMenu(self):
        self.MenuPrincipal.deshabilitarBarraMenu()
        self.MenuTrabajador.deshabilitarBarraMenu()
        self.MenuBonificacion.deshabilitarBarraMenu()
        self.MenuDetallesSW.deshabilitarBarraMenu()
