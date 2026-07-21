try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    operation = input("Enter the operation (+, -, *, /): ")
except ValueError:
    print("Invalid input! Please enter valid numbers.")

if operation == "+":
    def add(a, b):
        return a + b
    print("The answer is:", add(a, b))

elif operation == "-":
    def subtract(a, b):
        return a - b
    print("The answer is:", subtract(a, b))

elif operation == "*":
    def multiply(a, b):
        return a * b
    print("The answer is:", multiply(a, b))
  
elif operation == "/":
    def divide(a, b):
        if b == 0:
            return "Invalid input! You cannot divide by 0!"
        else:
            return a / b
    print("The answer is:", divide(a, b))

else:
    print("That is not an operation we can do. Please enter one of these: +, -, *, /")