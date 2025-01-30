print("Welcome to the guessing game!")
print("I'm thinking a nuber from 1-100.")
import random
rand_number= random.randint(1,101)
print(rand_number)
difficulty= input("Choose difficulty. Type 'easy' or 'hard': ")


def game(num):
  num_of_guesses= num
  print(f"You have {num} of guesses.")
  while num_of_guesses > 0:
    guess=int(input("Make a guess: "))
    if guess > rand_number:
      num_of_guesses= num_of_guesses-1
      print(f"Too high. You have {num_of_guesses} guesses left")
    elif guess < rand_number:
      num_of_guesses=num_of_guesses-1
      print(f"Too low. You have {num_of_guesses} guesses left")
    elif guess == rand_number:
      print(f"Your guess {guess} is right. You Win!")
      break
  if num_of_guesses ==0:
    print ("You lose")


if difficulty == "hard":
  game(5)
if difficulty == "easy":
  game(10)
  
