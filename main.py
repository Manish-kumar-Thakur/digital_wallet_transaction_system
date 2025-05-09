from user import register_user, view_users
from wallet import add_balance, check_balance
from transaction import send_money, view_transactions

def main():
    while True:
        print("\n=== Digital Wallet System ===")
        print("1. Register User")
        print("2. View Users")
        print("3. Add Balance")
        print("4. Send Money")
        print("5. Check Balance")
        print("6. View Transactions")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            password = input("Enter password: ")
            tier = input("Enter tier (Basic/Silver/Gold): ")
            limit = float(input("Enter limit amount: "))
            register_user(name, phone, password, tier, limit)
        elif choice == "2":
            view_users()
        elif choice == "3":
            phone = input("Enter phone: ")
            amount = float(input("Enter amount to add: "))
            add_balance(phone, amount)
        elif choice == "4":
            sender = input("Enter sender phone: ")
            receiver = input("Enter receiver phone: ")
            amount = float(input("Enter amount: "))
            send_money(sender, receiver, amount)
        elif choice == "5":
            phone = input("Enter phone to check balance: ")
            check_balance(phone)
        elif choice == "6":
            view_transactions()
        elif choice == "7":
            print("Thank you for using digital wallet transaction system!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
