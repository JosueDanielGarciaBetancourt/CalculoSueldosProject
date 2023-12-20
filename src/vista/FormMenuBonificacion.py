import re
from sqlite3 import DatabaseError

from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QDate, Qt
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
from vista.Window_Utils import center, MensajesWindow, returnDirectorioGUI
from logica.Inserts import Inserts
from logica.Queries import Queries
from logica.Updates import Updates
from logica.Deletes import Deletes
from src.logica import Deletes

directorio_ui = returnDirectorioGUI()


class FormMenuBonificacion:
    def __init__(self, parent):
        self.parent = parent
        self.MenuBonificacion = uic.loadUi(f"{directorio_ui}MenuBonificacion.ui")
        center(self.MenuBonificacion)
        self.initGUI()

    def mostrar(self):
        self.MenuBonificacion.show()

    def ocultar(self):
        self.MenuBonificacion.close()

    def deshabilitarBarraMenu(self):
        self.MenuBonificacion.menubarMenuBonificacion.setEnabled(False)

    def deshabilitarBotones(self):
        self.MenuBonificacion.pushButtonBuscarBonificaciones.setEnabled(False)
        self.MenuBonificacion.pushButtonRegresar.setEnabled(False)

    def habilitarBarraMenu(self):
        self.MenuBonificacion.menubarMenuBonificacion.setEnabled(True)

    def habilitarBotones(self):
        self.MenuBonificacion.pushButtonBuscarBonificaciones.setEnabled(True)
        self.MenuBonificacion.pushButtonRegresar.setEnabled(True)

    def salir(self):
        self.parent.deshabilitarLosBotones()
        self.parent.deshabilitarLaBarraMenu()
        self.parent.showMenuPrincipalSalir()

    def irBonificacionVerModificar(self):
        self.parent.showBonificacionVerModificar()

    def regresarMenuPrincipal(self):
        self.parent.showMenuPrincipal()

    def irMenuTrabajador(self):
        self.parent.showMenuTrabajador()

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
        self.MenuBonificacion.pushButtonRegresar.clicked.connect(self.regresarMenuPrincipal)
        self.MenuBonificacion.pushButtonBuscarBonificaciones.clicked.connect(self.irBonificacionVerModificar)

        # menubar
        self.MenuBonificacion.actionInicio.triggered.connect(self.regresarMenuPrincipal)
        self.MenuBonificacion.actionTrabajador.triggered.connect(self.irMenuTrabajador)
        self.MenuBonificacion.actionAcercaDeGestorDeSueldosV1.triggered.connect(self.viewFormAcercaDeGestorDeSueldosV1)
        self.MenuBonificacion.actionAcercaDeNosotros.triggered.connect(self.viewFormAcercaDeNosotros)
        self.MenuBonificacion.actionSalir.triggered.connect(self.salir)


