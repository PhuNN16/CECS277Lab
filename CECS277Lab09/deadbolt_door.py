import door
import random

class DeadboltDoor(door.Door):
    def __init__(self) -> None:
        '''Initialize the state of the bolt and keep user input'''
        # self._bolt1 = random.randint(1, 2)
        # if self._bolt1 == 2:
        #     self._bolt2 = 1
        # else:
        #     self._bolt2 = random.randint(1, 2)
        # self._bolt2 = random.randint(1, 2)
        self._bolt1 = 2
        self._bolt2 = 2
        self._input = 0

    def examine_door(self):
        '''Return the description of the door'''
        return "A door with two deadbolts. Both need to be unlocked to open the door, but you can’t tell if each one is locked or unlocked."    

    def menu_options(self):
        '''return the string for the menu'''
        return "1. Toggle bolt 1\n2. Toggle bolt 2\n"

    def get_menu_max(self):
        '''return the number of options that this door has'''
        return 2

    def attempt(self, option):
        '''The user pick a bolt to toggle and switch state between even and odd'''
        self._input = option
        if self._input == 1:
            self._bolt1 += 1
            return "You toggle the first bolt."
        else:
            self._bolt2 += 1
            return "You toggle the second bolt."

    def is_unlockedself(self):
        '''return true if both bolts are even and false otherwise'''
        # if (self._bolt1 % 2 and self._bolt2 % 2) == 0:
        if self._bolt1 % 2 == 0 and self._bolt2 % 2 == 0:
            return True
        return False

    def clue(self):
        '''Return the clue after the user's failed attempt'''
        # if self._bolt1 % 2 == 0 or self._bolt2 % 2 == 0:
        if self._bolt1 % 2 == 0 and self._bolt2 % 2 == 0:
            return "You jiggle the door...it seems like one of the bolts is unlocked."
        else:
            return "You jiggle the door...it seems like it's completely locked."

    
    def success(self):
        '''return the string when the door is unlocked'''
        return "You unlocked both deadbolts and opened the door\n"

