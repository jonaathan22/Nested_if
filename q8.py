age = int(input("enter age  :"))
mem = input("membership :").upper()

if age > 60 :
    if mem == "YES":
        print("Eligible for discount")
    else :
      print("no eligible")    
else :
    print("no")