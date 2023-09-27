fun main() {
    println("Calculadora básica en Kotlin")

    // Pedir al usuario que ingrese dos números y la operación
    print("Ingrese el primer número: ")
    val num1 = readLine()!!.toDouble()
    print("Ingrese la operación (+, -, *, /): ")
    val operacion = readLine()!!
    print("Ingrese el segundo número: ")
    val num2 = readLine()!!.toDouble()

    // Realizar la operación correspondiente
    val resultado = when (operacion) {
        "+" -> num1 + num2
        "-" -> num1 - num2
        "*" -> num1 * num2
        "/" -> num1 / num2
        else -> throw IllegalArgumentException("Operación inválida: $operacion")
    }

    // Mostrar el resultado al usuario
    println("El resultado de $num1 $operacion $num2 es $resultado")
}