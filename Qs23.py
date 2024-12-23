age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ")
score = float(input("Enter academic score (out of 100): "))

if 18 <= age <= 25:
    if gender == 'M':
        if score >= 85:
            print("Full Scholarship")
        elif score >= 70:
            print("Partial Scholarship")
        else:
            print("No Scholarship")
    elif gender == 'F':
        if score >= 80:
            print("Full Scholarship")
        elif score >= 65:
            print("Partial Scholarship")
        else:
            print("No Scholarship")
    else:
        print("Invalid gender input")
else:
    print("Age is not within the eligible range for scholarship.")