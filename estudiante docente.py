gitclass Estudiante(Usuario):
    def __init__(self, nombre, correo, identificacion, contrasena, semestre: int, carrera: str):
        super().__init__(nombre, correo, identificacion, contrasena)
        self.semestre = semestre
        self.carrera = carrera

    def ver_notas(self):
        print(f"{self.nombre} de {self.carrera} semestre {self.semestre} esta viendo sus notas")

    def inscribir_materia(self, materia):
        print(f"{self.nombre} se inscribio en {materia}")

class Docente(Usuario):
    def __init__(self, nombre, correo, identificacion, contrasena, materiasAsignadas: str):
        super().__init__(nombre, correo, identificacion, contrasena)
        self.materiasAsignadas = materiasAsignadas

    def registrarMaterias(self):
        print(f"Docente {self.nombre} registro: {self.materiasAsignadas}")

e1 = Estudiante("lina marcela", "lina@mail.com", 120294587, "00000l", 3, "sistemas y redes")
d1 = Docente("hermes ortiz", "hermes@mail.com", 234567241, "00000h", "ingeniero")

e1.iniciar_sesion()
e1.ver_notas()
e1.inscribir_materia("programacion")
e1.cerrar_sesion()
print("---")
d1.iniciar_sesion()
d1.registrarMaterias()
d1.cerrar_sesion()