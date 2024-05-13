

print('Welcome to Treasure hunt.\nYour mission is to find the treasure chest.')
choice1 = input('You are at a cross road. On your left you see a trail leading to a lake, on the right you see trail throug dense forest. Where do you want to go? Type "left" or "right".\n')
choice1 = choice1.lower()

if choice1 == "left":
  choice2 = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
  choice2 = choice2.lower()
  if choice2 == "wait":
    door_color = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n')
    door_color = door_color.lower()
    if door_color == "yellow":
      print('You found the treasure! You win!')
    elif door_color == "red":
      print('You enter a room on fire. Game Over.')
    elif door_color == "blue":
      print('You enter a room full of beasts. Game Over.')
    else:
      print("You chose a door that doesn't exist. Game Over.")
  elif choice2 == 'swim':
    print('You decide to swimm to the island. On the way there you get attacked by an angry trout. Game Over.')
  else:
    print(f'You typed {choice2} which is not a valid option. Game Over.')
elif choice1 == 'right': 
  print('You enter the forest and are attaked by a big brown bear. Game Over.')
else:
  print(f'You typed {choice1} which is not a valid option. Game Over.')
print('Thank you for playing! See you next time.')

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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
