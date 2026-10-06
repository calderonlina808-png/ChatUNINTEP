from datetime import datetime




class institucion:
    """Representa la institución educativa asociada al chat universitario"""

    def __init__(self, nombre, usuarios, dominio_correo):
        """Inicializa una institución con su nombre, lista de usuarios y dominio de correo"""
        self.nombre = nombre
        self.usuarios = usuarios
        self.dominio_correo = dominio_correo

    def agregar_usuarios(self, usuarios):
        """Agrega un nuevo usuario a la lista de usuarios de la institución"""
        self.usuarios.append(usuarios)

    def remover_usuarios(self, usuarios):
        """Remueve un usuario de la lista de usuarios de la institución"""
        self.usuarios.remove(usuarios)

    def contar_usuarios(self):
        """Cuenta los usuarios de la lista de usuarios de la institución"""
        return len(self.usuarios)

    def buscar_usuarios(self, usuarios):
        """Busca un usuario dentro de la lista de la institución"""
        if usuarios in self.usuarios:
            return "Se encontro al usuario"
        else:
            return "No se encontro al usuario"

    def verificar_correo(self, correo_electronico):
        """Verifica que un correo pertenezca al dominio institucional"""
        if correo_electronico.endswith(self.dominio_correo):
            return "correo valido"
        else:
            return "correo no valido"

    def __str__(self):
        """Define cómo se muestra la institución al imprimirla"""
        return f"Institución: {self.nombre} | Usuarios registrados: {self.contar_usuarios()}"




class Notificacion:
    """Representa un aviso enviado a un usuario dentro del sistema de chat universitario"""

    def __init__(self, id_notificacion, contenido, usuario_destino):
        """Inicializa una notificación con su id, contenido y usuario destinatario"""
        self.id_notificacion = id_notificacion
        self.contenido = contenido
        self.fecha_hora = datetime.now()
        self.leido = False
        self.usuario_destino = usuario_destino

    def marcar_leido(self):
        """Marca la notificación como leída por el usuario"""
        self.leido = True
        print(f"Notificación {self.id_notificacion} marcada como leída")

    def __str__(self):
        """Define cómo se muestra la notificación al imprimirla"""
        estado = "Leída" if self.leido else "No leída"

        return (
            f"[{estado}] {self.contenido} "
            f"({self.fecha_hora.strftime('%d/%m/%Y %H:%M')})"
        )



if __name__ == "__main__":

    # --- Usuarios simples ---
    usuario1 = usuario("Carla Moreno", "carla@mail.com", 123456, "00000")
    usuario2 = usuario("Ramón Gil", "ramon@mail.com", 234567, "00000")
    usuario3 = usuario("Juan Pérez", "juan@mail.com", 345678, "00000")
    usuario4 = usuario("María López", "maria@mail.com", 456789, "00000")
    usuario5 = usuario("Luis Torres", "luis@mail.com", 567890, "00000")

    # --- Estudiantes ---
    estudiante1 = Estudiante(
        "lina marcela",
        "lina@mail.com",
        120294587,
        "000001",
        3,
        "sistemas y redes"
    )

    estudiante2 = Estudiante(
        "carlos perez",
        "carlos@mail.com",
        120294588,
        "000002",
        5,
        "ingenieria de software"
    )

    estudiante3 = Estudiante(
        "ana torres",
        "ana@mail.com",
        120294589,
        "000003",
        1,
        "seguridad informatica"
    )

    # --- Docentes ---
    docente1 = Docente(
        "hermes ortiz",
        "hermes@mail.com",
        234567241,
        "00000h",
        "programacion"
    )

    docente2 = Docente(
        "laura gomez",
        "laura@mail.com",
        234567242,
        "00000l",
        "bases de datos"
    )

    docente3 = Docente(
        "jorge diaz",
        "jorge@mail.com",
        234567243,
        "00000j",
        "redes"
    )

    # --- Probar inicio y cierre de sesión ---
    estudiante1.iniciar_sesion("000001")
    estudiante1.ver_notas()
    estudiante1.cerrar_sesion()

    print("---")

    docente1.iniciar_sesion("00000h")
    docente1.registrarMaterias()
    docente1.cerrar_sesion()

    print("---")

    # --- Crear institución ---
    chatunintep = institucion(
        "UNINTEP",
        [],
        "@mail.com"
    )

    # --- Agregar todos los usuarios ---
    todos_los_usuarios = [
        usuario1,
        usuario2,
        usuario3,
        usuario4,
        usuario5,
        estudiante1,
        estudiante2,
        estudiante3,
        docente1,
        docente2,
        docente3
    ]

    for u in todos_los_usuarios:
        chatunintep.agregar_usuarios(u)

    # --- Mostrar institución ---
    print(chatunintep)

    # --- Mostrar usuarios registrados ---
    for u in chatunintep.usuarios:
        print(u)

    print("---")

    # --- Verificar correos ---
    print(chatunintep.verificar_correo("lina@mail.com"))
    print(chatunintep.verificar_correo("lina@gmail.com"))

    print("---")

    # --- Crear y probar una notificación ---
    n1 = Notificacion(
        1,
        "Tienes un nuevo mensaje en el grupo Programación 2",
        estudiante1
    )

    print(n1)

    n1.marcar_leido()

    print(n1)