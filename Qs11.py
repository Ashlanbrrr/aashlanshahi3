def underwater_world():
    print("Welcome to the Underwater World!")

    choice = input("Do you choose to 'dive deeper' or 'surface'? ")

    if choice == "dive deeper":
        action = input("Do you want to 'search for pearls' or 'chase the fish'? ")

        if action == "search for pearls":
            print("You found a rare pearl. You Win!")
        elif action == "chase the fish":
            print("You got lost underwater. Game Over.")
        else:
            print("Invalid choice. Game Over.")
    
    elif choice == "surface":
        print("You returned safely.")
    
    else:
        print("Invalid choice. Game Over.")