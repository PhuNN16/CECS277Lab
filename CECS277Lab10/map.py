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
            file = open('map.txt')
            self._map = []
            self._revealed = []
            for row, y in enumerate(file):
                list_map = []
                list_reveal = []
                for columns, x in enumerate(y):
                    if x != ' ' and x != '\n':
                        list_map.append(x)
                    if row == 0 and columns == 0:
                        list_reveal.append(True)
                    else:
                        list_reveal.append(False)
                self._map.append(list_map)
                self._revealed.append(list_reveal)

            # self._reveal = []
            # for row in range(len(self._map)):
            #     list = []
            #     for columns in row:
            #         if row == 0 and columns == 0:
            #             list.append(True)
            #         list.append(False)
            #     self._revealed.append(list)
                    
            Map._initialized = True

    def __getitem__(self, row):
        '''Grabs the the row of the map'''
        return self._map[row]

    def __len__(self):                # for some reason this confuses me
        '''Returns the number of rows in the map'''
        return len(self._map)

    def show_map(self, loc):
        '''Printing the grid of the map with the hero's location'''
        string = ''
        for rows, y in enumerate(self._map):
            for columns, x in enumerate(y):
                if self._revealed[rows][columns] is True:
                    if [rows, columns] == loc:
                        string += '* '
                    else:
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
        self._map[loc[0]][loc[1]] = 'n' #SWITCH AROUND LOC IF NEEDED
