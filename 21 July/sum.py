# Write a program in Python to find the sum of digits of a number using recursion. 
# ● Example: 
# ○ Input: 1234 
# ○ Output: 10 
num = int(input("Enter your number: "))

def sum(num):
    if num == 0:
        return 0

    last_digit = num % 10
    remaining_digit = num // 10

    return last_digit + sum(remaining_digit)

answer = sum(num)
print(answer)

