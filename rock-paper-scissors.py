import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print('Hello! This is a game of rock-paper-scissors. The game is aganst randomized computer.')
computer_input = random.randint(1, 3)
print('Please choose your sign:\n1 - rock\n2 - paper\n3 - scissors')
player_input = int(input())
if player_input > 3 or player_input < 1:
  print('You typed invalid number, you lose!')
else:
  if computer_input == 1:
    print("Computer chose rock:")
    print(rock)
  elif computer_input == 2:
    print("Computer chose paper:")
    print(paper)
  elif computer_input == 3:
    print("Computer chose scissors:")
    print(scissors)
  
  if player_input == 1:
    print("You chose rock:")
    print(rock)
  elif player_input == 2:
    print("You chose paper:")
    print(paper)
  elif player_input == 3:
    print("You chose scissors:")
    print(scissors)
  
  if (computer_input == 1 and player_input == 3) or (computer_input == 2 and player_input == 1) or (computer_input == 3 and player_input == 2):
    print('You lose!')
  elif computer_input == player_input:
    print('It is a draw!')
  else:
    print('You win')
  
  
  
