class NumeroNegativoError(Exception):
    pass

class EntradaDatos:

    # validaciones
    @staticmethod
    def validar_numero_positivo(mensaje_ingreso, mensaje_error):
        while True:
            try:
                num = float(input(mensaje_ingreso))
                if num < 0:
                    raise NumeroNegativoError(mensaje_error)
                return num
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")
            except NumeroNegativoError as e:
                print(f"Error: {e}")

    @staticmethod
    def validar_entero_positivo(mensaje_ingreso, mensaje_error):
        while True:
            try:
                num = int(input(mensaje_ingreso))
                if num < 0:
                    raise NumeroNegativoError(mensaje_error)
                return num
            except ValueError:
                print("Error: Ingrese un valor entero válido.")
            except NumeroNegativoError as e:
                print(f"Error: {e}")

    # ingreso de datos
    @staticmethod
    def obtener_datos_usuario():
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        return username, password

    # ultima_id = 0
    @staticmethod
    def obtener_datos_trabajador():
        # EntradaDatos.ultima_id += 1  # Incrementa la última ID generada
        # IdTrabajador = EntradaDatos.ultima_id  # Asigna la nueva ID al trabajador
        IdTrabajador = EntradaDatos.validar_entero_positivo("Ingrese el ID del trabajador (DNI): ",
                                                             "No puede ser negativo")

        nombreTrabajador = input("Ingrese el nombre del trabajador: ")
        sueldo_basico = EntradaDatos.validar_numero_positivo("Ingrese el valor del sueldo básico: ",
                                                             "El sueldo básico no puede ser negativo")
        dias_falta = EntradaDatos.validar_entero_positivo("Ingrese la cantidad de días de falta: ",
                                                          "Los días de falta no pueden ser negativos")
        minutosTardanza = EntradaDatos.validar_entero_positivo("Ingrese el total de minutos de tardanza: ",
                                                               "Los minutos de tardanza no pueden ser negativos")
        horas_extras = EntradaDatos.validar_entero_positivo("Ingrese la cantidad de horas extras trabajadas: ",
                                                           "Las horas extras no pueden ser negativas.")
        return IdTrabajador, nombreTrabajador, sueldo_basico, dias_falta, minutosTardanza, horas_extras
