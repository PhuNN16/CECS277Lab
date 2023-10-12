import entity
import random


class Hero(entity.Entity):

    def basic_attack(self, other):
        """Does a specified amount of damage to the other entity """
        dmg = (random.randint(1, 6)) + (random.randint(1, 6))
        other.take_damage(dmg)
        return self._name + " slashes the " + other._name + " with their sword for " + str(dmg) + " damage!"

    def special_attack(self, other):
        """Does a specified amount of damage to the other entity"""
        dmg = random.randint(1, 12)
        other.take_damage(dmg)
        return self._name + " hits the " + other._name + " with an arrow for " + str(dmg) + " damage!"
