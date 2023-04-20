# prompt user for height and weight
try:
    height = float(input("Enter your height in centimeters(cm):\n"))
    weight = float(input("Enter your weight in kilograms(kg):\n"))
except:
    print("please input numeric values only")
    exit()

# height_meters = height / 100
bmi = weight / ((height / 100) ** 2)

# check bmi status
if type(bmi) != type(1.1):
    adj = "not possible to calculate"
elif bmi < 16:
    adj = "severely underweight"
elif bmi < 18.5:
    adj = "underweight"
elif bmi < 25:
    adj = "of a normal weight"
elif bmi < 30:
    adj = "overweight"
elif bmi < 35:
    adj = "moderately obese"
elif bmi < 40:
    adj = "severely obese"
else:
    adj = "morbidly obese"

print(f"your bmi is {round(bmi, 2)}.\nyou are {adj}")

if type(bmi) != type(1.1):
    adj = "not possible to calculate"
elif bmi > 39.9:
    adj = "morbidly obese"
elif bmi > 34.9:
    adj = "severely obese"
elif bmi > 29.9:
    adj = "moderately obese"
elif bmi > 24.9:
    adj = "overweight"
elif bmi > 18.4:
    adj = "of a normal weight"
elif bmi > 15.9:
    adj = "underweight"
else:
    adj = "severely underweight"

print(f"your bmi is {round(bmi, 2)}.\nyou are {adj}")
