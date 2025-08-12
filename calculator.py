print("\nBasic Calculator")
print("Operations available: + (addition), - (subtraction), * (multiplication), / (division)\n")

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ").strip()
    
    if operation == '+':
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")
    elif operation == '/':
        if num2 == 0:
            print("\nError: Division by zero is not allowed!")
        else:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("\nInvalid operation! Please enter one of: +, -, *, /")

except ValueError:
    print("\nError: Please enter valid numbers!")
