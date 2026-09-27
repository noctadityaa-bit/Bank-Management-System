def validate_account_number(account_number):
    return account_number.isdigit() and len(account_number) == 4


def validate_pin(pin):
    return pin.isdigit() and len(pin) == 4


def validate_amount(amount):
    return amount >= 0