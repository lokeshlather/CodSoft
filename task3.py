import random

def ComputerChoice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def Result(PlayerChoice, ComputerChoice):
    if PlayerChoice == ComputerChoice:
        return "It's a tie!"
    elif (PlayerChoice == "rock" and ComputerChoice == "scissors") or \
         (PlayerChoice == "scissors" and ComputerChoice == "paper") or \
         (PlayerChoice == "paper" and ComputerChoice == "rock"):
        return "You Win!"
    else:
        return "You Lose!"

def main():
    print("Welcome to Rock-Paper-Scissors!")
    
    while True:
        Player_Choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
        
        if Player_Choice == 'exit':
            print("Thanks for playing!")
            break
        
        if Player_Choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        Computer_Choice=ComputerChoice()
        print(f"Computer Choose: {Computer_Choice}")

        
        result = Result(Player_Choice, Computer_Choice)
        print(result)

if __name__ == "__main__":
    main()
