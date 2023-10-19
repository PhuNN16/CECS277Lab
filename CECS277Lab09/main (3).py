import check_input
import basic_door
import deadbolt_door
import locked_door
import random


def open_door(door):
    '''The steps to open the door'''
    print(door.examine_door())
    while True:
        choice = check_input.get_int_range(door.menu_options(), 1, door.get_menu_max())
        print(door.attempt(choice))
        if door.is_unlockedself():
            break
        print(door.clue())
    print(door.success())


def main():
    '''An escape room game where you have to break out of 3 random door'''
    print("Welcome to the escape room.\nYou must unlock 3 doors to escape...")
    for i in range(3):
        door1 = basic_door.BasicDoor()
        door2 = deadbolt_door.DeadboltDoor()
        door3 = locked_door.LockedDoor()
        list_of_door = [door1, door2, door3]
        open_door(list_of_door[random.randint(0, 2)])
        # open_door(door1)
    print("Congratulations! you escaped this time.")


main()
