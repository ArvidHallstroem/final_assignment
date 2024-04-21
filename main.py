def display_menu():
    #Displays the main menu options to the user
    print("\nMenu:")
    print("1. Check availability of seat")
    print("2. Book a seat")
    print("3. Free a seat")
    print("4. Show booking state")
    print("5. Exit program")

def check_availability(seats, row, col):
    #Checks if a seat is available for booking
    return seats[row][col] == 'F'

def book_seat(seats, row, col):
    #Books a seat if it is available
    if seats[row][col] == 'F':
        seats[row][col] = 'R'  # Change the status from Free to Reserved.
        return "Seat booked."
    return "Seat not available or already booked."

def free_seat(seats, row, col):
    #Frees a booked seat."""
    if seats[row][col] == 'R':
        seats[row][col] = 'F'  # Change the status from Reserved to Free.
        return "Seat freed."
    return "Seat was not booked."

def show_booking_state(seats):
    """Displays the current state of all seats."""
    for row in seats:
        print(' '.join(row))  # Join each row's elements with a space and print.

def main():
    # Initialize the seating arrangement.
    # 'F' for free seats, 'X' for isles, 'S' for storage areas.
    seats = [['F' if not (c == 2 or r >= 4 and c >= 6) else 'X' if c == 2 else 'S' for c in range(10)] for r in range(7)]
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")  # Get user input for menu selection.
        if choice == '5':
            print("Exiting program.")  # Exit the program on choice '5'.
            break
        elif choice in ['1', '2', '3']:
            row = int(input("Enter row number from [0-6]: "))
            col = int(input("Enter row number from [0-9]: "))
            # Validate seat selection.
            if row < 0 or row > 6 or col < 0 or col > 9 or seats[row][col] in ['X', 'S']:
                print("Invalid seat selection.")
                continue
            if choice == '1':
                # Check seat availability.
                print("Available" if check_availability(seats, row, col) else "Not available")
            elif choice == '2':
                # Attempt to book the seat.
                result = book_seat(seats, row, col)
                print(result)
            elif choice == '3':
                # Attempt to free the seat.
                result = free_seat(seats, row, col)
                print(result)
        elif choice == '4':
            show_booking_state(seats)  # Display the current booking state of all seats.

if __name__ == "__main__":
    main()

