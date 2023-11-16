import plate

class LargePlate(plate.Plate):
    def description(self):
        '''Return the string for a plate'''
        return 'Flimsy 12 inch paper plate with'

    def area(self):
        '''Returns the integer for area'''
        return 113

    def weight(self):
        '''Returns the intger for the weight'''
        return 24

    def count(self):
        '''Return the number of food on the plate'''
        return 0