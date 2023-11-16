import abc

class Plate(abc.ABC):
    @abc.abstractmethod
    def description(self):
        '''Return the string for a plate'''
        pass

    @abc.abstractmethod
    def area(self):
        '''Returns the integer for area'''
        pass

    @abc.abstractmethod
    def weight(self):
        '''Decrement weight when plate is decorated'''
        pass

    @abc.abstractmethod
    def count(self):
        '''Return the number of food on the plate'''
        pass

    