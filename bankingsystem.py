#Aim to create a banking code where user can check for balance, deposit money,withdraw money and the main menu will appear until user exits 
#Menu
#Balance
#deposit
#withdraw
#withdraw

# Starting Balance
balance = 1000

#menu
def show_menu():
    print("\n====== Python ATM ======")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")


# Function to check balance
def check_balance():
    print(f"Your current balance is:{balance}")


# Function to deposit money
def deposit():
    global balance

    amount = int(input("Enter amount to deposit: "))

    balance = balance + amount

    print("Deposit Successful!")
    print(f"New Balance: ₹{balance}")


# Function to withdraw money
def withdraw():
    global balance

    amount = int(input("Enter amount to withdraw: "))

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal Successful!")
        print(f"Remaining Balance: ₹{balance}")
    else:
        print("Insufficient Balance!")


# ---------------- Main Program ---------------- #

print("Welcome to Python ATM")

while True:

    show_menu()

    choice = int(input("Select an option: "))

    if choice == 1:
        check_balance()

    elif choice == 2:
        deposit()

    elif choice == 3:
        withdraw()

    elif choice == 4:
        print("Thank you for using Python ATM!")
        break

    else:
        print("Invalid Choice!")