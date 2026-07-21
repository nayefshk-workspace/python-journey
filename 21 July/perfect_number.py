# Write a Python program to check whether a number is a Perfect Number.
#
# Example:
# Input: 28
#
# Output:
# Perfect Number
#
# Explanation:
# Factors of 28 (excluding itself):
# 1 + 2 + 4 + 7 + 14 = 28
#input
num = int(input("Enter your number: "))
#variale
factor_sum = 0

#loop
for i in range(1, num):
    if num % i == 0:
        factor_sum = factor_sum + i  
if factor_sum == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
