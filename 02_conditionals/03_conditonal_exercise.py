# prompt for name
first_name = input("What's your first name?\n")
last_name = input("What's your last name?\n")
name_length = len(first_name) + len(last_name)
# compare length of name with average
if name_length < 12:
    adj = "shorter than"
elif name_length > 12:
    adj = "longer than"
elif name_length == 12:
    adj = "exactly"
else:
    adj = "not comparable to"


# output
print(f"{first_name} {last_name} ({name_length}) is {adj} the length of average Nigerian name (12).")
