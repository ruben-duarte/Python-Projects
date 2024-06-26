from random import randint

def user_guess_number(): 
    number = int(input("Enter a number between 1 and 100:  "))
    return number

#Enter a number 
print("="*12)
user_number = user_guess_number()
print("="*12)
print()
try_again = True
#create random number Primer enfoque
pc_number = randint(1, 100)

while try_again:
  #check if guess is correct
  if user_number == pc_number:        
    print("Correct!")
    try_again = False
  else:
    #if not guess again
    if user_number < pc_number:
      print("too low, guess again")
      user_number = user_guess_number()

    print("too high, guess again")
    user_number = user_guess_number()
      



