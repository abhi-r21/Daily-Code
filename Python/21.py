#Python number guessing game

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guessess = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:

  guess = input("Enter the guess: ")

  if guess.isdigit():
    guess = int(guess)
    guessess += 1

    if guess < lowest_num or guess > highest_num:
      print("The number is out of range")
      print(f"Please select a number between {lowest_num} and {highest_num}")
    elif guess < answer:
      print("Too Low! Try again!")
    elif guess > answer:
      print("Too High! Try again!")
    else:
      print(f"CORRECT! The answer was {answer}")
      print(f"Number of guesses: {guessess}")
      is_running = False
  
  else:
    print("Invalid guess")
    print(f"Please select a number between {lowest_num} and {highest_num}")