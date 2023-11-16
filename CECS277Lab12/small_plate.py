import plate

class SmallPlate(plate.Plate):
    def description(self):
        '''Return the string for a plate'''
        return 'Sturdy 10 inch paper plate with'

    def area(self):
        '''Returns the integer for area'''
        return 78

    def weight(self):
        '''Decrement weight when plate is decorated'''
        return 32

    def count(self):
        '''Return the number of food on the plate'''
        return 0