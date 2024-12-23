age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ")
experience = int(input("Enter years of experience: "))

if 21 <= age <= 35:
    if gender == 'M':
        if experience >= 5:
            print("Senior Developer")
        else:
            print("Junior Developer")
    elif gender == 'F':
        if experience >= 5:
            print("Senior Analyst")
        else:
            print("Junior Analyst")
    else:
        print("Invalid gender input")
elif age > 35:
    print("Manager Role")
else:
    print("Age is below the eligible range for the role.")