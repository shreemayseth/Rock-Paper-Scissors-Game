#print("Rock...")
#print("Paper...")
#print("Scissors...")

from random import randint
player = input("Player , make your move: ")
rand = randint(0,2)
if rand == 0:
    computer = "rock"
elif rand == 1:
    computer = "paper"
else:
    computer = "scissors"

print(f"Computer plays: {computer}")
#player2 = input("Player2 , make your move: ")

if player == "rock" and computer == "scissors":
    print("player wins!!")
elif player == "scissors" and computer == "paper":
    print("player wins!!")
elif player == "paper" and computer == "rock":
    print("player wins!!")
elif player == "scissors" and computer == "rock":
    print("computer wins!!")
elif player == "paper" and computer == "scissors":
    print("computer wins!!")
elif player == "rock" and computer == "paper":
    print("computer wins!!")
elif player == computer:
    print("Oops! It's a tie")
else:
    print("Something went wrong")