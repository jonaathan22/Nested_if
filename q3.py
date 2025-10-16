age = int(input("age:"))
citizen = input("citizenship:")
if age >= 18:
    if citizen == "Yes":
     print("Eligible to vote")
    else :
     print("not a citizen")
else:
  print("not eligible")
