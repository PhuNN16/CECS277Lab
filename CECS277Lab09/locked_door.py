import door
import random


class LockedDoor(door.Door):

    def __init__(self) -> None:
        '''Initialize position of key and keep user input as an attribute'''
        self._key_location = random.randint(1, 3)
        self._input = 0

    def examine_door(self):
        return "You encounter a locked door. Look around for the key."

    def menu_options(self):
        return "1. Look under the mat\n2. Look under the flower\n3. Look under fake rock\n"

    def get_menu_max(self):
        '''return the number of options that this door has'''
        return 3

    def attempt(self, option):
        '''User look for key in one of three places return string for the location'''
        self._input = option
        string = "You look under the "
        if option == 1:
            string += "mat."
        elif option == 2:
            string += "flower pot."
        else:
            string += "fake rock."
        return string

    def is_unlockedself(self):
        '''Return true if the user pick the right place to look for the key'''
        if self._input == self._key_location:
            return True
        return False

    def clue(self):
        '''Return the clue after the user's failed attempt'''
        return "Look somewhere else."

    def success(self):
        '''return the string when the door is unlocked'''
        return "You found the key and opened the door.\n"
