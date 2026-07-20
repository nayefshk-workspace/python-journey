# Write a Python program to calculate the sum of the first N natural numbers.
#
# Example:
# Input: 5
# Output: 15
#
# Explanation:
# 1 + 2 + 3 + 4 + 5 = 15

number = int(input("Enter your number: "))

# sum = number * (number + 1) / 2

# print(sum)

#diff approach


total = 0

for i in range(1, number + 1):
    total = total + i

print(total)

