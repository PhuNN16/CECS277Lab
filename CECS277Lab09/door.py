import abc


class Door(abc.ABC):
    '''Abstract class for doors where user will need to override the methods'''
    @abc.abstractmethod
    def examine_door(self):
        pass

    @abc.abstractmethod
    def menu_options(self):
        pass

    @abc.abstractmethod
    def get_menu_max(self):
        pass

    @abc.abstractmethod
    def attempt(self):
        pass

    @abc.abstractmethod
    def is_unlockedself(self):
        pass

    @abc.abstractmethod
    def clue(self):
        pass

    @abc.abstractmethod
    def success(self):
        pass
