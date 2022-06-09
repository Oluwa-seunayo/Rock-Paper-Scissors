rock = 'R'

paper = 'P'

scissors = 'S'


import random

response = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_response = random.randint(0,2)

if computer_response == 0:
  print("\n" + "computer chooses" + rock + "\n rock")
elif computer_response == 1:
  print("\n" + "computer chooses" + paper + " \n paper")
else:
  print("\n" + "computer chooses" + scissors + "\n scissors!")


if response > 3:
  print("you have entered an invalid number")
else:
  print("replay!!!!!!!")
if response == 0 and computer_response == 2:
  print("You win!")
elif response == 1 and computer_response == 0:
  print("you win")
elif response == 2 and computer_response == 1:
  print("You win!")
elif response == computer_response:
  print("it\'s a draw")
else:
  print("You lose!!!!!!!")