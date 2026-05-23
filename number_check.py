num = input("Enter mobile number: ")

if len(num) == 10 and num.isdigit():

    if num[0] in ['6', '7', '8', '9']:
        
        print("Valid Indian Mobile Number")
    else:
        print("Invalid Indian Mobile Number")

else:
    print("Number must contain 10 digits only")