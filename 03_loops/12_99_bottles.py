user = int(input("how many bottles?\t"))

# for loop
for bottle in range(user, 0, -1):
    next_bottle = bottle - 1

    if bottle == 1:
        plural = ""
        next_bottle = "no more"
    else:
        plural = "s"

    if next_bottle == 1:
        next_plural = ""
    else:
        next_plural = "s"

    print(f"""****************************************************************
{bottle} bottle{plural} of beer on the wall.
{bottle} bottle{plural} of beer.
take one down, pass it around, {next_bottle} bottle{next_plural} of beer on the wall.
    """)


# while loop
bottle = user
while bottle > 0:
    next_bottle = bottle - 1

    if bottle == 1:
        plural = ""
        next_bottle = "no more"
    else:
        plural = "s"

    if next_bottle == 1:
        next_plural = ""
    else:
        next_plural = "s"

    print(f"""****************************************************************
{bottle} bottle{plural} of beer on the wall.
{bottle} bottle{plural} of beer.
take one down, pass it around, {next_bottle} bottle{next_plural} of beer on the wall.
    """)
    bottle -= 1
