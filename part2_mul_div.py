# Part 2: Multiplication and Division
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
    print("Division of the two numbers is:", division)
else:
    print("Error: Division by zero is not allowed.")

print("Multiplication of the two numbers is:", multiplication)
