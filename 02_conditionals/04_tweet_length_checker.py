# set max length and prompt for tweet string
max_length = 14
tweet = len(input("Enter new tweet:\n"))
# validate tweet char length
if tweet <= 0:
    status = "Error"
    adj = "is too short"
elif tweet <= max_length:
    status = "OK"
    adj = "will work"
else:
    status = "Error"
    adj = f"is {tweet - max_length} chars too long"
# print response
print(f"{status}!!! This {tweet} char tweet {adj}.")
