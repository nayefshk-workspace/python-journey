#fruit menu 
def show_shopping_list():
    print("========== SHOPPING LIST ========== \n 1. Show Items \n 2. Add Item \n 3. Remove Item \n 4. Exit \n Choose an option:")

#show items
def show_item():
    print(f"Items in bag:{show_item}")



#  add items
def add_item():
    global item

    amount = int(input("Enter item name : "))

    show_item = add_item + show_item

    print("item added")
    print(f"New List: ₹{show_item}")


# Remove items
def remove_item():
    global item

    amount = int(input("Enter item name to remove: "))

    balance = balance - amount
    print("Item removed Successful!")
    print(f"Remaining items: ₹{show_item}")


# ---------------- Main Program ---------------- #

print("Item list")

while True:

    show_item()

    choice = int(input("Select an option: "))

    if choice == 1:
        show_item()

    elif choice == 2:
        add_item()

    elif choice == 3:
        remove_item()

    elif choice == 4:
        print("Done")
        break

    else:
        print("Invalid Choice!")