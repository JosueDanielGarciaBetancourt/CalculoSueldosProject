class Usuario:
    # Lista para almacenar objetos Usuario
    listaUsuarios = []

    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        Usuario.listaUsuarios.append(self)

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def setUsuario(self, nuevo_username, nuevo_password):
        self.__username = nuevo_username
        self.__password = nuevo_password

    def imprimir_atributos_usuario(self):
        print()
        print(f"El nombre de usuario es: {self.__username}")
        print(f"La contraseña es: {self.__password}\n")
