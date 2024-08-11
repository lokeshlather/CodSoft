def Add(a, b):
    return a + b

def Subtract(a, b):
    return a - b

def Multiply(a, b):
    return a * b

def Divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    else:
        return a / b

def main():
    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice in ['1', '2', '3', '4']:
            try:
                First = float(input("Enter First number: "))
                Second = float(input("Enter Second number: "))

                if choice == '1':
                    print(f"Result: {Add(First, Second)}")
                elif choice == '2':
                    print(f"Result: {Subtract(First, Second)}")
                elif choice == '3':
                    print(f"Result: {Multiply(First, Second)}")
                elif choice == '4':
                    print(f"Result: {Divide(First, Second)}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        
        elif choice == '5':
            print("Exiting the calculator.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
