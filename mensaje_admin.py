class Mensaje:
    """Representa un mensaje enviado en un grupo o chat"""

    def __init__(self, usuario, contenido, id_mensaje=None, fecha=None, destinatario=None):
        self.id_mensaje = id_mensaje
        self.usuario = usuario
        self.remitente = usuario  # Alias para compatibilidad
        self.contenido = contenido
        self.fecha = fecha if fecha else datetime.now()
        self.destinatario = destinatario

    def enviar(self):
        print(f"Mensaje enviado por {self.usuario.nombre}")

    def recibir(self):
        if self.destinatario:
            print(f"Mensaje recibido por {self.destinatario.nombre}")

    def eliminar(self):
        self.contenido = ""
        print("Mensaje eliminado.")

    def __str__(self):
        return f"{self.usuario.nombre}: {self.contenido}"

class Grupo:
    def __init__(self, nombre_grupo, apodo_grupo):
        self.nombre_grupo = nombre_grupo
        self.apodo_grupo = apodo_grupo
        self.participantes = []
        self.mensajes = []

    def agregar_participante(self, usuario):
        self.participantes.append(usuario)
        print(f"{usuario.nombre} fue agregado al grupo.")

    def remover_participante(self, usuario):
        if usuario in self.participantes:
            self.participantes.remove(usuario)
            print(f"{usuario.nombre} fue removido del grupo.")
        else:
            print("El usuario no pertenece al grupo.")

    def contar_participantes(self):
        return len(self.participantes)

    def enviar_mensaje_grupo(self, mensaje):
        self.mensajes.append(mensaje)
        print("Mensaje enviado al grupo.")

    def mostrar_mensajes(self):
        print(f"\n--- Mensajes del grupo {self.apodo_grupo} ---")
        if not self.mensajes:
            print("No hay mensajes.")
        else:
            for mensaje in self.mensajes:
                print(mensaje)

class Administrador(usuario):
    """Representa un administrador con permisos especiales sobre el contenido y los grupos"""

    def __init__(self, nombre, correo="", identificacion="", contraseña=""):
        super().__init__(nombre, correo, identificacion, contraseña)
        self.lista_permisos = []

    def eliminar_mensajes(self, grupo):
        grupo.mensajes.clear()
        print("Todos los mensajes fueron eliminados.")

    def gestionar_contenido(self, contenido):
        print(f"El administrador está gestionando el contenido: {contenido}")
