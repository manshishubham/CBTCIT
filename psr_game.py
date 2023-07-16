from random import randint

#creating list of options
l = ["Rock", "Paper", "Scissors", "rock", "paper", "scissors"]

#assigning chance to computer while opponent waits
computer = l[randint(0,5)]
player = False

while player == False:
    player = input("\nChoose - Rock, Paper, Scissors? ")
    print(f"\nYou chose {player}, computer chose {computer}.\n")
    if player == computer:
        print("Tie!")
    elif player == "Rock" or player == "rock":
        if computer == "Paper" or player == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper" or player == "paper":
        if computer == "Scissors" or computer == "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors" or player == "scissors":
        if computer == "Rock" or computer == "rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("Check your spelling!\n")
    
    again = input("\nWant to play again? ")
    if again == "Yes":
        player = False
        computer = l[randint(0,2)]
    else:
        player = True
        
        