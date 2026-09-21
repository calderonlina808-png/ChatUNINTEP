class usuario:
    """DOCUMENTACION"""
    """REPRESENTA UN USUARIO REGISTRADO EN CHAT UNINTEP"""

    def __init__(self, nombre, correo, identificacion, contraseña):
        self.nombre = nombre
        self.correo = correo
        self.identificacion = identificacion
        self.__contraseña = contraseña

    def iniciar_sesion(self, contraseña_ingresada):
        """EL USUARIO PUEDE INICIAR SESION EN SU DISPOSITIVO""" #docstring
        if contraseña_ingresada == self.__contraseña:
            print (f"{self.nombre} inicio sesión correctamente")
            return True
        else: 
            print ("contraseña incorrecta")
            return False

    def cerrar_sesion(self):
        """EL USUARION CIERRA SESION DE MANERA SEGURA"""
        print (f"{self.nombre} cerro sesión correctamente")

    def actualizar_perfil(self):
        """EL USUSARIO PUEDE ACTUALIZAR SUS DATOS CADA QUE LO NECESITE"""
        print("¿Qué dato deseas actualizar?")
        print("1. Correo")
        print("2. Contraseña")
        opcion = input("Elige una opción (1 o 2): ")

        if opcion == "1":
            nuevo_correo = input("Ingresa tu nuevo correo: ")
            self.correo = nuevo_correo
            print("Correo actualizado correctamente")

        elif opcion == "2":
            nueva_contraseña = input("Ingresa tu nueva contraseña: ")
            self.__contraseña = nueva_contraseña
            print("Contraseña actualizada correctamente")
        else:
                print("Opción no válida")
  
    def __str__(self):
        return f"Usuario: {self.nombre} | Correo: {self.correo} | ID: {self.identificacion}"

usuario1 = usuario("Carla Moreno", "carla@example.com", 123456, "00000")
usuario2 = usuario("Ramón Gil", "ramon@example.com", 234567 ,"00000")
print(usuario.__doc__)
print(usuario1.iniciar_sesion.__doc__)

usuarios = [usuario1, usuario2]
for u in usuarios:
    print(u)

print("MENÚ: Actualizar datos:")
usuario1.actualizar_perfil()