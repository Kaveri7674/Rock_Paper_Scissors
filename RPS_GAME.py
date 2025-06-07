import random
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")
options = ["rock", "paper", "scissors"]
your_choice = input("Enter your choice (rock, paper, scissors): ").lower()
# Check for valid input
if your_choice not in options:
    print("Invalid choice! Please choose rock, paper, or scissors.")
else:
    computer_choice = random.choice(options)
    print("You chose:", your_choice)
    print("Computer chose:", computer_choice)

    if your_choice == computer_choice:
        print("It's a tie!")
    elif your_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif your_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif your_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("Computer wins!")
