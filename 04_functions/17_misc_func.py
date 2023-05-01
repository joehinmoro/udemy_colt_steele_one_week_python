# function to check if num is even
def is_even(num):
    return not num & 1

# slugify function


def slugify(txt):
    return txt.strip().lower().replace(" ", "-")


print(slugify(" ha lol"))
print(slugify("fiFBTst Days of man"))
print(slugify("  to BE rounded"))
print(slugify("This is the last\n\t"))
