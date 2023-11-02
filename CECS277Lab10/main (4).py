import check_input
import enemy
import hero
import map
import random

def main():
    '''The user travels through a dungeon to fight monsters, and find the exit'''
    user_name = input("What is your name, traveler? ")
    player = hero.Hero(user_name)
    the_map = map.Map()
    tag = True
    
    
    while tag is True:
        print(player)
        print(the_map.show_map(player.loc))
        print('\n1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit')
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
            monster = enemy.Enemy()
            print('You encountered ', monster)
            while True:
                print('1. Attack', monster.name,'\n2. Run Away')
                choice = check_input.get_int_range('Enter Choice: ', 1, 2)

                if choice == 1:
                    print(player.attack(monster))
                    if monster.hp == 0:
                        print(f'You have slain {monster.name}\n')
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
            print('Congratulations! You found the exit.')
            tag = False

    print('Game Over')
    
                    
        



main()



# !!! old way of doing randomize direction of running away !!!
# while True:
#     direction = random.randint(1, 4)
#     if direction == 1 and player.loc[0] - 1 >= 0 and player.loc[0] - 1 <= len(the_map) - 1:
#         player.go_north()
#         break
#     elif direction == 2 and player.loc[0] + 1 >= 0 and player.loc[0] + 1 <= len(the_map) - 1:
#         player.go_south()
#         break
#     elif direction == 3 and player.loc[1] + 1 >= 0 and player.loc[1] + 1 <= len(the_map[0]) - 1:
#         player.go_east()
#         break
#     elif direction == 4 and player.loc[1] - 1 >= 0 and player.loc[1] - 1 <= len(the_map[0]) - 1:
#         player.go_west()
#         break

# the_map.reveal(player.loc)
# break

# !!! old way of doing movement !!!
# if choice == 1:
#     encounter = player.go_north()
# elif choice == 2:
#     encounter = player.go_south()
# elif choice == 3:
#     encounter = player.go_east()
# elif choice == 4:
#     encounter = player.go_west()
# else:
#     break