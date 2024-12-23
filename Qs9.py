print("Welcome to the Space Adventure!")
action = input("Do you want to 'land on Mars' or 'fly to Jupiter'?: ")

if action == "land on mars":
    mars_choice = input("You chose to land on Mars. Do you want to 'explore' or 'build a base'?: ")
    if mars_choice == "explore":
        print("You found alien artifacts. You Win!")
    elif mars_choice == "build a base":
        print("You ran out of resources. Game Over.")
    else:
        print("Invalid choice. Mission failed.")
elif action == "fly to jupiter":
    print("Your spaceship crashed. Game Over.")
else:
    print("Invalid action. You are lost in space!")
