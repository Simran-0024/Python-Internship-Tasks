# Importing the random module
import random

# Generating the random number
rand =random.randint(1,100)

# Asking for the number of chances the player wants to play
n=int(input("Enter the number of chances you want to guess: "))
for i in range(1,n+1):
  
  # Asking the player for their guess or if they want to exit
  guess = input("Guess the number (or type 'exit' to quit): ")
  if guess.lower()=="exit":
    exit()
    
  # Casting the string to integer
  try:
    guess = int(guess)
  except ValueError:
    print("Invalid input! Please enter a number or 'exit'.")
    continue
  
  # Checking if the guess is correct or not and giving the sugessions accordingly
  if guess==rand:
    print("Congratulations! You guessed the number correctly in",i,"chances.")
  elif guess<rand:
    print("opps! Too Low....Come on try again!")
  elif guess>rand:
    print("oops! Too High....Come on try again!")
    
    # To display -- when the number of chances user had is over
else:
  print("Sorry! You didn't guess the number correctly in",n,"chances....Wanna Play again...then please run the code again!")