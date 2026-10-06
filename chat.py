class ForoUniversitario:
    """Representa el foro donde los usuarios publican temas y respuestas"""

    def _init_(self):
        """Inicializa el foro con una lista vacía de temas"""
        self.temas = []

    def publicar_tema(self, titulo, contenido, autor):
        """Publica un nuevo tema en el foro, indicando su autor"""
        tema = {"titulo": titulo, "contenido": contenido, "autor": autor, "respuestas": []}
        self.temas.append(tema)
        print(f"{autor.nombre} publicó el tema '{titulo}' en el foro")


# ======================= CHAT DE CURSO =======================
class ChatDeCurso:
    """Representa el chat de un curso específico, donde los usuarios envían mensajes"""

    def _init_(self, nombre_curso):
        """Inicializa un chat de curso con su nombre y listas vacías de mensajes y participantes"""
        self.nombre_curso = nombre_curso
        self.lista_mensajes = []
        self.participantes = []

    def enviar_mensaje(self, remitente, contenido):
        """Crea un mensaje y lo agrega al historial del chat del curso"""
        nuevo_mensaje = Mensaje(remitente, contenido, self.nombre_curso)
        self.lista_mensajes.append(nuevo_mensaje)

    def recibir_mensajes(self):
        """Muestra todos los mensajes enviados en el chat del curso"""
        for msj in self.lista_mensajes:
            print(msj)


# ======================= MODULO ACADEMICO =======================
class ModuloAcademico:
    """Representa el módulo que administra horarios y notas de los estudiantes"""

    def _init_(self):
        """Inicializa el módulo con diccionarios vacíos de horarios y notas"""
        self.horarios = {}
        self.notas = {}

    def registrar_horario(self, estudiante, horario):
        """Registra el horario de un estudiante, usando su identificación como clave"""
        self.horarios[estudiante.identificacion] = horario

    def registrar_nota(self, estudiante, materia, nota):
        """Registra la nota de un estudiante en una materia específica"""
        if estudiante.identificacion not in self.notas:
            self.notas[estudiante.identificacion] = {}
        self.notas[estudiante.identificacion][materia] = nota


# ======================= CHATBOT UNIVERSITARIO (integra todo) =======================
class ChatbotUniversitario:
    """Clase central que integra usuarios, foro, chats de curso y módulo académico"""

    def _init_(self):
        """Inicializa el chatbot con sus listas y módulos vacíos"""
        self.lista_usuarios = []
        self.foro = ForoUniversitario()
        self.chats_cursos = {}
        self.modulo_academico = ModuloAcademico()

    def registrar_usuario(self, usuario_creado):
        """Registra un usuario (usuario, Estudiante o Docente) ya creado en el sistema"""
        self.lista_usuarios.append(usuario_creado)
        return usuario_creado

    def crear_chat_curso(self, nombre_curso):
        """Crea un nuevo chat de curso y lo guarda por nombre"""
        nuevo_chat = ChatDeCurso(nombre_curso)
        self.chats_cursos[nombre_curso] = nuevo_chat
        return nuevo_chat


# ======================= PRUEBAS INTEGRADAS =======================
if _name_ == "_main_":
    # --- Usuarios "simples" (sin rol específico) ---
    usuario1 = usuario("Carla Moreno", "carla@mail.com", 123456, "00000")
    usuario2 = usuario("Ramón Gil", "ramon@mail.com", 234567, "00000")
    usuario3 = usuario("Juan Pérez", "juan@mail.com", 345678, "00000")
    usuario4 = usuario("María López", "maria@mail.com", 456789, "00000")
    usuario5 = usuario("Luis Torres", "luis@mail.com", 567890, "00000")

    # --- Estudiantes ---
    estudiante1 = Estudiante("lina marcela", "lina@mail.com", 120294587, "000001", 3, "sistemas y redes")
    estudiante2 = Estudiante("carlos perez", "carlos@mail.com", 120294588, "000002", 5, "ingenieria de software")
    estudiante3 = Estudiante("ana torres", "ana@mail.com", 120294589, "000003", 1, "seguridad informatica")

    # --- Docentes ---
    docente1 = Docente("hermes ortiz", "hermes@mail.com", 234567241, "00000h", "programacion")
    docente2 = Docente("laura gomez", "laura@mail.com", 234567242, "00000l", "bases de datos")
    docente3 = Docente("jorge diaz", "jorge@mail.com", 234567243, "00000j", "redes")

    # Probar inicio/cierre de sesión
    estudiante1.iniciar_sesion("000001")
    estudiante1.ver_notas()
    estudiante1.cerrar_sesion()
    print("---")

    docente1.iniciar_sesion("00000h")
    docente1.registrarMaterias()
    docente1.cerrar_sesion()
    print("---")

    # --- Crear institución y agregar TODOS los usuarios creados ---
    chatunintep = institucion("UNINTEP", [], "@mail.com")

    todos_los_usuarios = [
        usuario1, usuario2, usuario3, usuario4, usuario5,
        estudiante1, estudiante2, estudiante3,
        docente1, docente2, docente3
    ]

    for u in todos_los_usuarios:
        chatunintep.agregar_usuarios(u)

    print(chatunintep)
    for u in chatunintep.usuarios:
        print(u)

    print("---")
    print(chatunintep.verificar_correo("lina@mail.com"))
    print(chatunintep.verificar_correo("lina@gmail.com"))
    print("---")

    # --- Probar Notificacion con un usuario real ---
    n1 = Notificacion(1, "Tienes un nuevo mensaje en el grupo Programación 2", estudiante1)
    print(n1)
    n1.marcar_leido()
    print(n1)
    print("---")

    # --- Probar ChatbotUniversitario, ForoUniversitario y ChatDeCurso ---
    bot = ChatbotUniversitario()
    bot.registrar_usuario(estudiante2)
    bot.registrar_usuario(docente2)

    chat_programacion = bot.crear_chat_curso("Proyecto Programación")
    chat_programacion.enviar_mensaje(estudiante2, "Hola profe")
    chat_programacion.enviar_mensaje(docente2, "Hola Carlos")
    chat_programacion.recibir_mensajes()

    bot.foro.publicar_tema("Dudas", "Ayuda con el codigo", estudiante2)