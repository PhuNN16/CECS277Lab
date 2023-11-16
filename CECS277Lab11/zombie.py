import entity
import random

class Zombie(entity.Entity):
    """
    This class will create the expirienced level variant of a Zombie.
    """
    def __init__(self) -> None:
        name = 'Enraged Zombie'
        hp = random.randint(8, 10)
        super().__init__(name, hp)

    def attack(self, entity):
        dmg = random.randint(5, 12)
        entity.take_damage(dmg)
        return f'{self.name} attacks {entity.name} for {dmg} damage.'
