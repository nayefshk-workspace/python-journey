# 22.Create a string variable named my_string and assign it the value "racecar". 
# a. Use slicing to print the string "race" from my_string. 
# b. Use slicing to print the string "cec" from my_string in reverse order. 
# c. Check if my_string is a palindrome (i.e., reads the same forwards and backwards) and print the result.

my_string = "racecar"

print(my_string[:4])

print(my_string[4:1:-1])

print(my_string == my_string[::-1])