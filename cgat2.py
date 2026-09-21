from abc import ABC, abstractmethod

class Chat(ABC):
    """
    Clase abstracta CHAT basada en el diagrama de clases,
    con atributos de listas y métodos abstractos para enviar y recibir mensajes.
    """
    def __init__(self):
        self.lista_usuarios = []
        self.lista_mensajes = []

    @abstractmethod
    def recibirMensaje(self, mensaje: str) -> None:
        """Método abstracto para manejar la recepción de mensajes."""
        pass

    @abstractmethod
    def enviarMensaje(self, mensaje: str) -> None:
        """Método abstracto para manejar el envío de mensajes."""
        pass


# Ejemplo de cómo se implementaría en una clase concreta heredando de Chat:
class ChatPrivado(Chat):
    def recibirMensaje(self, mensaje: str) -> None:
        self.lista_mensajes.append(mensaje)
        print(f"Mensaje recibido: {mensaje}")

    def enviarMensaje(self, mensaje: str) -> None:
        self.lista_mensajes.append(mensaje)
        print(f"Mensaje enviado: {mensaje}")


# Código de prueba para verificar que funciona sin errores
if __name__ == "__main__":
    mi_chat = ChatPrivado()
    mi_chat.enviarMensaje("¡Hola, este es un mensaje de prueba!")
    mi_chat.recibirMensaje("¡Hola! ¿Cómo estás?")
    
    print("Usuarios actuales:", mi_chat.lista_usuarios)
    print("Historial de mensajes:", mi_chat.lista_mensajes)