import entity
import random

class EasySkeleton(entity.Entity):
    """
    This class will create the beginner level variant of a Skeleton.
    """
    def __init__(self) -> None:
        name = 'Skeleton'
        hp = random.randint(3, 4)
        super().__init__(name, hp)

    def attack(self, entity):
        dmg = random.randint(1, 4)
        entity.take_damage(dmg)
        return f'{self.name} attacks {entity.name} for {dmg} damage.'