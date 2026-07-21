# Write a Python program to count the number of even digits
# and odd digits in a given number.
#
# Example:
# Input: 123456
#
# Output:
# Even digits: 3
# Odd digits: 3


number = int(input("Enter your number: "))

#variables 
even_digits = 0
odd_digits = 0
last_digit = 0
#looop
while number > 0:
    last_digit = number % 10

    if last_digit % 2 == 0:
        even_digits = even_digits + 1
    else:
        odd_digits = odd_digits + 1
    number = number // 10
print("Odd number: ",odd_digits)
print("Even number: ",even_digits)