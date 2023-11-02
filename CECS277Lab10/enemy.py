import entity
import random

class Enemy(entity.Entity):
    def __init__(self) -> None:
        '''Initializing the enemy with a name and health points'''
        list_of_name = ['Aiden, The Not So Angry Giant', 
                        'Ashley, Eeper Sleeper', 
                        'Chris, Bane of ស្ត្រី', 
                        'Matt, Scourge of the Court',
                        'Andrea, The Andyeli', 
                        'Manuel, Legend of the League',
                        'Anh, Eater of Men',
                        'Sean, wait why am I here?!?'
                       ]
        name = list_of_name[random.randint(0, len(list_of_name) - 1)]
        # name = list_of_name[2]
        hp = random.randint(4, 8)
        super().__init__(name, hp)

    def attack(self, entity) -> str:
        '''Attacking another entity'''
        dmg = random.randint(1, 4)
        entity.take_damage(dmg)
        return f'{self.name} attacks {entity.name} for {dmg} damage.'