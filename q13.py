age = int(input("enter age:"))
weekend = input(" : ").lower

if age < 12:
     print("child")
elif  age > 12 and age <60:
    if weekend == "yes":
     print("10%/ extra adult ticket ")
    else :
     print("adult tickett")
else :
   print("senior ticket")