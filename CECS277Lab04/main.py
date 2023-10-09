# Name: Phu Nguyen, Sean Nightingale
# Date: 9/12/2023
# Desc: A game that displays a maze for the player to solve.

import check_input

def read_maze():
    '''Reads the text file and formats it into a 2d list'''
    maze_file = open("maze.txt")
    maze = []
    for rows in maze_file:
        line = []
        for letters in rows:
            line.append(letters)
        maze.append(line)
    return maze


def find_start(maze):
    '''Searches through a maze to find the coords for "s", or starting point'''
    current_y = 0
    for y in maze:
        for x in range(len(y)):
            if y[x] == "s": #could have used maze[x][y]
                return [current_y, x]
        current_y += 1


def display_maze(maze, loc):
    '''Reads a 2d list of a maze and displays it. Takes in a 1D list coordinate and replaces that coordinate with X'''
    current_y = 0
    for y in maze:
        current_x = 0
        for x in y:
            if [current_y, current_x] == loc:
                print("X", end="")
            else:
                print(x, end="")
            current_x += 1
        current_y += 1


def main():
    '''    
        maze[Position Y][Position X]
        
        Origin is located in the TOP LEFT CORNER
       
    '''
    print("-Maze Solver-")
    maze = read_maze()
    player_loc = find_start(maze)
    while True:
        display_maze(maze, player_loc)
        print("\n1. Go North", "\n"+
                "2. Go South", "\n"+
                "3. Go East", "\n"+
                "4. Go West")
        
        if maze[player_loc[0]][player_loc[1]] == "f": #breaking out the loop
            print("Congratulations! You solved the maze.")
            break

        choice = check_input.get_int_range("Enter choice: ", 1, 4)
        
        if choice == 1:
            temp = player_loc[0] - 1 #origin starts top left corner
            if maze[temp][player_loc[1]] == "*":
                print("You cannot move there")
            else:
                player_loc[0] -= 1
        
        elif choice == 2:
            temp = player_loc[0] + 1
            if maze[temp][player_loc[1]] == "*":
                print("You cannot move there")
            else:
                player_loc[0] += 1
               
        elif choice == 3:
            temp = player_loc[1] + 1
            if maze[player_loc[0]][temp] == "*":
                print("You cannot move there")
            else:
                player_loc[1] += 1
                
        elif choice == 4:
            temp = player_loc[1] - 1
            if maze[player_loc[0]][temp] == "*":
                print("You cannot move there")
            else:
                player_loc[1] -= 1

main()
