# Requirements:
# Ask for the PIN.
# If the PIN is "1234":
# Ask for the withdrawal amount.
# If the amount is less than or equal to 5000, print:
# Transaction Successful
# Otherwise, print:
# Insufficient Balance
# If the PIN is incorrect, print:
# Invalid PIN

pin = int(input("Enter your PIN: "))

if pin == 1234:
    amount = int(input("Enter withdrawal amount: "))
    if amount <= 5000:
        print("Transaction Successful")
    else:
        print("Insufficient Balance")
else:
    print("Invalid PIN")