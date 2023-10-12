import random
import dragon


class FireDragon(dragon.Dragon):

    def __init__(self, name, max_hp, f_shots):
        """Initializes the name, hitpoints, and amount of special attacks"""
        super().__init__(name, max_hp)
        self.f_shots = f_shots

    def special_attack(self, other):
        """An overidden special attack that only works depended on another parameter"""
        if self.f_shots > 0:
            dmg = random.randint(5, 9)
            other.take_damage(dmg)
            self.f_shots -= 1
            return self.name + " engulfs you in flames for " + str(
                dmg) + " damage!"
        else:
            return self.name + " tries to spit fire at you but is all out of fire shots."

    def __str__(self):
        """Returns the amount of special attack"""
        return super().__str__(
        ) + f"\nFire Shots remaining: {self.f_shots}"  # TODO
