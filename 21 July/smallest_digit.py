# Write a Python program to find the smallest digit in a number.
#
# Example:
# Input: 59384
# Output: 3


num = int(input("Enter your number: "))
smallest = 9 

while num > 0:
    last_digit = num % 10
    if last_digit < smallest:
        smallest = last_digit
    num = num // 10

print("Smallest digit:",smallest)