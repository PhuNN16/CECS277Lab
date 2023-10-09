import check_input
import rectangle


def display_grid(grid):
    "Displays the updated contents of the grid"
    for columns in range(len(grid)):
        for rows in range(len(grid[columns])):
            print(grid[columns][rows], end=" ")
        print()  #split the rows into columns


def reset_grid(grid):
    "Resets the grid and removes the previous rectangle"
    for columns in range(len(grid)):
        for rows in range(len(grid[columns])):
            grid[columns][rows] = "."


def place_rect(grid, rect):
    "Overwrites the dots within the bounds of the rectangle with stars"
    dimensions = rect.get_dimensions()
    vertex1 = rect.get_coords()

    vertex2 = vertex1[1] + dimensions[
        1]  #vertex1 y-coords + height (top left is (0,0))
    vertex3 = vertex1[0] + dimensions[0]  #vertex1 x-coords + width

    for columns in range(len(grid)):
        for rows in range(len(grid[columns])):
            if (columns >= vertex1[1] and columns < vertex2
                    and rows >= vertex1[0] and rows < vertex3):
                grid[columns][rows] = "*"


def main():
    width = check_input.get_int_range("Enter rectangle width: ", 1, 5)
    height = check_input.get_int_range("Enter rectangle height: ", 1, 5)
    rect = rectangle.rectangle(width, height)

    grid = []
    for columns in range(20):
        temp = []
        for rows in range(20):
            temp.append(".")
        grid.append(temp)

    while True:
        place_rect(grid, rect)
        display_grid(grid)

        print("Enter Direction: ", "\n" + "1. Up", "\n" + "2. Down",
              "\n" + "3. Left", "\n" + "4. Right", "\n" + "5. Quit")
        movement = check_input.get_int_range("", 1, 5)

        if movement == 1:
            rect.move_up()
        elif movement == 2:
            rect.move_down()
        elif movement == 3:
            rect.move_left()
        elif movement == 4:
            rect.move_right()
        elif movement == 5:
            break

        if (rect.get_coords()[0] < 0 or rect.get_coords()[0] >
            (20 - rect.width)):
            print("Cannot move the rectangle out of bounds.")
            if movement == 3:
                rect.move_right()
            elif movement == 4:
                rect.move_left()

        if (rect.get_coords()[1] < 0 or rect.get_coords()[1] >
            (20 - rect.height)):
            print("Cannot move the rectangle out of bounds.")
            if movement == 1:
                rect.move_down()
            elif movement == 2:
                rect.move_up()

        reset_grid(grid)


main()