class FormBonificacionVerModificar:
    def __init__(self, parent):
        self.parent = parent
        self.BonificacionVerModificar = uic.loadUi(f"{directorio_ui}\BonificacionVerModificar.ui")
        center(self.BonificacionVerModificar)
        self.tableColumnValorBoniEditable = False  # Variable para rastrear el estado de edición
        self.original_values = []
        self.num_filasGUITableBonificaciones = self.BonificacionVerModificar.tablaBonificaciones.rowCount()
        self.initGUI()

    def mostrar(self):
        self.BonificacionVerModificar.show()

    def ocultar(self):
        self.BonificacionVerModificar.close()

    def regresar(self):
        self.parent.showMenuBonificacion()

    def actualizarContadorNumeroFilas(self):
        self.num_filasGUITableBonificaciones = self.BonificacionVerModificar.tablaBonificaciones.rowCount()

    def verificarSeleccion(self):
        seleccionado = False
        # Obtiene el modelo de selección de la tabla
        selection_model = self.BonificacionVerModificar.tablaBonificaciones.selectionModel()
        # Verifica si hay alguna celda seleccionada en el modelo de selección
        if selection_model.hasSelection():
            seleccionado = True
        return seleccionado

    def generar_nuevo_id(self, id_anterior):
        # Extraer la parte no numérica del ID
        parte_no_numerica = ''.join(filter(str.isalpha, id_anterior))

        # Extraer la parte numérica del ID y convertirla a un entero
        parte_numerica = int(''.join(filter(str.isdigit, id_anterior)))

        # Incrementar el número
        nuevo_numero = parte_numerica + 1

        # Formatear el nuevo ID con la misma estructura
        nuevo_id = f"{parte_no_numerica}{nuevo_numero:02d}"

        return nuevo_id

    def obtener_campos_ultima_fila(self):
        self.actualizarContadorNumeroFilas()
        listaValoresCamposUltimaFila = []
        if self.num_filasGUITableBonificaciones > 0:
            for columna in range(self.BonificacionVerModificar.tablaBonificaciones.columnCount()):
                # Obtiene el contenido de la celda en la última fila y la columna actual
                item = self.BonificacionVerModificar.tablaBonificaciones.item(self.num_filasGUITableBonificaciones - 1,
                                                                              columna)
                listaValoresCamposUltimaFila.append(item.text() if item is not None else "")
        return listaValoresCamposUltimaFila

    def disable_edit_tableBonificacionesRow(self, fila):
        try:
            self.tableColumnValorBoniEditable = not self.tableColumnValorBoniEditable
            num_columnas = self.BonificacionVerModificar.tablaBonificaciones.columnCount()
            for column in range(num_columnas):
                item = self.BonificacionVerModificar.tablaBonificaciones.item(fila - 1, column)
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
        except Exception as e:
            mensaje = f"Ocurrió un error inesperado al intentar habilitar/deshabilitar las columnas de la fila" \
                      f"{fila}, {e}"
            print(mensaje)
            MensajesWindow.mostrarMensajeErrorInesperado(mensaje)

    def agregarBonificacion(self):
        self.BonificacionVerModificar.label_InstruccionAgregar.setVisible(True)
        self.BonificacionVerModificar.label_InstruccionModificar.setVisible(False)
        self.BonificacionVerModificar.pushButton_AgregarBonificacion.setEnabled(True)
        self.actualizarContadorNumeroFilas()
        self.tableColumnValorBoniEditable = not self.tableColumnValorBoniEditable
        print(f"Editable? {self.tableColumnValorBoniEditable}")
        try:
            if self.tableColumnValorBoniEditable:
                self.BonificacionVerModificar.pushButton_AgregarBonificacion.setStyleSheet(
                    "font: 700 15pt 'Calibri';"
                    "color: white;"
                    "border: 1px solid white;"
                    "border-radius: 15px;"
                    "background-color: rgb(41, 11, 11);")
                self.BonificacionVerModificar.pushButton_AgregarBonificacion.setText("Guardar cambios")
                self.BonificacionVerModificar.pushButton_ModificarBonificacion.setEnabled(False)
                self.BonificacionVerModificar.pushButtonRegresar.setEnabled(False)
                self.BonificacionVerModificar.pushButton_EliminarBonificacion.setEnabled(False)
                self.BonificacionVerModificar.tablaBonificaciones.insertRow(self.num_filasGUITableBonificaciones)
                self.actualizarContadorNumeroFilas()
                ultimaBonificacion = Queries.get_last_bonification()
                nuevoIDBonificacion = self.generar_nuevo_id(ultimaBonificacion.IDBonificacion)
                itemNuevoID = QTableWidgetItem(str(nuevoIDBonificacion))
                itemNuevoID.setTextAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
                self.BonificacionVerModificar.tablaBonificaciones.setItem(self.num_filasGUITableBonificaciones - 1,
                                                                          0, itemNuevoID)
                item = self.BonificacionVerModificar.tablaBonificaciones.item(self.num_filasGUITableBonificaciones - 1,
                                                                              0)
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            else:
                self.actualizarContadorNumeroFilas()
                self.BonificacionVerModificar.pushButton_AgregarBonificacion.setStyleSheet(
                    "font: 700 15pt 'Calibri';"
                    "color: white;"
                    "border: 1px solid white;"
                    "border-radius: 15px;"
                    "background-color: rgb(52, 50, 125);")
                self.BonificacionVerModificar.pushButton_AgregarBonificacion.setText("Agregar bonificación")
                self.BonificacionVerModificar.pushButton_ModificarBonificacion.setEnabled(True)
                self.BonificacionVerModificar.pushButtonRegresar.setEnabled(True)
                self.BonificacionVerModificar.pushButton_EliminarBonificacion.setEnabled(True)

                listaValoresCamposUltimaFila = self.obtener_campos_ultima_fila()
                if listaValoresCamposUltimaFila[1] != "" and listaValoresCamposUltimaFila[2] != "" and listaValoresCamposUltimaFila[3] != "":
                    nuevoID_item = self.BonificacionVerModificar.tablaBonificaciones.item(self.num_filasGUITableBonificaciones - 1,
                                                                                  0)
                    listaValoresCamposUltimaFila[0] = nuevoID_item.text()
                    nuevoIDBonificacion = listaValoresCamposUltimaFila[0]
                    nuevoTipoBonificacion = listaValoresCamposUltimaFila[1]
                    nuevaUnidadBonificacion = listaValoresCamposUltimaFila[2]
                    nuevoValorBonificacion = listaValoresCamposUltimaFila[3]

                    Inserts.insertBonificacion(nuevoIDBonificacion, nuevoTipoBonificacion, float(nuevoValorBonificacion))

                    for columna, dato in enumerate(listaValoresCamposUltimaFila):
                        itemNuevaFila = QTableWidgetItem(str(dato))
                        itemNuevaFila.setTextAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
                        self.BonificacionVerModificar.tablaBonificaciones.setItem(self.num_filasGUITableBonificaciones - 1,
                                                                                  columna, itemNuevaFila)
                    self.disable_edit_tableBonificacionesRow(self.num_filasGUITableBonificaciones)
                    self.tableColumnValorBoniEditable = False
                else:
                    self.BonificacionVerModificar.pushButton_AgregarBonificacion.setStyleSheet(
                        "font: 700 15pt 'Calibri';"
                        "color: white;"
                        "border: 1px solid white;"
                        "border-radius: 15px;"
                        "background-color: rgb(41, 11, 11);")
                    self.BonificacionVerModificar.pushButton_AgregarBonificacion.setText("Guardar cambios")
                    self.BonificacionVerModificar.pushButton_ModificarBonificacion.setEnabled(False)
                    self.BonificacionVerModificar.pushButtonRegresar.setEnabled(False)
                    self.BonificacionVerModificar.pushButton_EliminarBonificacion.setEnabled(False)
                    self.tableColumnValorBoniEditable = True
                    MensajesWindow.mostrarMensajeRegistroError("Por favor, ingrese todos los campos")
        except Exception as e:
            mensaje = f"Error inesperador al registrar las bonificaciones: {e}"
            print(mensaje)
            MensajesWindow.mostrarMensajeRegistroError(mensaje)

    def enable_disable_edit_tableBonificacionesColumn3(self):
        try:
            self.tableColumnValorBoniEditable = not self.tableColumnValorBoniEditable
            self.actualizarContadorNumeroFilas()
            for fila in range(self.num_filasGUITableBonificaciones):
                item = self.BonificacionVerModificar.tablaBonificaciones.item(fila, 3)
                if self.tableColumnValorBoniEditable:
                    item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)
                else:
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
        except Exception as e:
            mensaje = f"Ocurrió un error inesperado al intentar habilitar/deshabilitar la columna Valor, {e}"
            print(mensaje)
            MensajesWindow.mostrarMensajeErrorInesperado(mensaje)

    def restaurarValoresCorrectosColumn3(self):
        try:
            print(self.original_values)
            for fila in range(self.num_filasGUITableBonificaciones):
                original_value_item = QTableWidgetItem(str(self.original_values[fila]))
                # | → Es como "mezclar" o combinar las configuraciones individuales en una sola que
                # incluye tanto la alineación horizontal como la vertical.
                original_value_item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
                self.BonificacionVerModificar.tablaBonificaciones.setItem(fila, 3, original_value_item)
        except Exception as e:
            print(f"Ocurrió un error inesperado al regresar a los valores anteriores {e}")

    def modificarGUITableBonificacionesColumn3(self):
        # Habilitar o deshabilitar la edición de la columna 3 "Valor" de la tabla bonificaciones de la GUI
        self.enable_disable_edit_tableBonificacionesColumn3()
        try:
            self.BonificacionVerModificar.label_InstruccionAgregar.setVisible(False)
            if self.tableColumnValorBoniEditable:
                self.BonificacionVerModificar.pushButton_ModificarBonificacion.setEnabled(True)
                self.BonificacionVerModificar.label_InstruccionModificar.setVisible(True)
                self.BonificacionVerModificar.pushButton_ModificarBonificacion.setStyleSheet(
                    "font: 700 15pt 'Calibri';"
                    "color: white;"
                    "border: 1px solid white;"
                    "border-radius: 15px;"
                    "background-color: rgb(41, 11, 11);")
                self.BonificacionVerModificar.pushButton_ModificarBonificacion.setText("Guardar cambios")
                self.BonificacionVerModificar.pushButtonRegresar.setEnabled(False)
                self.BonificacionVerModificar.pushButton_AgregarBonificacion.setEnabled(False)
                self.BonificacionVerModificar.pushButton_EliminarBonificacion.setEnabled(False)
            else:
                self.BonificacionVerModificar.label_InstruccionModificar.setVisible(False)
                self.BonificacionVerModificar.pushButton_ModificarBonificacion.setStyleSheet(
                    "font: 700 15pt 'Calibri';"
                    "color: white;"
                    "border: 1px solid white;"
                    "border-radius: 15px;"
                    "background-color: rgb(52, 50, 125);")
                self.BonificacionVerModificar.pushButton_ModificarBonificacion.setText("Modificar bonificación")
                self.BonificacionVerModificar.pushButtonRegresar.setEnabled(True)
                self.BonificacionVerModificar.pushButton_AgregarBonificacion.setEnabled(True)
                self.BonificacionVerModificar.pushButton_EliminarBonificacion.setEnabled(True)
        except Exception as e:
            print(f"Error: {e}")

        # Guardar los valores originales antes de intentar la modificación
        try:
            if self.tableColumnValorBoniEditable:
                self.original_values = []
                for fila in range(self.num_filasGUITableBonificaciones):
                    valorAlmacenadoBonificacion = self.BonificacionVerModificar.tablaBonificaciones.item(fila, 3).text()
                    print(valorAlmacenadoBonificacion)
                    self.original_values.append(valorAlmacenadoBonificacion)
            print(self.original_values)
        except Exception as e:
            print(f"Error inesperado al guardar valores originales {e}")

        # Modificar los valores en la columna 3 "Valor" de la tabla bonificaciones de la GUI
        if not self.tableColumnValorBoniEditable:
            try:
                for fila in range(self.num_filasGUITableBonificaciones):
                    IDBonificacion = self.BonificacionVerModificar.tablaBonificaciones.item(fila, 0).text()
                    nuevoValorBonificacion = self.BonificacionVerModificar.tablaBonificaciones.item(fila, 3).text()
                    try:
                        nuevoValorBonificacion = float(nuevoValorBonificacion)
                    except ValueError:
                        print("No se puede convertir a número")
                        raise ValueError("No se puede convertir a número")

                    if nuevoValorBonificacion <= 0:
                        print("No se permiten valores menores o iguales a 0")
                        raise ValueError("No se permiten valores menores o iguales a 0")

                    if not re.match(r'^[0-9.]+$', str(nuevoValorBonificacion)):
                        print("No se permiten valores que contengan letras")
                        raise ValueError("No se permiten valores que contengan letras")

                    Updates.updateValorBonificacion(IDBonificacion, nuevoValorBonificacion)
                mensaje = f"Modificación realizada correctamente"
                print(mensaje)
                MensajesWindow.mostrarMensajeRegistroExito(mensaje)
            except ValueError as e:
                self.tableColumnValorBoniEditable = False
                self.enable_disable_edit_tableBonificacionesColumn3()
                self.restaurarValoresCorrectosColumn3()
                self.BonificacionVerModificar.pushButton_ModificarBonificacion.setStyleSheet(
                    "font: 700 15pt 'Calibri';"
                    "color: white;"
                    "border: 1px solid white;"
                    "border-radius: 15px;"
                    "background-color: rgb(41, 11, 11);")
                self.BonificacionVerModificar.pushButton_ModificarBonificacion.setText("Guardar cambios")
                mensaje = f"Error inesperado al procesar los valores {nuevoValorBonificacion}: {e}, " \
                          f"por favor ingreses valores numéricos"
                print(mensaje)
                MensajesWindow.mostrarMensajeErrorInesperado(mensaje)
            except Exception as e:
                self.tableColumnValorBoniEditable = False
                self.enable_disable_edit_tableBonificacionesColumn3()
                self.restaurarValoresCorrectosColumn3()
                self.BonificacionVerModificar.pushButton_ModificarBonificacion.setStyleSheet(
                    "font: 700 15pt 'Calibri';"
                    "color: white;"
                    "border: 1px solid white;"
                    "border-radius: 15px;"
                    "background-color: rgb(41, 11, 11);")
                self.BonificacionVerModificar.pushButton_ModificarBonificacion.setText("Guardar cambios")
                mensaje = f"Error inesperado al procesar la modificación: {e}"
                print(mensaje)
                MensajesWindow.mostrarMensajeErrorInesperado(mensaje)

    def eliminarBonificacion(self):
        try:
            self.BonificacionVerModificar.label_InstruccionAgregar.setVisible(False)
            self.BonificacionVerModificar.label_InstruccionModificar.setVisible(False)
            if Queries.get_num_bonificaciones() > 0:
                if self.verificarSeleccion():
                    selectedRow = self.BonificacionVerModificar.tablaBonificaciones.currentRow()
                    selectedIDBonificacion = self.BonificacionVerModificar.tablaBonificaciones.item(selectedRow,
                                                                                                    0).text()
                    selectedTipoBonificacion = self.BonificacionVerModificar.tablaBonificaciones.item(selectedRow,
                                                                                                      1).text()

                    confirmacionEliminar = MensajesWindow.mostrarMensajeConfirmacion("Confirmación de eliminación",
                                                                                     f"Se eliminará la bonificación {selectedTipoBonificacion}. "
                                                                                     f"¿Está seguro de eliminarla?",
                                                                                     QMessageBox.Icon.Question)
                    if confirmacionEliminar == "Sí":
                        Deletes.Deletes.deleteBonificacion(selectedIDBonificacion)
                        selected_row = self.BonificacionVerModificar.tablaBonificaciones.currentRow()
                        self.BonificacionVerModificar.tablaBonificaciones.removeRow(selected_row)
                        self.deseleccionarTabla()
                else:
                    MensajesWindow.mostrarMensajeEliminarError("Selecciona una fila antes de eliminar")
            else:
                MensajesWindow.mostrarMensajeEliminarError("No existen bonificaciones registradas en la base de datos")
        except DatabaseError as de:
            print(f"Error de base de datos al buscar bonificación en la base de datos: {de}")
        except Exception as e:
            mensaje = f"Error inesperado al eliminar bonificación: {e}"
            print(mensaje)
            MensajesWindow.mostrarMensajeEliminarError(mensaje)

    def deseleccionarTabla(self):
        self.BonificacionVerModificar.tablaBonificaciones.clearSelection()

    def initGUI(self):
        self.BonificacionVerModificar.dateEditFechaActual.setDate(QDate.currentDate())
        self.BonificacionVerModificar.pushButtonNoSelection.clicked.connect(self.deseleccionarTabla)
        self.BonificacionVerModificar.dateEditFechaActual.setDate(QDate.currentDate())
        self.BonificacionVerModificar.label_InstruccionAgregar.setVisible(False)
        self.BonificacionVerModificar.label_InstruccionModificar.setVisible(False)

        # botones
        self.BonificacionVerModificar.pushButton_AgregarBonificacion.clicked.connect(self.agregarBonificacion)
        self.BonificacionVerModificar.pushButton_ModificarBonificacion.clicked.connect(
            self.modificarGUITableBonificacionesColumn3)
        self.BonificacionVerModificar.pushButton_EliminarBonificacion.clicked.connect(self.eliminarBonificacion)
        self.BonificacionVerModificar.pushButtonRegresar.clicked.connect(self.regresar)

        # tabla
        self.BonificacionVerModificar.tablaBonificaciones.resizeColumnsToContents()
        self.BonificacionVerModificar.tablaBonificaciones.resizeRowsToContents()

        # En Qt Designer ya se realizó la deshabilitación de edición de todas las celdas
