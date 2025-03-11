def calculator():
    # Start of the calculator function

    try:
        # Try to execute the following code block
        num1 = float(input("Enter the first number: "))
        # Prompt the user to enter the first number and convert it to a float
        num2 = float(input("Enter the second number: "))
        # Prompt the user to enter the second number and convert it to a float
        operation = input("Enter the operation (+, -, *, /): ")
        # Prompt the user to enter the desired operation

        if operation == "+":
            # Check if the operation is addition
            result = num1 + num2
            # Perform addition
        elif operation == "-":
            # Check if the operation is subtraction
            result = num1 - num2
            # Perform subtraction
        elif operation == "*":
            # Check if the operation is multiplication
            result = num1 * num2
            # Perform multiplication
        elif operation == "/":
            # Check if the operation is division
            if num2 == 0:
                # Check if the second number is zero to avoid division by zero
                print("Error: Division by zero")
                # Print an error message
                return
                # Exit the function
            result = num1 / num2
            # Perform division
        else:
            # If the operation is not one of the expected ones
            print("Invalid operation")
            # Print an error message
            return
            # Exit the function

        print(f"{num1} {operation} {num2} = {result}")
        # Print the result of the operation

    except ValueError:
        # If a ValueError occurs (e.g., invalid input)
        print("Invalid input. Please enter valid numbers.")
        # Print an error message

if __name__ == "__main__":
    # Check if the script is being run directly
    calculator()
    # Call the calculator function
