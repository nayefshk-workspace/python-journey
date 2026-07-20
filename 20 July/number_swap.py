# Write a program in Python to swap two numbers using a third variable. 
# ● Example: 
# ○ Input: a = 5, b = 10 
# ○ Output: a = 10, b = 5

# number1 = int(input("Enter your first number: ")) #5
# number2 = int(input("Enter your second number: ")) #10

# number3 = number1 #5
# number1 = number2 #10
# number2 = number3
# #number3 = 5
# #number1 = 10

# print(f'first number : {number1}')
# print(f'second number : {number2}') 


number1 = int(input("Enter your first number: ")) #5
number2 = int(input("Enter your second number: ")) #10

number1 = number1 + number2 # a5 + b10 a15
#number1 = 15
number2 = number1 - number2 # b10 15-10 b5
#number2 = 5
number1 = number1 - number2
print(f"Enter your first number: {number1}")
print(f"Enter your second number: {number2}")
