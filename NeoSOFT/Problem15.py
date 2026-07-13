# 15.Create a string variable named email and assign it the value "jane.doe@example.com". 

# a. Print the username (i.e., "jane.doe") by slicing the string. 
# b. Print the domain (i.e., "example.com") by slicing the string. 
# c. Replace the domain with "mycompany.com" and print the resulting email address. 

email = "jane.doe@example.com"

print(email[:8])

print(email[9:])

print(email.replace("example.com", "mycompany.com"))