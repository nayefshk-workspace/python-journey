# Write a Python program to calculate the area of a circle. 
# ● Example: 
# ○ Input: radius = 5 
# ○ Output: 78.54 
#area = pi x radius x radius
import math

radius = float(input("Enter circle radius: "))

# pi = 3.14

# area = pi * radius**2
area = math.pi * radius**2

print(f"The area is {area:.2f}")
#The .2f means "show exactly 2 digits after the decimal point."

