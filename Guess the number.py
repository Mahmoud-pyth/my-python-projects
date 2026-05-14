import random
number = int(input('Enter a 4-digits PIN code:\n'))
chose = random.randint(1000,9999)
if len(str(number)) != 4:
  print("please enter a 4-digit PIN code")
elif chose == number:
  print(f"The computer chose, {chose} like you, you won")
else:
  print(f"Sorry the computer chose, {chose} you lost")
