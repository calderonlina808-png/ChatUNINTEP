class institucion:
    """REPRESENTA UN USUARIO REGISTRADO EN CHAT UNINTEP"""

    def __init__(self, nombre, usuarios, dominio_correo):
        self.nombre = nombre
        self.usuarios = usuarios
        self.dominio_correo = dominio_correo

    def agregar_usuarios(self, usuarios):
        """Agrega un nuevo usuario a la lista de usuarios de la institucion"""
        self.usuarios.append(usuarios)
    def remover_usuarios(self, usuarios):
        """Remueve un usuario de la lista de usuarios de la institucion"""
        self.usuarios.remove(usuarios)

    def contar_usuarios(self):
        """Cuenta los usuarios de la lista de usuarios de la institucion"""
        return(len(self.usuarios))
    
    def buscar_usuarios(self, usuarios):
        """Busca los usuarios en la lista de la institucion"""
        if usuarios in self.usuarios:
    
            return("Se encontro al usuario")
        else:
            return("No se encontro al usuario")

    def verificar_correo(self, correo_electronico):
        """Se hace la verificacion del correo de la institucion"""
        if correo_electronico.endswith(self.dominio_correo):
            return("correo valido")
        else:
            return("correo no valido")