import check_input
import deck
import player
import dealer
# Names: Nick Nguyen, Sean Nightingale
# Date: 10/4/2023
# Desc: A program to play the game of black jack between the user and a dealer.


def display_winner(pScore, dScore, points):
    '''Display the winner of that round of blackjack and how many round each person won'''
    if pScore > 21 and dScore > 21 or pScore == dScore:
        print("Neither wins.")
    elif pScore > 21 or dScore > pScore and dScore <= 21:
        points[1] += 1
        print("Dealer wins.")
    else:
        points[0] += 1
        print("Player wins.")
    
    print(f"Player's points: {points[0]}")
    print(f"Dealer's points: {points[1]}")


def main():
    '''A game of blackjack where whoever gets closest to 21 without going over wins'''
    # starting condition 
    print("-Blackjack-")
    deck_of_cards = deck.Deck()
    deck_of_cards.shuffle()
    points = [0, 0]
    #Player's turn
    while True:
        Player = player.Player(deck_of_cards)
        while True:
            print(f"\nPlayer's Card:\n{Player}")
            print("1. Hit\n2. Stay")
            hit_or_not = check_input.get_int_range("Enter Choice: ", 1, 2)
            if hit_or_not == 2:
                break
            else:
                Player.hit()
            if Player.score() > 21:
                print(f"\nPlayer's Card:\n{Player}")
                print("1. Hit\n2. Stay")
                print("Bust!")
                break
        #Dealer's turn
        Dealer = dealer.Dealer(deck_of_cards)
        print(Dealer.play())
        #winner
        display_winner(Player.score(), Dealer.score(), points)
        #check to see when reset deck
        if len(deck_of_cards) <= 15:
            deck_of_cards = deck.Deck()
            deck_of_cards.shuffle()
        #play again?
        play_again = check_input.get_yes_no("Play again? (Y/N): ")
        if play_again is False:
            break


main()