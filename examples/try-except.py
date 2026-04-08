class DivisionError(Exception):
    """Custom exception for division errors."""

    pass


a = 1
b = 1
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    if b == 2:
        raise DivisionError("b cannot be 2.")
    result = a / b
    print("The result is: ", result)
except DivisionError as e:
    print(f"Custom error occurred: {e}")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except KeyboardInterrupt:
    print("\nError: Input interrupted by the user.")
finally:
    print("This block will always execute, regardless of exceptions.")

print("Continuing with the rest of the program...")
