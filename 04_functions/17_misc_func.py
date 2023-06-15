# function to check if num is even
def is_even(num):
    return not num & 1

# slugify function


def slugify(txt, sep="-"):
    return txt.strip().lower().replace(" ", sep)


print(slugify(" ha lol"))
print(slugify("fiFBTst Days of man"))
print(slugify("  to BE rounded"))
print(slugify("This is the last\n\t"))


# vowel counter

def vowel_count(txt):
    total = 0
    for char in "aeiou":
        total += txt.count(char)
    return total


def parent():
    par_var = "parent var"

    def child():
        global child_var
        child_var = "child var"
        print(f"child accessed {par_var}")
    child()
    print(f"parent accessed {child_var}")


parent()
print(child_var)


score = 5


def doublr():
    global score
    score = 10


doublr()
print(score)


def func_1():
    rand_1 = 123


def func_2():
    global rand_2
    rand_2 = 456


func_1()
func_2()

print(rand_2)
# print(rand_1)

rand_10 = ["foo", "bar"]
print(rand_10[0][1])

ran