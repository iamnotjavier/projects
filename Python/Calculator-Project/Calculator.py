def main():
    while True:
        menu()
        try:
            option = int(input("Select Operator: "))

            if option == 0:
                print("Exiting Calculator...")
                break

            if option not in range(1, 5):
                print("Invalid option, try again.")
                continue

            first_number = float(input("Enter 1st Number: "))
            second_number = float(input("Enter 2nd Number: "))

            print(f"Result:", operation(option, first_number, second_number))

        except ValueError:
            print("Invalid Input, please only enter numbers.")


def menu():
    print("=" * 30)
    print("Select One")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Exit")
    print("=" * 30)


def operation(choice, num1, num2):
    if choice == 1:
        print(f"Result:", num1 + num2)
    elif choice == 2:
        print(f"Result:", num1 - num2)
    elif choice == 3:
        print(f"Result:", num1 * num2)
    elif choice == 4:
        if num2 == 0:
            raise ZeroDivisionError
        else:
            return num1 / num2


if __name__ == "__main__":
    main()
