import enemy_factory
import goblin
import random
import skeleton
import zombie

class ExpertFactory(enemy_factory.EnemyFactory):
    """
    This factory will create a random enemy that is challenging to defeat.
    """
    def create_random_enemy(self):
        monster = [goblin.Goblin, skeleton.Skeleton, zombie.Zombie]
        return monster[random.randint(0, 2)]()