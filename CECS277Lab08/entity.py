import abc


class Entity(abc.ABC):

    def __init__(self, name, max_hp):
        """Initializes the name, maximum hitpoints and current hitpoints"""
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp

    @property
    def name(self):
        """Accesses the name property"""
        return self._name

    @property
    def hp(self):
        """Accesses the hitpoints property"""
        return self._hp

    @hp.setter
    def hp(self, hp):
        """sets the property of hitpoints"""
        self._hp = hp
    
    def take_damage(self, dmg):
        """Calculates the hitpoints after an entity recieves damage"""
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def __str__(self):
        """Returns a string of the name and hitpoints remaining of teh entity"""
        return f"{self._name}: {self.hp}/{self._max_hp}"

    @abc.abstractmethod
    def basic_attack(self, other):
        pass

    @abc.abstractmethod
    def special_attack(self, other):
        pass
