import door
import random

class BasicDoor(door.Door):
    def __init__(self) -> None:
        '''Initialize the door as either push or pull and keep user input'''
        self._state = random.randint(1, 2)
        self._input = 0

    def examine_door(self):
        '''Return the description of the door'''
        return "A door that is either pushed or pulled."

    def menu_options(self):
        '''return the string for the menu'''
        return "1. Push\n2. Pull\n"

    def get_menu_max(self):
        '''return the number of options that this door has'''
        return 2

    def attempt(self, option):
        '''return the string for when the user try to push or pull and set _input to user input'''
        self._input = option
        if self._input == 1:
            return "You pushed the door."
        else:
            return "You pulled the door."

    def is_unlockedself(self):
        '''return true if the user pick the correctly'''
        if self._state == self._input:
            return True
        return False

    def clue(self):
        '''Return the clue after the user's failed attempt'''
        return "Try the other way."

    def success(self):
        '''return the string when the door is unlocked'''
        return "Congratulations, you opened the door.\n"