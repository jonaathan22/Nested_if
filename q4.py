character = input("")
if character in 'a,e,i,o,u':
    print("vowels")
else : 
   if character.isupper():
    print("consonant and upper")
   else :
      print("consonant and lower")