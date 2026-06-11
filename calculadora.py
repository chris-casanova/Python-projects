def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    print("Simple Calculator")
    print("Enter an expression like 2 + 3 or type 'exit' to quit")

    while True:
        expression = input("calc> ").strip()
        if expression.lower() in {"exit", "quit"}:
            print("Goodbye")
            break
        if not expression:
            continue

        parts = expression.split()
        if len(parts) != 3:
            print("Please enter a valid expression with two numbers and an operator")
            continue

        try:
            x = float(parts[0])
            op = parts[1]
            y = float(parts[2])

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

            print(result)
        except ValueError as e:
            print(f"Error: {e}")
        except Exception:
            print("Invalid input. Use numbers and an operator like 4 + 5")

if __name__ == "__main__":
    main()
