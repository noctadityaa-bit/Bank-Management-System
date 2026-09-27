def deposit(accounts, account_number):

    try:
        amount = float(input("Enter amount to deposit: "))

        if amount < 0:
            print("Amount cannot be negative!")
            return

        accounts[account_number]["balance"] += amount

        accounts[account_number]["transactions"].append(
            "Deposited ₹" + str(amount)
        )

        print("Money deposited successfully!")

    except ValueError:
        print("Please enter a valid amount!")


def withdraw(accounts, account_number):

    try:
        amount = float(input("Enter amount to withdraw: "))

        if amount < 0:
            print("Amount cannot be negative!")
            return

        if amount > accounts[account_number]["balance"]:
            print("Insufficient balance!")
            return

        accounts[account_number]["balance"] -= amount

        accounts[account_number]["transactions"].append(
            "Withdrawn ₹" + str(amount)
        )

        print("Money withdrawn successfully!")

    except ValueError:
        print("Please enter a valid amount!")


def show_transaction_history(accounts, account_number):

    print("\n----- TRANSACTION HISTORY -----")

    if len(accounts[account_number]["transactions"]) == 0:
        print("No transactions yet.")

    else:
        for transaction in accounts[account_number]["transactions"]:
            print("-", transaction)