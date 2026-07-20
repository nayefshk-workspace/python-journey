# Write a Python program to check if a given number is prime or not.
#
# Example:
# Input: 17
# Output: True
#
# Input: 10
# Output: False

# number = int(input("Enter your number : "))
# while True:
#     if number < 2:
#         print("Its not a prime number")
    
#     else:
#         for i in range(2,number):
#             if number % i == 0:
#                 print("its not a prime number")
#                 break
#         else:
#             print("Its a prime number")
#     print("Do you want to continue? (yes/no):")

    
while True:
    number = int(input("Enter your number: "))

    if number < 2:
        print("It's not a prime number")

    else:
        for i in range(2, number):
            if number % i == 0:
                print("It's not a prime number")
                break
        else:
            print("It's a prime number")

    choice = input("\nDo you want to check another number? (yes/no): ").lower()

    if choice == "no":
        print("Thank you for using the Prime Number Checker!")
        break

    print()  