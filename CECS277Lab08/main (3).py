import random
import hero
import dragon
import fire_dragon
import flying_dragon
import check_input

# Names: Phu Nguyen, Sean Nightingale
# Date:  10/10/2023
# Desc:  A program that lets the user battle 3 unique dragons as a hero.

def main():
    """Creates the entity instances and their interactions"""
    dragon_list = [dragon.Dragon("Deadly Nadder" , 10), fire_dragon.FireDragon("Gronkle", 15, 3), flying_dragon.FlyingDragon("Timberjack", 20, 5)]
    player_name = input("What is your name, challenger? \n")
    print(
        f"Welcome to dragon training, {player_name} \nYou must defeat 3 dragons."
    )
    player = hero.Hero(player_name, 50)

    while True:
        """Loops through the battle interface until either the hero, or all 3 dragons are killed"""
        
        print(f"\n{player}")
        for i in range(len(dragon_list)):
            print(f"{i + 1}. Attack {dragon_list[i]}")
        dragon_choice = check_input.get_int_range(
            "Choose a dragon to attack: ", 1, len(dragon_list)) - 1
        print("\nAttack with:\n1. Sword (2 D6)\n2. Arrow (1 D12)")
        
        attack_choice = check_input.get_int_range("Enter weapon: ", 1, 2)
        if attack_choice == 1:
            print(player.basic_attack(dragon_list[dragon_choice]))
        elif attack_choice == 2:
            print(player.special_attack(dragon_list[dragon_choice]))

        if dragon_list[dragon_choice].hp <= 0:
            dragon_list.pop(dragon_choice)
            if len(dragon_list) == 0:
                print(
                    "\nCongratulations! You have defeated all 3 dragons, you have passed the trials."
                )
                break
        dragon_choice = random.randint(1, len(dragon_list)) - 1
        attack_choice = random.randint(1, 2)
        
        if attack_choice == 1:
            print(dragon_list[dragon_choice].basic_attack(player))
        elif attack_choice == 2:
            print(dragon_list[dragon_choice].special_attack(player))

        if player.hp <= 0:
            print("You have been defeated.")
            break


main()
