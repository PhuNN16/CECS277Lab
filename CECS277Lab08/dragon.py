import entity
import random


class Dragon(entity.Entity):

    def basic_attack(self, other):
        """A tail attack damaging the hero between 3 to 7 damage"""
        dmg = random.randint(3, 7)
        other.take_damage(dmg)
        return self._name + " smashes you with its tail for " + str(
            dmg) + " damage!"

    def special_attack(self, other):
        """A claw attack damaging the hero between 4 to 8 damage"""
        dmg = random.randint(4, 8)
        other.take_damage(dmg)
        return self._name + " slashes you with its claws for " + str(
            dmg) + " damage!"
