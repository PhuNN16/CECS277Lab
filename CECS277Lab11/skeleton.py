import entity
import random

class Skeleton(entity.Entity):
    """
    This class will create the expirienced level variant of a Skeleton.
    """
    def __init__(self) -> None:
        name = 'Armored Skeleton'
        hp = random.randint(6, 10)
        super().__init__(name, hp)

    def attack(self, entity):
        dmg = random.randint(6, 10)
        entity.take_damage(dmg)
        return f'{self.name} attacks {entity.name} for {dmg} damage.'
