# Write a Python program to check if the given year is a leap year or not.
# ● Example: 
# ○ Input: 2020 
# ○ Output: True 

# Input year

# ↓

# Is it divisible by 4?

# No → Not Leap Year

# Yes ↓

# Is it divisible by 100?

# No → Leap Year

# Yes ↓

# Is it divisible by 400?

# Yes → Leap Year

# No → Not Leap Year

year = int(input("Enter year: "))
# if year % 4 == 0:

#     if year % 100 == 0:

#          if year % 400 == 0:
#              print("Its a leap year")
#          else:
#              print("Its not a leap year")

#     else:
#          print("Its a leap year")

# else:
#      print("Its not a leap year")

if (year %4==0 and year%100!=0) or (year%400==0):
    print("Leap")
else:
    print("Its not a leap year")