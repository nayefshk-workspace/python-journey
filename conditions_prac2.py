# Write a program that:
# Asks the user for their username.
# If the username is "admin":
# Ask for the password.
# If the password is "python123":
# Login Successful
# Otherwise:
# Wrong Password
# If the username is not "admin":
# User Not Found

user = input("Enter your username: ")

if user == "admin":
    password = input("Enter your password: ")
    if password =="python123":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Username not found")