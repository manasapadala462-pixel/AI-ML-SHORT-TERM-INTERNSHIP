while True:
    name = input("Enter Account Holder Name: ")
    acc_no = int(input("Enter Account Number: "))
    balance = int(input("Enter Balance Amount: "))

    print("Select the operation you want to perform:")
    print("1. Check Balance \n 2. Deposit Money \n 3. Withdraw Money \n 4. Exit")

    choice = int(input("Enter your choice: "))

    def check_balance(b):
        return b

    def deposit(b, amount):
        return b + amount

    def withdraw(b, amount):
        if amount > b:
            return "Insufficient Balance"
        return b - amount

    if choice == 1:
        print("Account Holder Name:", name)
        print("Account Number:", acc_no)
        print("Available Balance is:", check_balance(balance))

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        print("Updated Balance is:", deposit(balance, amount))

    elif choice == 3:
        amount = int(input("Enter withdraw amount: "))
        print("Updated Balance is:", withdraw(balance, amount))

    elif choice == 4:
        print("Exiting ATM.")
        break

    else:
        print("Invalid choice! Please select a valid operation.")
