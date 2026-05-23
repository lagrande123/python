height = float(input("enter your height"))
weight = float(input("enter your weight"))
BMI = weight / (height/100)**2
if BMI <= 18.5:
    print("underweight")
elif BMI <= 24.9:
    print("you are healthy")
elif BMI <= 29.9:
    print("overweight")
elif BMI <= 34.9:
    print("severe overweight")
elif BMI <= 39.9:
    print("obese")
else:
    print("severe obese")