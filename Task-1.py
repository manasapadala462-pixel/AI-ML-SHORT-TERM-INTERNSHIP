while True:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    print("Select the operation you want to perform:")
    print("1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exit")
    choice = int(input("Enter your choice: "))
 
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    def multiply(a, b):
        return a * b
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b
 
    if choice == 1:
        print("The result of addition is: ", add(n1, n2))
    elif choice == 2:
        print("The result of subtraction is: ", subtract(n1, n2))
    elif choice == 3:
        print("The result of multiplication is: ", multiply(n1, n2))
    elif choice == 4:
        print("The result of division is: ", divide(n1, n2))
    elif choice == 5:
        print("Exiting the calculator.")
        break
    else:
        print("Invalid choice! Please select a valid operation.")
