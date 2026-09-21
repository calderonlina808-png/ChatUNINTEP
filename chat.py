# featured-chat
abstract class Chat {

    protected String nombre;

    public Chat(String nombre) {
        this.nombre = nombre;
    }

    // Método abstracto
    public abstract void enviarMensaje(String mensaje);

    // Método normal
    public void mostrarNombre() {
        System.out.println("================================");
        System.out.println("CHAT: " + nombre);
        System.out.println("================================");
    }
}


// CHATBOT
class Chatbot extends Chat {

    public Chatbot() {
        super("Chatbot");
    }

    @Override
    public void enviarMensaje(String mensaje) {
        System.out.println("Chatbot: Hola, soy el asistente virtual.");
        System.out.println("Mensaje recibido: " + mensaje);
    }
}


// FORO UNIVERSITARIO
class ForoUniversitario extends Chat {

    public ForoUniversitario() {
        super("Foro Universitario");
    }

    @Override
    public void enviarMensaje(String mensaje) {
        System.out.println("Foro Universitario: " + mensaje);
    }
}


// CHAT DE CURSO
class ChatCurso extends Chat {

    public ChatCurso() {
        super("Chat de Curso");
    }

    @Override
    public void enviarMensaje(String mensaje) {
        System.out.println("Chat de Curso: " + mensaje);
    }
}


// MODULO ACADEMICO
class ModuloAcademico extends Chat {

    public ModuloAcademico() {
        super("Modulo Academico");
    }

    @Override
    public void enviarMensaje(String mensaje) {
        System.out.println("Modulo Academico: " + mensaje);
    }
}


// PROGRAMA PRINCIPAL
public class Main {

    public static void main(String[] args) {

        // Crear los diferentes tipos de chat
        Chat chatbot = new Chatbot();
        Chat foro = new ForoUniversitario();
        Chat curso = new ChatCurso();
        Chat modulo = new ModuloAcademico();

        // CHATBOT
        chatbot.mostrarNombre();
        chatbot.enviarMensaje("Necesito ayuda con una tarea.");

        System.out.println();

        // FORO UNIVERSITARIO
        foro.mostrarNombre();
        foro.enviarMensaje("¿Alguien sabe cuándo es el examen?");

        System.out.println();

        // CHAT DE CURSO
        curso.mostrarNombre();
        curso.enviarMensaje("Hola compañeros, ¿ya hicieron la actividad?");

        System.out.println();

        // MODULO ACADEMICO
        modulo.mostrarNombre();
        modulo.enviarMensaje("Consultar mis notas académicas.");