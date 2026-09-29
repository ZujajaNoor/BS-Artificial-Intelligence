# Create a simple ATM program.
# Start with:
# Balance = 50000
# Display:
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit
# Use a loop so the user can continue using the ATM until they select Exit.

balance = 50000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"Your Balance:{balance}")
    elif choice == 2:
        deposit = int(input("Enter amount you want to deposit: "))
        balance += deposit
        print(f"Now Your Balance:{balance}")
    elif choice == 3:
        withdraw = int(input("Enter amount you want to withdraw: "))
        if withdraw < balance:
            balance -= withdraw
            print(f"Now Your Balance:{balance}")
        else:
            print("Your balance is too low!")
    elif choice == 4:
        print("Thank you for your time!")
        break
    else:
        print("Invalid Choice!!!")
