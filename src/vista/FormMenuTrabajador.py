from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QMessageBox
from vista.Window_Utils import center, returnDirectorioGUI
from logica.Inserts import Insert
from logica.Deletes import Delete
from logica.Updates import Update
from logica.Queries import Queries
from logica.CalculoSueldo import CalculoSueldo

directorio_ui = returnDirectorioGUI()


class FormMenuTrabajador:
    def __init__(self, parent):
        self.parent = parent
        self.MenuTrabajador = uic.loadUi(f"{directorio_ui}MenuTrabajador.ui")
        center(self.MenuTrabajador)
        self.initGUI()

    def mostrar(self):
        self.MenuTrabajador.show()

    def ocultar(self):
        self.MenuTrabajador.close()

    def deshabilitarBarraMenu(self):
        self.MenuTrabajador.menubarMenuTrabajador.setEnabled(False)

    def deshabilitarBotones(self):
        self.MenuTrabajador.pushButton_RegistrarNuevo.setEnabled(False)
        self.MenuTrabajador.pushButton_BuscarExistente.setEnabled(False)
        self.MenuTrabajador.pushButtonRegresar.setEnabled(False)

    def habilitarBarraMenu(self):
        self.MenuTrabajador.menubarMenuTrabajador.setEnabled(True)

    def habilitarBotones(self):
        self.MenuTrabajador.pushButton_RegistrarNuevo.setEnabled(True)
        self.MenuTrabajador.pushButton_BuscarExistente.setEnabled(True)
        self.MenuTrabajador.pushButtonRegresar.setEnabled(True)

    def salir(self):
        self.parent.deshabilitarLosBotones()
        self.parent.deshabilitarLaBarraMenu()
        self.parent.showMenuPrincipalSalir()

    def regresarMenuPrincipal(self):
        self.parent.showMenuPrincipal()

    def irMenuBonificacion(self):
        self.parent.showMenuBonificacion()

    def irMenuDetallesSW(self):
        self.parent.showMenuDetallesSW()

    def irRegistrarTrabajador(self):
        self.parent.showRegistrarNuevoTrabajador()

    def irBuscarTrabajador(self):
        self.parent.showBuscarExistenteTrabajador()

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
        self.MenuTrabajador.pushButtonRegresar.clicked.connect(self.regresarMenuPrincipal)
        self.MenuTrabajador.pushButton_RegistrarNuevo.clicked.connect(self.irRegistrarTrabajador)
        self.MenuTrabajador.pushButton_BuscarExistente.clicked.connect(self.irBuscarTrabajador)

        # menubar
        self.MenuTrabajador.actionInicio.triggered.connect(self.regresarMenuPrincipal)
        self.MenuTrabajador.actionBonificaciones.triggered.connect(self.irMenuBonificacion)
        self.MenuTrabajador.actionAcercaDeGestorDeSueldosV1.triggered.connect(self.viewFormAcercaDeGestorDeSueldosV1)
        self.MenuTrabajador.actionAcercaDeNosotros.triggered.connect(self.viewFormAcercaDeNosotros)
        self.MenuTrabajador.actionSalir.triggered.connect(self.salir)


