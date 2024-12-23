def pirate_ship_adventure():
    print("Welcome to the Pirate Ship Adventure!")

    choice = input("Do you choose to 'search for treasure' or 'battle enemy ships'? ")

    if choice == "search for treasure":
        action = input("Do you want to 'dig on the island' or 'explore the cave'? ")

        if action == "dig on the island":
            print("You found a hidden treasure chest. You Win!")
        elif action == "explore the cave":
            print("You were trapped inside. Game Over.")
        else:
            print("Invalid choice. Game Over.")
    
    elif choice == "battle enemy ships":
        action = input("Do you want to 'attack' or 'defend'? ")

        if action == "attack":
            print("You won the battle. You Win!")
        elif action == "defend":
            print("You were outnumbered. Game Over.")
        else:
            print("Invalid choice. Game Over.")
    
    else:
        print("Invalid choice. Game Over.")
