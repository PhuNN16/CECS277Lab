import plate_decorator

class Potatoes(plate_decorator.PlateDecorator):

    def description(self) -> str:
        '''Decorate plate with string'''
        return super().description() +' Potatoes and'

    def area(self) -> int:
        '''Decrement area when plate is decorated'''
        return super().area() - 18

    def weight(self) -> int:
        '''Decrement weight when plate is decorated'''
        return super().weight() - 6

    def count(self) -> int:
        '''Increment the amount of food on the plate'''
        return super().count() + 1
