import abc

class Entity:
    def __init__(self, name, max_hp) -> None:
        
        self._name = name
        self._hp = max_hp
        self._max_hp = max_hp
        
    @property
    def hp(self):
        """Accesses the hitpoints property"""
        return self._hp
        
    @property
    def name(self) -> str:
        """Accesses the entity name"""
        return self._name
        
    def take_damage(self, dmg):
        '''The entity loses hp'''
        self._hp -= dmg
        if self.hp < 0:
            self._hp = 0
            
    def heal (self):
        '''Restore entity health points to max health'''
        self._hp = self._max_hp
        
    def __str__(self) -> str:
        '''String representation of this object'''
        return f'{self.name}\nHP: {self.hp}/{self._max_hp}'

    @abc.abstractmethod
    def attack(self, entity):
        '''Attacking another entity'''
        pass