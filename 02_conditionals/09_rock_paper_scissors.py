# imports
import random

# ascii
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# welcome message
print("***********************\nWelcome to\nRock | Paper | Scissors\n")
# prompt user input
try:
    user = int(
        input("Enter your move.\nPress:\n1: rock\n2: paper\n3: scissors\n\n"))
except:
    print("\ninvalid input.\ntry again!!!")
    exit()
if not (user == 1 or user == 2 or user == 3):
    # if not user == 1 or not user == 2 or not user == 3:
    print("\ninvalid input.\ntry again!!!")
    exit()
# generate cpu's input
cpu = random.randint(1, 3)
# ascii variable
if user == 1:
    user_art = rock
    user_text = "rock"
if user == 2:
    user_art = paper
    user_text = "paper"
if user == 3:
    user_art = scissors
    user_text = "scissors"
if cpu == 1:
    cpu_art = rock
    cpu_text = "rock"
if cpu == 2:
    cpu_art = paper
    cpu_text = "paper"
if cpu == 3:
    cpu_art = scissors
    cpu_text = "scissors"

if user == cpu:
    state = "drew"
elif (user == 1 and cpu == 3) or (user == 2 and cpu == 1) or (user == 3 and cpu == 2):
    state = "won"
else:
    state = "lost"

print(
    f"\nYOUR MOVE: {user_text}{user_art}\n\nCOM MOVE: {cpu_text}{cpu_art}\n\nYOU {state.upper()}!!!")
