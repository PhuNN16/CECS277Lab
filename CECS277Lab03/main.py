# Sean Nightingale, Phu Nguyen
# 9/6/2023
# Desc: This programs runs a two player dice game. It rolls the dice, keeps track of score, and calculates the winner at the end.

import random
import check_input

def roll_dice(dice):
    '''This function creates a list of randomly rolled dices in descending order'''
    for i in range(len(dice)):
        dice[i] = random.randint(1, 6)
        dice.sort(reverse = True)


def display_dice(name, dice):
    '''Formats and displays the chosen list in the console for the players to see'''
    print(f"{name} = ", end="")
    for i in dice:
        print(i, end=" ")
    print() #fixes issue with end=" "
    

def find_winner(player_points):
    '''This function calculates and displays the end reslts as well as which player won'''
    print("Score: ")
    print(f"Player #1: {player_points[0]}")
    print(f"player #2: {player_points[1]}")

    if player_points[0] > player_points[1]:
        print("Player #1 won!")
    elif player_points [0] == player_points[1]:
        print("It's a tie!")
    else:
        print("Player #2 won!")

def main():
    '''This is the main game that is put together with the help of the other functions'''
    player_score = [0, 0]
    print("- Ship, Captain, and Crew! –\n")

    for i in range(2):
        rolls = [0, 0, 0, 0, 0] #the game starts with 5 rolls
        keeps = []
        print(f"Player #{i+1}'s turn:") #i starts at 0, so +1 to get which player's turn
        
        
        for j in range(3):
            
            roll_dice(rolls)
            display_dice("Rolls", rolls)
            if 6 in rolls and len(keeps) == 0: #if keeps is empty add 6
                keeps.append(6)
                rolls.remove(6)
                print("Yo Ho Ho! Ye secured a ship!")
            if 5 in rolls and len(keeps) == 1: #len(keeps) = 1 if 6 is found
                keeps.append(5)
                rolls.remove(5)
                print("Shiver me timbers! A Captn'!")
            if 4 in rolls and len(keeps) == 2: #len(keeps) = 2 if 6 & 5 are found
                keeps.append(4)
                rolls.remove(4)
                print("Ye bribed a crew with Grog!")
            
            display_dice("Keep", keeps)
            
            if len(keeps) == 3:
                cargo = rolls
                display_dice("Cargo", cargo)
                cargo_points = cargo[0] + cargo[1]
                print(f"Your cargo points are: {cargo_points}")
                player_score[i] = cargo_points

            
            if j < 2:
                play_again  = check_input.get_yes_no("\nRoll again? ") #\n for formatting
                if play_again is False:
                   print(f"Player #{i+1}'s score: {player_score[i]} \n")
                   break
            else:
                print(f"Player #{i+1}'s score: {player_score[i]} \n")

    find_winner(player_score) 
        
        
        

main()