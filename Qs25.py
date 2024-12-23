age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ")
show_type = input("Enter show type (Matinee/Evening): ")

if age < 12:
    if show_type == 'Matinee':
        ticket_price = 500
    elif show_type == 'Evening':
        ticket_price = 700
    else:
        print("Invalid show type.")
elif 12 <= age < 60:
    if gender == 'M':
        if show_type == 'Matinee':
            ticket_price = 800
        elif show_type == 'Evening':
            ticket_price = 1000
        else:
            print("Invalid show type.")
    elif gender == 'F':
        if show_type == 'Matinee':
            ticket_price = 700
        elif show_type == 'Evening':
            ticket_price = 900
        else:
            print("Invalid show type.")
    else:
        print("Invalid gender input.")
else:  # Age >= 60
    ticket_price = 600
    print(f"The ticket price is Rs{ticket_price}")
