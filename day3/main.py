# Day 3 of 100 days of code
# Treasure hunt game - choose your own adventure
# ascii art from: https://ascii.co.uk/art/treasure

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure!")

# User chooses to go left or right
choice = str.lower(input("left or right? "))
if choice == "right":
    print("You walked right into a forest fire - that's game over. Better luck next time!")
    exit()
else:
    print("Great job! You survived the first step!")

# User chooses to swim or wait
choice = str.lower(input("swim accross the atlantic or wait? "))
if choice == "swim":
    print("You got eaten by a shark - that's game over. Better luck next time!")
    exit()
else:
    print("Great job! You survived the second step!")

# User chooses a door
choice = str.lower(input("Choose a door: red, blue, or yellow? "))
if choice == "red":
    print("You got drown in a pool of blood - that's game over. Better luck next time!")
    exit()
elif choice == "blue":
    print("You fell into a deep depression - that's game over. Better luck next time!")
    exit()
else:
    print("Great job! You've found the treasure and can now afford health insurance!! You win!!")
