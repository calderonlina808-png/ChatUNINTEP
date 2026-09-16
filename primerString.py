class usuario:
    """DOCUMENTACION"""
    """REPRESENTA UN USUARIO REGISTRADO EN CHAT UNINTEP"""
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
    def enviar_Mensaje(self):
       """ ENVIAR UN MENSAJE A OTRO USUARIO  """
    
    def consultarInformacion(self):
      """    CONSULTAR LA INFORMACION DEL USUARIO """

usuario1 = usuario("Lina", "lina@unintep.edu.co")
usuario2 = usuario("Ana", "ana@unintep.edu.co")
usuario3 = usuario("Sol", "sol@unintep.edu.co")

print(usuario.__doc__)
print(usuario1.enviar_Mensaje.__doc__)