class FormRegistrarNuevoTrabajador:
    def __init__(self, parent):
        self.parent = parent
        self.RegistrarNuevoTrabajador = uic.loadUi(f"{directorio_ui}\\TrabajadorRegistrar.ui")
        center(self.RegistrarNuevoTrabajador)
        self.initGUI()

    def mostrar(self):
        self.RegistrarNuevoTrabajador.show()

    def ocultar(self):
        self.RegistrarNuevoTrabajador.close()

    def mostrarError(self, titulo, mensaje):
        errorBox = QMessageBox()
        errorBox.setWindowTitle(titulo)
        errorBox.setText(mensaje)
        errorBox.setIcon(QMessageBox.Icon.Warning)
        errorBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        errorBox.exec()

    def registrar(self):
        try:
            DNI = self.RegistrarNuevoTrabajador.inputDNI.text()
            ApellidosNombres = self.RegistrarNuevoTrabajador.inputNombres.text()
            SueldoBase = self.RegistrarNuevoTrabajador.inputSueldoBasico.text()
            Cargo = self.RegistrarNuevoTrabajador.inputCargo.text()

            # Validar campos vacíos y otras condiciones
            campos_vacios = []

            if DNI.strip() == "":
                campos_vacios.append("DNI")
            elif not DNI.isdigit() or len(DNI) != 8:
                self.mostrarError("Error de validación", "El DNI debe contener 8 cifras numéricas")
                return

            if ApellidosNombres.strip() == "":
                campos_vacios.append("Apellidos y Nombres")
            elif len(ApellidosNombres) > 50:
                self.mostrarError("Error de validación",
                                  "El campo 'Apellidos y Nombres' no puede tener más de 50 caracteres. Por favor, "
                                  "ingrese una información más corta.")
                return

            if Cargo.strip() == "":
                campos_vacios.append("Cargo")
            elif len(Cargo) > 100:
                self.mostrarError("Error de validación",
                                  "El campo 'Cargo' no puede tener más de 100 caracteres. Por favor, ingrese un cargo "
                                  "más corto.")
                return

            if SueldoBase.strip() == "":
                campos_vacios.append("Sueldo Básico")
            else:
                try:
                    SueldoBase = float(SueldoBase)
                    if SueldoBase > 15000:
                        self.mostrarError("Error de validación", "El Sueldo Básico no debe ser mayor a 15000.00")
                        return
                except ValueError:
                    self.mostrarError("Error de valor", "El campo 'Sueldo Básico' debe contener un número")
                    return

            if campos_vacios:
                if len(campos_vacios) == 1:
                    mensaje = f"El campo {', '.join(campos_vacios)} está vacío"
                else:
                    mensaje = f"Los campos: {', '.join(campos_vacios)} están vacíos"

                self.mostrarError("Error de validación", mensaje)
            else:
                Insert.insertTrabajador(DNI, ApellidosNombres, SueldoBase, Cargo)

        except Exception as e:
            print(f"Surgió el siguiente error al registrar trabajador: {e}")

    def cancelar(self):
        self.parent.showMenuTrabajador()

    def initGUI(self):
        # botones
        self.RegistrarNuevoTrabajador.pushButton_Registrar.clicked.connect(self.registrar)
        self.RegistrarNuevoTrabajador.pushButton_Cancelar.clicked.connect(self.cancelar)
        self.RegistrarNuevoTrabajador.dateEditFechaActual.setDate(QDate.currentDate())


class FormBuscarExistenteTrabajador:
    def __init__(self, parent):
        self.parent = parent
        self.BuscarExistenteTrabajador = uic.loadUi(f"{directorio_ui}\\TrabajadorBuscar.ui")
        center(self.BuscarExistenteTrabajador)
        self.initGUI()

    def mostrar(self):
        self.BuscarExistenteTrabajador.show()

    def ocultar(self):
        self.BuscarExistenteTrabajador.close()

    def regresar(self):
        self.parent.showMenuTrabajador()

    def viewInspeccionarTrabajador(self):
        self.parent.showInspeccionarTrabajador()

    def initGUI(self):
        self.BuscarExistenteTrabajador.pushButtonRegresar.clicked.connect(self.regresar)
        self.BuscarExistenteTrabajador.dateEditFechaActual.setDate(QDate.currentDate())
        self.BuscarExistenteTrabajador.pushButtonVerTrabajador.clicked.connect(self.viewInspeccionarTrabajador)


class FormInspeccionarTrabajador:
    def __init__(self, parent):
        self.parent = parent
        self.InspeccionarTrabajador = uic.loadUi(f"{directorio_ui}\\TrabajadorInspeccionar.ui")
        center(self.InspeccionarTrabajador)
        self.initGUI()

    def mostrar(self):
        self.InspeccionarTrabajador.show()

    def ocultar(self):
        self.InspeccionarTrabajador.close()

    def regresar(self):
        self.parent.showBuscarExistenteTrabajador()

    def initGUI(self):
        pass
