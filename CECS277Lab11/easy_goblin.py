import entity
import random

class EasyGoblin(entity.Entity):
    """
    This class will create the beginner level variant of a Goblin.
    """
    def __init__(self) -> None:
        name = 'Goblin'
        hp = random.randint(4, 6)
        super().__init__(name, hp)

    def attack(self, entity):
        dmg = random.randint(2, 5)
        entity.take_damage(dmg)
        return f'{self.name} attacks {entity.name} for {dmg} damage.'