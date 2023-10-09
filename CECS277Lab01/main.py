import random
import check_input


# Name: Phu Nguyen, Sean Nightingale
# Date: 8/24/2023
# Desc: Prompting the user to guess a random number between 1 - 100. We will tell them too high or too low and keep track of the number of guesses
def main():
  print("I'm thinking of a number. ", end="")
  random_num = random.randint(1, 100)
  guess = None  #instantiate variable
  num_tries = 0
  prompt = "Make a guess:"
  while guess != random_num:
    guess = check_input.get_int_range(prompt, 1, 100)
    num_tries += 1
    prompt = "Guess again:"
    if guess < random_num:
      print("Too low!", end=" ")
    elif guess > random_num:
      print("Too high!", end=" ")
  print(f"Correct! You got it in {num_tries} tries.")
main()