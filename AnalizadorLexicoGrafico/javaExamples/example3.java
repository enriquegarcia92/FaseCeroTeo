import java.util.Scanner;

public class SaludoPersonalizado{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String nombre;
        char continue;

        do {
            System.out.println("Por favor, ingrese su nombre:");
            nombre = scanner.nextLine();

            System.out.println("¡Hola, " + nombre + "! Bienvenido al programa.");

            System.out.println("¿Desea continuar? (S para sí, cualquier otra tecla para salir):");
            continue = scanner.next().charAt(0);
            scanner.nextLine();

            switch (continue) {
                case 'S':
                case 's':
                    System.out.println("Continuando...");
                    break;
                default:
                    System.out.println("Saliendo del programa.");
                    return;
            }

        } while (true);
    }
}
