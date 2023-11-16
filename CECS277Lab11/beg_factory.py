import enemy_factory
import easy_zombie
import easy_skeleton
import easy_goblin
import random

class BeginnerFactory(enemy_factory.EnemyFactory):
    """
    This factory will create a random enemy that is easy to defeat.
    """
    def create_random_enemy(self):
        i = random.randint(0, 2)
        monster = [easy_goblin.EasyGoblin, easy_skeleton.EasySkeleton, easy_zombie.EasyZombie]
        return monster[i]()
        