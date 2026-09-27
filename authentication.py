def login(accounts):

    account_number = input("Enter account number: ")
    pin = input("Enter PIN: ")

    if account_number in accounts and accounts[account_number]["pin"] == pin:
        print("Login successful!")
        return account_number

    print("Invalid account number or PIN!")
    return None