import entity
import random

class EasyZombie(entity.Entity):
    """
    This class will create the beginner level variant of a Zombie.
    """
    def __init__(self) -> None:
        name = 'Zombie'
        hp = random.randint(4, 5)
        super().__init__(name, hp)

    def attack(self, entity):
        dmg = random.randint(1, 5)
        entity.take_damage(dmg)
        return f'{self.name} attacks {entity.name} for {dmg} damage.'