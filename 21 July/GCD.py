# Write a Python program to find the Greatest Common Divisor (GCD)
# of two numbers.

# Example:
# Input:
# 12
# 18

# Output:
# 6

# Input:
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Variables:
gcd = 1
if num1 < num2: 
    smaller_number = num1 
else: 
    smaller_number = num2

# Loop:
for i in range(1, smaller_number + 1):

    if num1 % i == 0 and num2 % i == 0:
        gcd = i

# Output:
print(f"The GCD is: {gcd}")


