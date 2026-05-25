import re

number = input("Enter mobile number: ")

match = re.fullmatch("[6-9]\\d{9}", number)

if match:
    print("Valid mobile number")
else:
    print("Invalid mobile number")