import dragon
import random


class FlyingDragon(dragon.Dragon):

    def __init__(self, name, max_hp, swoops):
        """Initializes the name, hitpoints, and amount of special attacks"""
        super().__init__(name, max_hp)
        self.swoops = swoops

    def special_attack(self, other):
        """An overidden special attack that only works depended on another parameter"""
        if self.swoops > 0:
            dmg = random.randint(5, 8)
            other.take_damage(dmg)
            self.swoops -= 1
            return self.name + " swoops at you for " + str(dmg) + " damage!"
        else:
            return self.name + " tries to swoop down to hit you, but failed."

    def __str__(self):
        """Returns the amount of special attacks"""
        return super().__str__(
        ) + f"\nSwoop attacks remaining: {self.swoops}"  # TODO
