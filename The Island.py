print("""
          ********* ▀▄▀▄▀▄The Island▄▀▄▀▄▀********

\n""")
print("Welcome to my Island!🏝️🏝️🏝️")
print("There are two doors in front of you: a red door 🚪  and a blue door 🚪.")
door = input("Which door do you want to chose?\n").lower()
if door == "red":
  print("Great! now you entered a room ")
  print("You found three box: white🎁, black🎁, green🎁")
  box = input("Which box will you chose\n").lower()
  if box == "green":
    print("Congratulations🎉🎉🎉! you found the treasure💰💰💰")
  elif box == "black":
    print("Oops! you found a box fulled by snakes🐍🐍🐍")
    print("Game Over☠️☠️")
  elif box == "white":
    print("sorry! you found a box fulled by spiders🕷️🕷️🕷️")
    print("Game over☠️☠️")
  else:
    print("⚠️Please enter a valid box⚠️")
elif door == "blue":
  print("Oops! you chose the crocodile door🐊🐊🐊")
  print("Game over☠️☠️")
else:
  print("⚠️Please enter a valid door⚠️")
