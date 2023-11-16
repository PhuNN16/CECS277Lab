class Map:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        '''Initialize a singleton class object'''
        if not Map._initialized:
            self.load_map(0)
            Map._initialized = True

    def __getitem__(self, row):
        '''Grabs the the row of the map'''
        return self._map[row]

    def __len__(self):
        '''Returns the number of rows in the map'''
        return len(self._map)

    def show_map(self, loc):
        '''Printing the grid of the map with the hero's location'''
        string = ''
        for rows, y in enumerate(self._map):
            for columns, x in enumerate(y):
                if [rows, columns] == loc:
                    string += '* '
                elif self._revealed[rows][columns] is True:
                    string += self._map[rows][columns] + ' '
                else:
                    string += 'x '
            string += '\n'
        return string

    def reveal(self, loc):
        '''Reveal the letter underneath the grid '''
        self._revealed[loc[0]][loc[1]] = True
    
    def remove_at_loc(self, loc):
        '''Change the letter underneath the grid to n'''
        self._map[loc[0]][loc[1]] = 'n' 

    def load_map(self, map_num):
        """Fills the playable map with the correct permutation"""
        map = ['map1.txt', 'map2.txt', 'map3.txt']
        file = open(map[map_num])
        self._map = []
        self._revealed = []
        for row, y in enumerate(file):
            list_map = []
            list_reveal = []
            for columns, x in enumerate(y):
                if x != ' ' and x != '\n':
                    list_map.append(x)
                list_reveal.append(False)
            self._map.append(list_map)
            self._revealed.append(list_reveal)
