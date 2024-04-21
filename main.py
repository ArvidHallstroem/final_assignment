def display_menu():
    print("1. Check availability of seat")
    print("2. Book a seat")
    print("3. Free a seat")
    print("4. Show booking state")
    print("5. Exit program")

def main():
    seats = [['F' if not (c == 2 or r >= 4 and c >= 6) else 'X' if c == 2 else 'S' for c in range(10)] for r in range(7)]
    while True:
        display_menu()
        choice=input("Enter your choice:")
        if choice == '5':
            print("Exiting the program")
            break
        elif choice in ['1', '2', '3']:
            row=int(input("Enter row number from [0-6]"))
            col=int(input("Enter col number from [0-6]"))

            if row<0 or row>6 or col<0 or col>9 or seats[row][col] in ['X', 'S']:
                print("Invalid seat")
                continue
        if choice == '1':
            print()
        elif choice=='2':
            print()
        elif choice=='3':
            print()
        elif choice=='4':
            
if __name__=="__main__":
    main()
