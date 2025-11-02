ANS = 0  # Stores the last answer

def main():
    global ANS  # So we can update it inside the function

    print("Smart Calculator v1.0")
    print("Type 'exit' anytime to quit.\n")

    while True:
        print(f"Last Result (ANS): {ANS}")  # Show stored value

        num_1 = input("Enter a number: ")
        if num_1.lower() == "exit":
            break

        expression = input("Enter operation (+, -, *, /, //, **, ^): ")
        if expression.lower() == "exit":
            break

        num_2 = input("Enter another number: ")
        if num_2.lower() == "exit":
            break

        # Replace 'ANS' with stored value
        if num_1 == "ANS":
            num_1 = ANS
        if num_2 == "ANS":
            num_2 = ANS

        try:
            num_1 = float(num_1)
            num_2 = float(num_2)

            # Perform operations
            if expression == "+":
                result = num_1 + num_2
            elif expression == "-":
                result = num_1 - num_2
            elif expression == "*":
                result = num_1 * num_2
            elif expression == "/":
                result = num_1 / num_2
            elif expression == "//":
                result = num_1 // num_2
            elif expression in ["**", "^"]:
                result = num_1 ** num_2
            else:
                print("Invalid operator.")
                continue

            # Print and store
            print(f" Result: {result}\n")
            ANS = result  # Store the last answer

        except ZeroDivisionError:
            print(" Error: Division by zero.\n")
        except ValueError:
            print(" Error: Invalid number.\n")

main()
