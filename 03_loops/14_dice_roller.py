from random import randint

# prompt for num of sides of die and num of dice
try:
    num_of_dice = int(input("how many dice?\t"))
    num_of_sides = int(input("how many sides?\t"))
except:
    print("Error. input must be integer")
    quit()
#
while True:
    rolls = "|"
    for num in range(0, num_of_dice):
        rolls = rolls + str(randint(1, num_of_sides)) + "|"
    print(rolls)
    next = input("roll again? press \"q\" to quit.\t")
    if next == "q":
        break


# print(rolls)
