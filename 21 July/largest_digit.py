# Write a Python program to find the largest digit in a number.
#
# Example:
# Input: 59384
# Output: 9

# Output:
# Print largest.

number = int(input("Enter your number: "))
largest = 0

while number > 0:
    last_digit = number % 10
    if last_digit > largest:
        largest = last_digit
    number = number // 10

print("Largest digit:", largest)
