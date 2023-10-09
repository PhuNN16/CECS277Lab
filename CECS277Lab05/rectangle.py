class rectangle:
    def __init__(self, w, h) -> None:
        "Sets all attributes to their initial values"
        self.x = 0
        self.y = 0
        self.width = w
        self.height = h


    def get_coords(self):
        "Returns the x and y values as a list"
        return [self.x, self.y]


    def get_dimensions(self):
        "Returns the width and height as a list"
        return [self.width, self.height]


    def move_up(self):
        "Updates the y coordinate in relation to the origin"
        self.y -= 1 


    def move_down(self):
        "Updates the y coordinate in relation to the origin"
        self.y += 1


    def move_left(self):
        "Updates the x coordinate in relation to the origin"
        self.x -= 1


    def move_right(self):
        "Updates the x coordinate in relation to the origin"
        self.x += 1