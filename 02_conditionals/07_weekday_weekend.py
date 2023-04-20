# prompt for day of week
day = input("what day is it?\nsun: Sunday\nmon: Monday\ntue: Tuesday\nwed: Wednesday\nthu: Thursday\nfri: Friday\nsat: Saturday\n")

if day == "mon" or day == "tue" or day == "wed" or day == "thu" or day == "fri":
    adj = "day"
elif day == "sun" or day == "sat":
    adj = "end"
else:
    print("invalid day")
    exit()

print(f"Today is a week{adj} day")
