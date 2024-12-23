print("Welcome to the Forest Adventure!")
path = input("Choose a path: 'left' or 'right': ")
if path == "left":
    action = input("You chose the left path. Do you want to 'explore' or 'rest'?: ").strip().lower()
    if action == "explore":
        print("You found treasure!")
    elif action == "rest":
        print("You were attacked by wild animals. Game Over.")
    else:
        print("Invalid choice. Adventure ends here.")
elif path == "right":
    print("You fell into a trap. Game Over.")
else:
    print("Invalid path. You are lost in the forest!")
    