def create_account(accounts):

    name = input("Enter your name: ")
    account_number = input("Enter 4-digit account number: ")

    if account_number in accounts:
        print("Account already exists!")
        return

    pin = input("Create 4-digit PIN: ")

    if not pin.isdigit() or len(pin) != 4:
        print("PIN must be exactly 4 digits!")
        return

    try:
        balance = float(input("Enter initial deposit: "))

        if balance < 0:
            print("Amount cannot be negative!")
            return

    except ValueError:
        print("Please enter a valid amount!")
        return

    accounts[account_number] = {
        "name": name,
        "pin": pin,
        "balance": balance,
        "transactions": []
    }

    print("Account created successfully!")