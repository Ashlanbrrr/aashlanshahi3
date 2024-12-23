age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ")
income = float(input("Enter income: "))

if age >= 18 and age < 60:
    if gender == 'M':
        if income > 1000000:
            tax = income * 0.30
        elif 500000 <= income <= 1000000:
            tax = income * 0.20
        else:
            tax = income * 0.10
    elif gender == 'F':
        if income > 1000000:
            tax = income * 0.25
        elif 500000 <= income <= 1000000:
            tax = income * 0.15
        else:
            tax = income * 0.05
    else:
        print("Invalid gender input")
elif age >= 60:
    if income > 1000000:
        tax = income * 0.20
    else:
        tax = income * 0.10
else:
    print("Invalid age input")
   