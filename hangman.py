import random
from replit import clear

import hangman_words
end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6
# print(f'Pssst, the solution is {chosen_word}.')
#Create blanks
display = []
for _ in range(word_length):
    display += "_"

from hangman_art import logo
print(logo)


while not end_of_game:
  guess = input("Guess a letter: ").lower()
  clear()
  if guess in display:
    print(f"You've already guessed {guess}")
  for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
          display[position] = letter
  print(f"{' '.join(display)}")
  
  if guess not in chosen_word:
    print(f"You've guessed {guess}, that is not in the word. You lose a life")
    lives -= 1
    if lives == 0:
      print('You lose')
      end_of_game = True

  if '_' not in display:
    end_of_game = True
    print('You win!')
  from hangman_art import stages
  print(stages[lives])


