# Write a Python program to find the factorial of a given number.
#
# Example:
# Input: 5
# Output: 120
#
# Explanation:
# 5! = 5 × 4 × 3 × 2 × 1 = 120

#intput
#factorial = number x number - 1


num = int(input("Enter a number: "))
def factorial(num):
    if num < 0:
        print("Negative numbers not allowed")
    result = 1
    for i in range(2, num + 1):
        result = result * i
    return result

print(factorial(num))