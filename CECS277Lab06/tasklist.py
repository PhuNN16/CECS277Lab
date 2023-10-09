import task



class Tasklist:
    def __init__(self) -> None:
        '''Reads the list of tasks from a file and saves them into tasklist'''
        self.tasklist = []
        
        file = open("tasklist.txt")
        for i in file.readlines():
            attribute = i.strip().split(",")
            temp = task.Task(attribute[0], attribute[1], attribute[2] + "\n")
            self.tasklist.append(temp)
        self.tasklist.sort()
        file.close()

    
    def add_task(self, desc, date, time):
        '''Adds a newly constructed task into tasklist in its properly sorted location'''
        temp = task.Task(desc, date, time)
        self.tasklist.append(temp)
        self.tasklist.sort()
    

    def mark_complete(self):
        '''Removes the completed task from the tasklist'''
        self.tasklist.pop(0)


    def save_file(self):
        '''Writes all of tasklist into a text file'''
        file = open("tasklist.txt", "w")
        for tasks in self.tasklist:
            file.write(tasks.__repr__())
        file.close()

    
    def __getitem__(self, index):
        '''Returns the task by index'''
        return self.tasklist[index]


    def __len__(self):
        '''Returns the number of tasks'''
        return len(self.tasklist)

