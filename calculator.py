print("Welcome to Simple Calculator!")
num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == '+':
    print(f"The result is: {num1 + num2}")
elif operator == '-':
    print(f"The result is: {num1 - num2}")
elif operator == '*':
    print(f"The result is: {num1 * num2}")
elif operator == '/':
    if num2 != 0:
        print(f"The result is: {num1 / num2}")
    else:
        print("Error! Division by zero.")
else:
    print("Invalid operator!")
