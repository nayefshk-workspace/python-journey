# 17.Create a string variable named my_string and assign it the value "Programming is fun!". 

# ● Use string interpolation to replace "fun" with "awesome" and print the resulting string. 

# ● Use the split method to split my_string into a list of words and print the result. 

# ● Use the join method to concatenate the list of words into a single string using a space as a separator and print the resulting string.

my_string = "Programming is fun!"
 

new_version = my_string.replace("fun", "awesome")
print(new_version)
 

words = my_string.split()
print(words)
 

print(" ".join(words))
