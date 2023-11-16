import entity
import random

class Goblin(entity.Entity):
    """
    This class will create the expirienced level variant of a Goblin.
    """
    def __init__(self) -> None:
        name = 'Violent Goblin'
        hp = random.randint(8, 12)
        super().__init__(name, hp)

    def attack(self, entity):
        dmg = random.randint(6, 12)
        entity.take_damage(dmg)
        return f'{self.name} attacks {entity.name} for {dmg} damage.'
        