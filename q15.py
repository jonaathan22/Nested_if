BMI = float(input(":"))
if BMI <= 18.5 :
   print("under weight ")
elif BMI >= 18.5 and BMI <= 24.9:
    print("Normal")
elif BMI >= 25 and BMI <= 29.5:
    print("over weight ")
else:
    print("Obese")