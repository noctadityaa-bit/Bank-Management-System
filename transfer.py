def transfer_money(accounts, account_number):

    receiver = input("Enter receiver account number: ")

    if receiver not in accounts:
        print("Receiver account does not exist!")
        return

    if receiver == account_number:
        print("You cannot transfer money to your own account!")
        return

    try:
        amount = float(input("Enter amount to transfer: "))

        if amount < 0:
            print("Amount cannot be negative!")
            return

        if amount > accounts[account_number]["balance"]:
            print("Insufficient balance!")
            return

        accounts[account_number]["balance"] -= amount
        accounts[receiver]["balance"] += amount

        accounts[account_number]["transactions"].append(
            "Transferred ₹" + str(amount) + " to Account " + receiver
        )

        accounts[receiver]["transactions"].append(
            "Received ₹" + str(amount) + " from Account " + account_number
        )

        print("Money transferred successfully!")

    except ValueError:
        print("Please enter a valid amount!")