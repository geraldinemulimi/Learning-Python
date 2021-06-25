from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess,answer,turns):
  """checks your guess against the answer and shows the number of attempts remaining."""
  if guess > answer:
    print("too high")
    return turns -1
  elif guess < answer:
    print("too low")
    return turns -1
  else:
    print(f"you got it!The answer was {answer}")
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "hard":
    return HARD_LEVEL_TURNS
  else:
    return EASY_LEVEL_TURNS
   
def game():

  print("Welcome to the Number Guessing Game")
  print("I am thinking of a number between 1 and 100")

  answer = randint(1,100)
  print(f"Psst, the correct answer is {answer}")

  turns = set_difficulty()

  guess = 0
  while guess!= answer:
    print(f"you have {turns} attempts remaining to guess the number.")
    guess = int(input("make a guess: "))

    turns = check_answer(guess,answer,turns)
    if turns == 0:
      print("you have run out of gueses,you lose!")
      return
game()