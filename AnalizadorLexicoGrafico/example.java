import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); //Inicializa Scanner
        /*Ejemplo de scanner basico Scanner scanner = new Scanner(System.in); */
        System.out.println("Ingrese el primer numero:");
        double num1 = scanner.nextDouble();

        System.out.println("Ingrese el segundo numero:");
        double num2 = scanner.nextDouble();

        System.out.println("Ingrese la operacion (+, -, *, /):");
        char operator = scanner.next().charAt(0);

        double result;

        switch (operator) {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                result = num1 / num2;
                break;
            default:
                System.out.println("Operación no válida");
                return;
        }

        System.out.println("El resultado es: " + result);
    }
}