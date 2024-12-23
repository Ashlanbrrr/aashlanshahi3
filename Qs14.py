def cybersecurity_mission():
    print("Welcome to the Cybersecurity Mission!")

    choice = input("Do you choose to 'trace the hacker' or 'secure the system'? ")

    if choice == "trace the hacker":
        action = input("Do you want to 'track their IP' or 'decode their message'? ")

        if action == "track their ip":
            print("You caught the hacker. You Win!")
        elif action == "decode their message":
            print("The message was a trap. Game Over.")
        else:
            print("Invalid choice. Game Over.")
    
    elif choice == "secure the system":
        action = input("Do you want to 'shut down the server' or 'upgrade the firewall'? ")

        if action == "shut down the server":
            print("The attack was stopped. You Win!")
        elif action == "upgrade the firewall":
            print("The hacker bypassed it. Game Over.")
        else:
            print("Invalid choice. Game Over.")
    
    else:
        print("Invalid choice. Game Over.")