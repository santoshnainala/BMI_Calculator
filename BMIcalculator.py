 #BMI calculator
height = float(input("Enter your height in cms : "))
weight = float(input("Enter your weight in kgs : "))
BMI = weight/(height/100)**2
print("Your BMI is : ",BMI)
if BMI <= 18.4:
    print("you are under weight")
elif BMI <= 24.9:
    print("you are healthy")
elif BMI <= 29.9:
    print("you are overweight")
elif BMI <= 34.9:
    print("you are severally over weight")
elif BMI <= 39.9:
    print("you are obese")
else:
    print("you are severally obese")
