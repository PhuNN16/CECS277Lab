import abc

class EnemyFactory(abc.ABC):
    """
    This factory creates an abstract method that
    each of the sub-factories will override.
    """
    @abc.abstractmethod
    def create_random_enemy(self):
        pass