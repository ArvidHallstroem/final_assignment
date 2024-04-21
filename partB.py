import random
import string

class SeatBookingSystem:
    def __init__(self):
        self.seats = [['F' for _ in range(10)] for _ in range(7)]  # Initialize seats as all free
        self.bookings = {}  # Initialize bookings dictionary to store booking references and customer data

    def display_menu(self):
        # Displays the main menu options to the user
        print("\nMenu:")
        print("1. Check availability of seat")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Show booking state")
        print("5. Exit program")

    def check_availability(self, row, col):
        # Checks if a seat is available for booking
        return self.seats[row][col] == 'F'

    def generate_booking_reference(self):
        # Generates a random booking reference with eight alphanumeric characters
        reference_length = 8
        reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=reference_length))

        # Ensure uniqueness of the reference
        while reference in self.bookings:
            reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=reference_length))

        return reference

    def book_seat(self, row, col, passport_number, first_name, last_name):
        # Books a seat if it is available
        if self.seats[row][col] == 'F':
            booking_reference = self.generate_booking_reference()
            self.seats[row][col] = booking_reference
            self.bookings[booking_reference] = {
                'passport_number': passport_number,
                'first_name': first_name,
                'last_name': last_name,
                'row': row,
                'column': col
            }
            print("Seat booked successfully.")
        else:
            print("Seat is already booked.")

    def free_seat(self, row, col):
        # Frees a booked seat and removes booking details from the database
        if self.seats[row][col] != 'F':
            booking_reference = self.seats[row][col]
            del self.bookings[booking_reference]
            self.seats[row][col] = 'F'
            print("Seat freed successfully.")
        else:
            print("Seat is already free.")

    def show_booking_state(self):
        # Displays the current state of all seats
        print("Seat Booking State:")
        for row in self.seats:
            print(' '.join(row))  # Join each row's elements with a space and print.


def main():
    seat_booking_system = SeatBookingSystem()

    while True:
        seat_booking_system.display_menu()
        choice = input("Enter your choice: ")  # Get user input for menu selection.
        if choice == '5':
            print("Exiting program.")  # Exit the program on choice '5'.
            break
        elif choice in ['1', '2', '3']:
            row = int(input("Enter row number from [0-6]: "))
            col = int(input("Enter column number from [0-9]: "))
            # Validate seat selection.
            if row < 0 or row > 6 or col < 0 or col > 9 or seat_booking_system.seats[row][col] in ['X', 'S']:
                print("Invalid seat selection.")
                continue
            if choice == '1':
                # Check seat availability.
                print("Available" if seat_booking_system.check_availability(row, col) else "Not available")
            elif choice == '2':
                # Attempt to book the seat.
                passport_number = input("Enter passport number: ")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                seat_booking_system.book_seat(row, col, passport_number, first_name, last_name)
            elif choice == '3':
                # Attempt to free the seat.
                seat_booking_system.free_seat(row, col)
        elif choice == '4':
            seat_booking_system.show_booking_state()  # Display the current booking state of all seats.


if __name__ == "__main__":
    main()