from random import randint

#Enter a number 
print("="*12)
user_guess_number = int(input("Enter a number between 1 and 100:  "))
print("="*12)
print()
try_again = True
#create random number
pc_number = randint(1, 100)

while try_again:
  #check if guess is correct
  if user_guess_number == pc_number:        
    print("Correct!")
    try_again = False
  else:
    #if not guess again
    if user_guess_number < pc_number:
      print("too low, guess again")
      user_guess_number = int(input("Enter a number between 1 and 100:  "))

    print("too high, guess again")
    user_guess_number = int(input("Enter a number between 1 and 100:  "))
  
      



