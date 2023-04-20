# prompt unit and temperature
unit = input("Enter temperature unit:\nc: Celsius\nf: *Ferenhiet\nk: Kelvin\n")
temp = float(input("Enter temperature value\n"))
# validate water boiling
if unit == "c":
    unit_name = "Celcius"
    if temp >= 100:
        adj = "is boiling"
    else:
        adj = "is not boiling"
elif unit == "f":
    unit_name = "*Ferenhiet"
    if temp >= 212:
        adj = "is boiling"
    else:
        adj = "is not boiling"
elif unit == "k":
    unit_name = "Kelvin"
    if temp >= 373:
        adj = "is boiling"
    else:
        adj = "is not boiling"
else:
    unit_name = "in an unrecognized unit"
    adj = "boiling state can't be validated"

# output
print(f"Your water {adj} at {temp} degrees {unit_name}")
