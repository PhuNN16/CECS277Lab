import beg_factory
import check_input
import exp_factory
import hero
import map
import random

# Names: Phu Nguyen, Sean Nightingale
# Date:  11/6/2023
# Desc:  A program that lets the user battle monsters through a maze to find the exit.



def main():
    '''The user travels through a dungeon to fight monsters, and find the exit'''
    user_name = input("What is your name, traveler? ")
    player = hero.Hero(user_name)
    map_num = 0
    the_map = map.Map()
    tag = True

    difficulty = [beg_factory.BeginnerFactory, exp_factory.ExpertFactory]
    diff_choice = check_input.get_int_range('Difficulty:\n1. Beginner\n2. Expert\n', 1, 2)

    print()
    while tag is True:
        print(player)
        print(the_map.show_map(player.loc))
        print('1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit')
        choice = check_input.get_int_range('Enter Choice: ', 1, 5)

        list_of_direction = [
            player.go_north, player.go_south, 
            player.go_east, player.go_west,
        ]
        if choice == 5:
            break
        encounter = list_of_direction[choice - 1]()
        the_map.reveal(player.loc)

        if encounter == 'm':
            
            monster = difficulty[diff_choice - 1]().create_random_enemy()
            print('You encountered ', monster)
            while True:
                print('1. Attack', monster.name,'\n2. Run Away')
                choice = check_input.get_int_range('Enter Choice: ', 1, 2)

                if choice == 1:
                    print(player.attack(monster))
                    if monster.hp == 0:
                        print(f'You have slain a {monster.name}\n')
                        the_map.remove_at_loc(player.loc)
                        break
                    print(monster.attack(player))
                    if player.hp == 0:
                        tag = False
                        break

                else:       
                    while True:
                        direction = random.randint(0, 3)
                        print(direction)
                        move = list_of_direction[direction]()
                        if move != 'o':
                            break

                    the_map.reveal(player.loc)
                    break


        elif encounter == 'o':
            print('You cannot go that way...\n')
        elif encounter == 'n':
            print('There is nothing here...\n')
        elif encounter == 's':
            print('You are back where you started...\n')
        elif encounter == 'i':
            print('You found a Health Potion! You drink it to restore your health.\n')
            the_map.remove_at_loc(player.loc)
            player.heal()
        elif encounter == 'f':
            print('Congratulations! You found the stairs to the next floor of the dungeon.')
            map_num += 1
            the_map.load_map(map_num % 3)
            
    print('Game Over')


main()