# imports
from random import randint
# initializations

# welcome message
print("\nWelcome to the Toothpick Game.\nPlayers will take turn picking out toothpicks\nuntil none is left.\nThe player who pick the last toothpick wins.\n")
# number of toothpicks
while True:
    try:
        toothpicks = int(input(
            "\nEnter number of toothpicks to be picked.\nMust be between 10 and 30 inclusive.\n"))
    except:
        print("\nError! invalid input. Try Again!")
        continue
    if toothpicks not in range(10, 31):
        print("\nError. Invalid number of toothpick. Try Again!")
    else:
        break
# players' names
while True:
    player_1 = input("\nplayer 1. What is your name?\t")
    player_2 = input("player 2. What is your name?\t")
    if player_1 == player_2:
        print("\nboth names can't be the same try again")
    else:
        break

# select first player randomly
if randint(1, 2) == 1:
    curr_player = player_1
else:
    curr_player = player_2

# start game
while True:
    # prompt text pluralization
    if toothpicks == 1:
        toothpick_plural = ""
        aux_plural = "is"
        option = "1"
    else:
        toothpick_plural = "s"
        aux_plural = "are"
        option = "1, 2 or 3"
        if toothpicks == 2:
            option = "1 or 2"

# prompt current user to pick from remaining toothpicks
    # validate user input as integer
    try:
        current = int(input(
            f"\n\n{'| ' * toothpicks}\nThere {aux_plural} {toothpicks} toothpick{toothpick_plural} left.\n{curr_player}, take out {option} out!\n"))
    # if user input is invalid, reply with error msg and prompt again
    except:
        print("invalid input")
        continue
    # if user input is invalid, reply with error msg and prompt again
    if not (current == 1 or current == 2 or current == 3) or (current > toothpicks):
        print(
            f"please, pick 1, 2, or 3 toothpicks from the remaining {toothpicks}")
        continue
    # subtract current user input from num of toothpick and update toothpicks
    toothpicks -= current
    # if toothpicks is empty, declare current user is winner and end game
    if toothpicks == 0:
        print(f"{curr_player} you took out the last {current} toothpick{toothpick_plural}.\nHence, You Win!!!")
        break
    # switch to the next player
    if curr_player == player_1:
        curr_player = player_2
    elif curr_player == player_2:
        curr_player = player_1
