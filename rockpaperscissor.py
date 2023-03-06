#Rock, Paper, Scissors Game By using python (06-03-2023)
import random

options = ("Rock", "Paper", "Scissors")
player = None

computer = random.choice(options)
Playername = input ("Enter your name: ")

while player not in options:
    player = input("Enter your choice(Rock/Paper/Scissors): ")

print("Your choice is: ", player)
print("Your opponent's choice is: ", computer)

if player == computer:
    print("It's a tie")
elif player == ("Rock") and computer == ("Scissors"):
    print("The Winner of The Game is : ", Playername)
elif player == ("Paper") and computer == ("Rock"):
    print("The Winner of The Game is : ", Playername)
elif player == ("Scissor") and computer == ("Paper"):
    print("The Winner of The Game is : ", Playername)
else:
    print("The Winner of the Game is : Opponent")