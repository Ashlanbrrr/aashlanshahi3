age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ")
membership_type = input("Enter membership type (Monthly/Yearly): ")

if 18 <= age < 30:
    if gender == 'M':
        if membership_type == 'Monthly':
            price = 50
        elif membership_type == 'Yearly':
            price = 500
        else:
            print("Invalid membership type.")
    elif gender == 'F':
        if membership_type == 'Monthly':
            price = 45
        elif membership_type == 'Yearly':
            price = 450
        else:
            print("Invalid membership type.")
    else:
        print("Invalid gender input.")
elif 30 <= age <= 50:
    if membership_type == 'Monthly':
        price = 60
    elif membership_type == 'Yearly':
        price = 600
    else:
        print("Invalid membership type.")
elif age > 50:
    if membership_type == 'Monthly':
        price = 40
    elif membership_type == 'Yearly':
        price = 400
    else:
        print("Invalid membership type.")
else:
    print("Age is below the eligible range for membership.")