class Estudiante(Usuario):
    """Representa un estudiante registrado en el chap unitep."""

    def __init__(self, nombre, correo, identificacion, contrasena, semestre: int, carrera: str):
        """Inicializa un estudiante con su semestre y carrera."""
        super().__init__(nombre, correo, identificacion, contrasena)
        self.semestre = semestre
        self.carrera = carrera

    def ver_notas(self):
        """Muestra las notas del estudiante."""
        print(f"{self.nombre} de {self.carrera} semestre {self.semestre} esta viendo sus notas")

    def inscribir_materia(self, materia):
        """Inscribe al estudiante en una materia."""
        print(f"{self.nombre} se inscribio en {materia}")

class Docente(Usuario):
    """Representa un docente registrado en el chap unitep."""

    def __init__(self, nombre, correo, identificacion, contrasena, materiasAsignadas: str):
        """Inicializa un docente con sus materias asignadas."""
        super().__init__(nombre, correo, identificacion, contrasena)
        self.materiasAsignadas = materiasAsignadas

    def registrarMaterias(self):
        """Registra las materias asignadas al docente."""
        print(f"Docente {self.nombre} registro: {self.materiasAsignadas}")

# --- 3 OBJETOS DE ESTUDIANTE ---
estudiante1 = Estudiante("lina marcela", "lina@mail.com", 120294587, "000001", 3, "sistemas y redes")
estudiante2 = Estudiante("carlos perez", "carlos@mail.com", 120294588, "000002", 5, "ingenieria de software")
estudiante3 = Estudiante("ana torres", "ana@mail.com", 120294589, "000003", 1, "seguridad informatica")

# --- 3 OBJETOS DE DOCENTE ---
docente1 = Docente("hermes ortiz", "hermes@mail.com", 234567241, "00000h", "programacion")
docente2 = Docente("laura gomez", "laura@mail.com", 234567242, "00000l", "bases de datos")
docente3 = Docente("jorge diaz", "jorge@mail.com", 234567243, "00000j", "redes")

# --- PRUEBA CON PARAMETRO DENTRO DEL PARENTESIS ---
estudiante1.iniciar_sesion("000001")
estudiante1.ver_notas()
estudiante1.cerrar_sesion()

docente1.iniciar_sesion("00000h")
docente1.registrarMaterias()
docente1.cerrar_sesion() 