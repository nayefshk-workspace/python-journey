# simple intrest = principal x rate x time
#Write a Python program to calculate simple interest. 
# ● Example: 
# ○ Input: Principal = 1000, Rate = 5%, Time = 2 
# ○ Output: 100.0 

princiapal = int(input("Enter principal: "))
rate = int(input("Enter Rate: "))
time = int(input("Enter time: "))

simple_intrest = princiapal * rate * time
simple_intrest = simple_intrest / 100
print(f"Your simple intrest comes up to {simple_intrest}")