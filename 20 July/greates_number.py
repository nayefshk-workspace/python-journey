# Write a Python program to find the greatest among three integers.
#
# Example:
# Input: 10, 20, 30
# Output: 30

number1 = int(input("Enter your number: "))
number2 = int(input("Enter your number: "))
number3 = int(input("Enter your number: "))

if number1 == number2 == number3:
    print("All the numbers are same")
elif number1 >= number2 and number1 >= number3:
    print(f"Number {number1} is greatest")

elif number2 >= number1 and number2 >= number3:
    
    print(f"Number {number2} is greatest")

else:
    print(f"Number {number3} is greatest")
    