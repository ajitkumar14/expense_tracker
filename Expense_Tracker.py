transactions = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter income amount: "))
        transactions.append(amount)
        print("Income added successfully!")

    elif choice == "2":
        amount = float(input("Enter expense amount: "))
        transactions.append(-amount)
        print("Expense added successfully!")

    elif choice == "3":
        balance = sum(transactions)
        print(f"Current Balance: ₹{balance}")

    elif choice == "4":
        print("\nTransaction History:")
        for t in transactions:
            print(t)

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")