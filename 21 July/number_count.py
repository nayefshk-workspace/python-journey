# Write a Python program to count the number of digits in a number.
#
# Example:
# Input: 12345
# Output: 5
number = int(input("Enter your number: "))


def count_digits(number):
    number = abs(number) #abs is absolute value (Remove the negative sign from a number.)

    if number == 0:
        return 1

    count = 0

    while number > 0:
        number = number // 10
        count = count + 1
    return count


answer = count_digits(number)

print(f"The number of digits in {number} is {answer}")