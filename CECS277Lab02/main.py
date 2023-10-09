import check_input
import random

#Name: Sean Nightingale, Phu Nguyen
#Date: 8/28/2023
#Desc: Prompts user to bet on where the queen is, given that it is hidden under one of three cards. 


def get_users_bet(money):
  '''Prompts user about how much to bet as well as checks if the users input is valid'''
  print(f"You have ${money}")
  return check_input.get_int_range("How much you wanna bet? ", 1, money)


def get_users_choice():
  '''Prompts user to pick 1 of 3 cards, and checks if the user's input is valid'''
  prompt = "Find the queen: "
  return check_input.get_int_range(prompt, 1, 3)


def display_queen_loc(queen_loc):
  '''Both displays and randomly places a queen card amoungst the kings'''
  cards = ["K", "K", "K"] #base display of cards. Location 0-2 for card 1-3
  cards[queen_loc] = "Q"  #updates list to place the queen card within
  print("+-----+ +-----+ +-----+","\n"
       "|     | |     | |     |", "\n"
       f"|  {cards[0]}  | |  {cards[1]}  | |  {cards[2]}  |", "\n" 
       "|     | |     | |     |", "\n"
       "+-----+ +-----+ +-----+")


def main():
  '''The main game where we implement all of the previous functions together'''
  balance = 100 #starting balance
  print("-Three card Monte\nFind the queen to double your bet!\n") 
  
  while balance > 0:  #loop to continue play if balance is more than 0
    queen_loc = random.randint(0, 2)  
    bet = get_users_bet(balance)
    print("+-----+ +-----+ +-----+","\n"
          "|     | |     | |     |", "\n"
          "|  1  | |  2  | |  3  |", "\n"
          "|     | |     | |     |", "\n"
          "+-----+ +-----+ +-----+")  
    user_choice = get_users_choice()
    display_queen_loc(queen_loc)
    
    if user_choice - 1 == queen_loc: # -1 because index starts at 0
      balance = balance + (bet * 2)
      print("You got lucky this time...")
    else:
      balance -= bet
      print("Sorry... you lose.")
      
    if balance == 0:
      print("You're out of money. Beat it loser!")
    else:
      play_again = check_input.get_yes_no("Play again? (Y/N): ")
      if play_again is False: #if user says "N" then it returns False.
        break #break exits out of the while loop

main()