import random
print("Welcome to the coin Guessing game!")
print("chose a method to toss the coin")
print("1. Using random.random()")
print("2. Using random.randint()")
chose = input("Enter your choice: (1 or 2)\n")
if chose == "1":
  guess = random.random()
  if guess >= 0.5:
    result = "Head"
  else:
    result = "Tail"
elif chose == "2":
  guess = random.randint(0,1)
  if guess == 1:
    result = "Head"
  else:
    result = "Tail"
else:
  print("please enter a valid choice")
  exit()
option = input("Enter your guess: (Head or Tail)\n")
if option.lower() == result.lower():
  print(f"congratulations! you guessed right")
else:
  print("you guessed wrong. try again")
print(f"The computer chose {result}")
