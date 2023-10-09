class Task:
    def __init__(self, desc, date, time) -> None:
        '''Sets the class's attributes'''
        self.description = desc
        self.date = date    #"MM/DD/YYYY"
        self.time = time    #"HH:MM"


    def __str__(self):
        '''Returns the task information to the user'''
        return f"{self.description} - Due: {self.date} at {self.time}"


    def __repr__(self):
        '''Returns a string in proper formatting'''
        return f"{self.description},{self.date},{self.time}"


    def __lt__(self, other):
        '''Sorts the tasks by due date priority'''
        if self.date[6:10] < other.date[6:10]:
            return True
        elif self.date[6:10] == other.date[6:10]:
            if self.date[0:2] < other.date[0:2]:
                return True
            elif self.date[0:2] == other.date[0:2]:
                if self.date[3:5] < other.date[3:5]:
                    return True
                elif self.date[3:5] == other.date[3:5]:
                    if self.time[0:2] < other.time[0:2]:
                        return True
                    elif self.time[0:2] == other.time[0:2]:
                        if self.time[3:5] < other.time[3:5]:
                            return True
                        elif self.time[3:5] == other.time[3:5]:
                            if ord(self.description) < ord(other.description):
                                return True
        return False



