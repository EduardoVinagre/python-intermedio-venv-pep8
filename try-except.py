a = 1
b = 1
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("The result is: ", result)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")