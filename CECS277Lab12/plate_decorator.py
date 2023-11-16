import abc
import plate

class PlateDecorator(plate.Plate, abc.ABC):
    def __init__(self, p) -> None:
        '''Construct the decorator'''
        self._plate = p

    def description(self) -> str:
        '''Calls plate description to decorate it'''
        return self._plate.description()

    def area(self) -> int:
        '''Calls plate area to decorate it'''
        return self._plate.area()

    def weight(self) -> int:
        '''Calls plate weight to decorate it'''
        return self._plate.weight()

    def count(self) -> int:
        '''Calls plate count to increment the number of food'''
        return self._plate.count()