# ------------------------------------------------------
# MOVIE THEATER SEAT BOOKING SYSTEM
# A simple beginner-friendly Python program
# ------------------------------------------------------
 
# We represent the 20 seats using a list.
# Each seat is either "O" (open/available) or "X" (booked).
# List index 0 = Seat 1, index 1 = Seat 2, and so on.
TOTAL_SEATS = 20
seats = ["O"] * TOTAL_SEATS   # creates a list of 20 "O"s
 
def show_menu():
    """Print the main menu."""
    print("\n===== MOVIE THEATER MENU =====")
    print("1. View available seats")
    print("2. Book a seat")
    print("3. Cancel a booking")
    print("4. View booked seats")
    print("5. Exit")
 
 
def view_available_seats():
    """Print all seats that are still open."""
    print("\nAvailable Seats:")
    available = []
    for i in range(TOTAL_SEATS):
        if seats[i] == "O":
            available.append(i + 1)   # +1 because seats are numbered from 1, not 0
 
    if available:
        print(available)
    else:
        print("No seats available. The theater is full!")
 
 
def view_booked_seats():
    """Print all seats that are currently booked."""
    print("\nBooked Seats:")
    booked = []
    for i in range(TOTAL_SEATS):
        if seats[i] == "X":
            booked.append(i + 1)
 
    if booked:
        print(booked)
    else:
        print("No seats have been booked yet.")
 
 
def book_seat():
    """Ask the user for a seat number and book it if possible."""
    view_available_seats()
    choice = input("\nEnter the seat number you want to book (1-20): ")
 
    # Make sure the user typed a number
    if not choice.isdigit():
        print("Please enter a valid number.")
        return
 
    seat_number = int(choice)
 
    # Check the number is in range
    if seat_number < 1 or seat_number > TOTAL_SEATS:
        print("Seat number must be between 1 and 20.")
        return
 
    index = seat_number - 1   # convert seat number back to list index
 
    if seats[index] == "X":
        print(f"Sorry, seat {seat_number} is already booked.")
    else:
        seats[index] = "X"
        print(f"Seat {seat_number} booked successfully!")
 
 
def cancel_booking():
    """Ask the user for a seat number and cancel it if it was booked."""
    view_booked_seats()
    choice = input("\nEnter the seat number you want to cancel (1-20): ")
 
    if not choice.isdigit():
        print("Please enter a valid number.")
        return
 
    seat_number = int(choice)
 
    if seat_number < 1 or seat_number > TOTAL_SEATS:
        print("Seat number must be between 1 and 20.")
        return
 
    index = seat_number - 1
 
    if seats[index] == "O":
        print(f"Seat {seat_number} was not booked, nothing to cancel.")
    else:
        seats[index] = "O"
        print(f"Booking for seat {seat_number} cancelled.")
 
#Here the main program loop will go every option the user choose it will be show according to this
 
def main():
    """Main program loop."""
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
 
        if choice == "1":
            view_available_seats()
        elif choice == "2":
            book_seat()
        elif choice == "3":
            cancel_booking()
        elif choice == "4":
            view_booked_seats()
        elif choice == "5":
            print("Thank you for visiting the theater. Goodbye!")
            break
        else:
            print("Invalid option, please choose a number from 1 to 5.")
 
 
# This makes sure main() only runs when this file is run directly,
# not when it's imported into another file.
if __name__ == "__main__":
    main()