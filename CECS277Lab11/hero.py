import entity
import random
import map


class Hero(entity.Entity):
    def __init__(self, name) -> None:
        '''Initializing hero with name and health points'''
        super().__init__(name, 25)
        self._loc = [0, 0]        # [row, col]

    @property
    def loc(self) -> list:
        """Accessing the hero's location"""
        return self._loc
   
    def attack(self, entity) -> str:
        '''attacking another entity'''
        damage = random.randint(2, 5)
        entity.take_damage(damage)
        return f"{self._name} attacks {entity.name} for {damage} damage."

    def go_north(self) -> chr: #FIX THESE PLS I did it wrong (forgor to read)
        '''The hero moves 1 block north in the grid'''
        the_map = map.Map()
        if self.loc[0] - 1 >= 0 and self.loc[0] - 1 <= len(the_map) - 1:
            self._loc[0] -= 1
            return the_map[self._loc[0]][self._loc[1]]
        return 'o'
    
    def go_south(self) -> chr:
        '''The hero moves 1 block south in the grid'''
        the_map = map.Map()
        if self.loc[0] + 1 >= 0 and self.loc[0] + 1 <= len(the_map) - 1:
            self._loc[0] += 1
            return the_map[self._loc[0]][self._loc[1]]
        return 'o'

    def go_east(self) -> chr:
        '''The hero moves 1 block east in the grid'''
        the_map = map.Map()
        if self.loc[1] + 1 >= 0 and self.loc[1] + 1 <= len(the_map[0]) - 1:
            self._loc[1] += 1
            return the_map[self._loc[0]][self._loc[1]]
        return 'o'

    def go_west(self) -> chr:
        '''The hero moves 1 block west in the grid'''
        the_map = map.Map()
        if self.loc[1] - 1 >= 0 and self.loc[1] - 1 <= len(the_map[0]) - 1:
            self._loc[1] -= 1
            return the_map[self._loc[0]][self._loc[1]]
        return 'o'
        