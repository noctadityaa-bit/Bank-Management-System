from storage import load_accounts, save_accounts
from account import create_account
from authentication import login
from transactions import deposit, withdraw, show_transaction_history
from transfer import transfer_money

accounts = load_accounts()

while True:

    print("\n==============================")
    print("     WELCOME TO BANK SYSTEM")
    print("==============================")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        create_account(accounts)
        save_accounts(accounts)

    elif choice == "2":

        account_number = login(accounts)

        if account_number is not None:

            while True:

                print("\n----- ACCOUNT MENU -----")
                print("1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Transfer Money")
                print("5. Change PIN")
                print("6. Transaction History")
                print("7. Logout")

                account_choice = input("Enter your choice: ")

                if account_choice == "1":

                    print("Current Balance: ₹", accounts[account_number]["balance"])

                elif account_choice == "2":

                    deposit(accounts, account_number)
                    save_accounts(accounts)

                elif account_choice == "3":

                    withdraw(accounts, account_number)
                    save_accounts(accounts)

                elif account_choice == "4":

                    transfer_money(accounts, account_number)
                    save_accounts(accounts)

                elif account_choice == "5":

                    new_pin = input("Enter new 4-digit PIN: ")

                    if new_pin.isdigit() and len(new_pin) == 4:
                        accounts[account_number]["pin"] = new_pin
                        save_accounts(accounts)
                        print("PIN changed successfully!")
                    else:
                        print("PIN must be exactly 4 digits!")

                elif account_choice == "6":

                    show_transaction_history(accounts, account_number)

                elif account_choice == "7":

                    print("Logged out successfully!")
                    break

                else:

                    print("Invalid choice!")

    elif choice == "3":

        print("Thank you for using Bank System!")
        break

    else:

        print("Invalid choice!")