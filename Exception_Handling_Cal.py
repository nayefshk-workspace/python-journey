# ============================================
# Challenge Problem: Calculator
# ============================================
# Create a menu-driven calculator.
#
# Menu:
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
#
# Requirements:
# 1. Ask the user to choose an operation.
# 2. Ask the user for two numbers.
# 3. Perform the selected operation.
#
# Handle the following:
# - Invalid menu choice
# - Invalid number input
# - Division by zero
#
# Use:
# - try
# - except
# - else
# - finally
# - raise (for invalid menu choices)
#
# Example:
# If the user enters 5 as the menu choice,
# raise:
# ValueError("Invalid menu choice")

print("Welcome to Python Calculator")

def show_menu():
    '''Opens up menu to select option'''
    print("\n====== Select An Option ======")
    print("1. ADD")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b  #


while True:
    show_menu()

    try:
        choice = int(input("Select an option: "))

        if choice not in (1, 2, 3, 4):
            raise ValueError("Invalid menu choice")

        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))

        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)

    except ValueError as e:
        print("Error:", e)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

    else:
        print(f"Result = {result}")

    finally:
        print("-- Operation attempt finished --")

    again = input("Do you want to calculate again? (yes/no): ")
    if again.lower() != 'yes':
        print("Goodbye!")
        break