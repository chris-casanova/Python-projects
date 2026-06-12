# ---------- Sección 1: funciones de operación ----------
# Aquí definimos las funciones básicas que realizan operaciones matemáticas.
# Cada función recibe dos argumentos y devuelve el resultado correspondiente.

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # Verificamos que no se intente dividir por cero
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# ---------- Sección 2: función principal ----------
# Esta función controla el flujo principal del programa.
# Muestra instrucciones, lee expresiones del usuario y llama a las funciones anteriores.

def main():
    print("Simple Calculator")
    print("Enter an expression like 2 + 3 or type 'exit' to quit")

    while True:
        # Leer la entrada del usuario y quitar espacios extra
        expression = input("calc> ").strip()

        # Salir si el usuario escribe 'exit' o 'quit'
        if expression.lower() in {"exit", "quit"}:
            print("Goodbye")
            break

        # Si el usuario no escribió nada, volvemos a preguntar
        if not expression:
            continue

        # Separa la expresión en tres partes: número operador número
        parts = expression.split()
        if len(parts) != 3:
            print("Please enter a valid expression with two numbers and an operator")
            continue

        try:
            # Convertir los valores a números flotantes
            x = float(parts[0])
            op = parts[1]
            y = float(parts[2])

            # Dependiendo del operador, llamamos a la función correspondiente
            if op == "+":
                result = add(x, y)
            elif op == "-":
                result = subtract(x, y)
            elif op == "*" or op.lower() == "x":
                result = multiply(x, y)
            elif op == "/":
                result = divide(x, y)
            else:
                print("Unsupported operator. Use +, -, *, or /")
                continue

            # Mostrar el resultado de la operación
            print(result)
        except ValueError as e:
            # Capturamos errores como "división por cero" o conversión fallida
            print(f"Error: {e}")
        except Exception:
            # Capturamos otros errores generales
            print("Invalid input. Use numbers and an operator like 4 + 5")


# ---------- Sección 3: punto de entrada ----------
# Esto permite ejecutar el programa como script.
# Si el archivo se importa como módulo, esta parte no se ejecuta.

if __name__ == "__main__":
    main()
