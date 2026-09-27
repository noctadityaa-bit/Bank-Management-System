from validation import validate_account_number, validate_pin, validate_amount

print("----- TESTING BANK MANAGEMENT SYSTEM -----")

print("Account Number Test:")
print(validate_account_number("1234"))
print(validate_account_number("123"))

print("\nPIN Test:")
print(validate_pin("1234"))
print(validate_pin("12"))

print("\nAmount Test:")
print(validate_amount(500))
print(validate_amount(-100))