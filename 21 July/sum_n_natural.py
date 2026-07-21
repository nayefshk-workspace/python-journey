# Write a Python program to calculate the sum of the first N natural numbers.
#
# Example:
# Input: 5
# Output: 15
#
# Explanation:
# 1 + 2 + 3 + 4 + 5 = 15

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


