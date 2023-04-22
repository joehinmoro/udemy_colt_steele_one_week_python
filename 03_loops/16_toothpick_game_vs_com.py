# imports
from random import randint
# initializations

# welcome message
print("\nWelcome to the Toothpick Game.\nThe Player will take turns with the computer\ntopick out toothpicks until none is left.\nThe player who pick the last toothpick wins.\n")

# number of toothpicks
while True:
    try:
        toothpicks = int(input(
            "\nEnter number of toothpicks to be picked.\nMust be between 10 and 50 inclusive.\n"))
    except:
        print("\nError! invalid input. Try Again!")
        continue
    if toothpicks not in range(10, 51):
        print("\nError. Invalid number of toothpick. Try Again!")
        continue
    else:
        break

# player name
while True:
    player = input("\nWhat is your name?\t").strip().capitalize()
    if len(player) != 0:
        break

# game difficulty
while True:
    try:
        level = int(input("Select difficulty. From 1 to 5\n"))
        if level not in range(1, 6):
            print("please provide a valid number. try again")
            continue
    except:
        print("please provide a valid input. try again")
        continue
    print(f"\nYou are playing against computer level {level}")
    break


# select first player randomly
if randint(1, 2) == 1:
    curr_player = "player"
    print(f"\n{player}, you start")
else:
    curr_player = "cpu"
    print(f"\n{'*' * 30}\nComputer starts")

# start game
while True:
    # prompt text pluralization
    if toothpicks == 1:
        toothpick_plural = ""
        aux_plural = "is"
        option = "the last 1"
    else:
        toothpick_plural = "s"
        aux_plural = "are"
        option = "1, 2 or 3"
        if toothpicks == 2:
            option = "1 or 2"

    if curr_player == "player":
        # PLAYER'S TURN
        # prompt current user to pick from remaining toothpicks
        # validate user input as integer
        try:
            current = int(input(
                f"\n\n{'*' *30}\n{'| ' * toothpicks}\nThere {aux_plural} {toothpicks} toothpick{toothpick_plural} left.\n\n{player}, take {option} out!\n"))
        # if user input is invalid, reply with error msg and prompt again
        except:
            print("invalid input")
            continue
        # if user input is invalid, reply with error msg and prompt again
        if not (current == 1 or current == 2 or current == 3) or (current > toothpicks):
            print(
                f"please, pick 1, 2, or 3 toothpicks from the remaining {toothpicks}")
            continue
        print(f"you picked {current}.\n{toothpicks - current} left.")
    elif curr_player == "cpu":
        # COM'S TURN
        # generate random number
        randnum = randint(1, 6)
        # in a chance of 1 in 1 to level difficulty, play wisely else play randomly
        if randnum in range(1, level + 1) and toothpicks % 4 != 0:
            current = toothpicks % 4
            adj = "wisely"
        else:
            if toothpicks < 2:
                current = 1
            elif toothpicks < 3:
                current = randint(1, 2)
            else:
                current = randint(1, 3)
            adj = "randomly"
        print(
            f"\nThe computer picked {current} {adj} from the remaining {toothpicks}")

    # subtract current user input from num of toothpick and update toothpicks
    toothpicks -= current
    # if toothpicks is empty, declare current user is winner and end game
    if toothpicks == 0:
        if curr_player != "cpu":
            print(
                f"\n{player} you took out the last {current} toothpick{toothpick_plural}.\nHence, You Win!!!")
        else:
            print(
                f"\nThe computer took out the last {current} toothpick{toothpick_plural}.\nHence, Computer Win!!!")
        # end game as no toothpick is left
        break

    # switch player
    if curr_player == "cpu":
        curr_player = "player"
    else:
        curr_player = "cpu"

    # com's turn
