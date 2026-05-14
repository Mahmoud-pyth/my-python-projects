print("Welcome to place the rabbit")
place = (["🌳", "🌳", "🌳"], ["🌳", "🌳", "🌳"], ["🌳", "🌳", "🌳"])
print(f"{place[0]}\n{place[1]}\n{place[2]}\n")
print("Where should the rabbit go?🐇...")
option = input("Please choose a row and a column:")
if len(option) != 2:
 print("Please enter a number of 2-digits")
 exit()
row = int(option[0])
column = int(option[1])
place[row-1][column-1] = "🐇"
print(f"{place[0]}\n{place[1]}\n{place[2]}\n")
