# import random
import random
randint = random.randint
# roll both dice using random integers and count rolls
die_1 = randint(1, 6)
die_2 = randint(1, 6)
count = 1

# while not (die_1 == 1 and die_2 == 1):
while die_1 != 1 or die_2 != 1:
    print(f"No Snake Eyes!!!\ndie 1 = {die_1}\ndie 2 = {die_2}\n")
    die_1 = randint(1, 6)
    die_2 = randint(1, 6)
    count += 1

print(f"Snake Eyes!!!\ndie 1 = {die_1}\ndie 2 = {die_2}\n{count} rolls")
