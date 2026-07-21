# Write a Python program to find the Least Common Multiple (LCM)
# of two numbers.
#
# Example:
# Input:
# 12
# 18
#
# Output:
# 36

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

largest_number = max(num1, num2)

max_limit = num1 * num2

for i in range(largest_number, max_limit + 1):
    if i % num1 == 0 and i % num2 == 0:
        lcm = i
        break  
print(f"The LCM is: {lcm}")
