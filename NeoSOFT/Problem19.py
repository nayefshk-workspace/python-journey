 
# 19.Create a string variable named my_string and assign it the value "python". ● Use slicing to print the first three characters of my_string in reverse order. 

# ● Use slicing to print the last two characters of my_string in reverse order. 

# ● Use the join method to add a hyphen between each character of my_string and print the resulting string. 

my_string = "python"

print(my_string[2::-1])
 
print(my_string[:-3:-1])

print("-".join(my_string))