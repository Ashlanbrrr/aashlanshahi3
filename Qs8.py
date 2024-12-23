print("Welcome to the Jungle Survival Challenge!")
action = input("Do you want to 'search for food' or 'build a shelter'?: ")

if action == "search for food":
    food_choice = input("You chose to search for food. Do you want to 'hunt' or 'gather'?: ")
    if food_choice == "hunt":
        print("You were attacked by a wild animal. Game Over.")
    elif food_choice == "gather":
        print("You found enough food. You Win!")
    else:
        print("Invalid choice. Survival failed.")
elif action == "build a shelter":
    print("Your shelter collapsed in the rain. Game Over.")
else:
    print("Invalid action. You are lost in the jungle!")