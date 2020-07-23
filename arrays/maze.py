# +------------+
# |A           |
# |        # # |
# | #          |
# |           #|
# |           #|
# |  #         |
# |   #        |
# |          # |
# |    B       |
# |    # #     |
# +------------+

maze = []
starting_marker = 'A'
end_marker = 'B'
boulder_char = '#'
line_start = '|'
maze_len = 12
maze_width = 10


def initialize(x, y):
    global maze
    maze = [[' ']* y for i in range(x)]

def mark_start_end(start_cord_x, start_cord_y, end_cord_x, end_cord_y):
    maze[start_cord_x][start_cord_y] = starting_marker
    maze[end_cord_x][end_cord_y] = end_marker

def mark_boulder(x_cord, y_cord):
    maze[x_cord][y_cord] = boulder_char

def get_first_last_lines():
    return '+' + ('-' * len(maze)) + '+'


def print_maze():
    print(get_first_last_lines())
    for i in range(maze_width):
        elem = line_start
        for j in range(maze_len):
            elem = elem + maze[j][i]
        elem = elem + line_start
        print(elem)

    print(get_first_last_lines())



initialize(maze_len, maze_width)

mark_start_end(0,0,4,8)
mark_boulder(1,2)
mark_boulder(2,5)
mark_boulder(3,6)
mark_boulder(4,9)
mark_boulder(6,9)
mark_boulder(8,1)
mark_boulder(10,1)
mark_boulder(10,7)
mark_boulder(11,3)
mark_boulder(11,4)
print_maze()




#
# Your previous Plain Text content is preserved below:
#
# Introduction:
# You find yourself on a rectangular sheet of ice surrounded by walls.
# There are some boulders sitting on the ice.
# Your exit coordinates are given to you.
#
# Sample Maze:
# The maze is provided as a list of 0-indexed coordinates:
#
# 12 10
# 0 0
# 4 8
# 1 2
# 2 5
# 3 6
# 4 9
# 6 9
# 8 1
# 10 1
# 10 7
# 11 3
# 11 4
# That should be interpreted as:
#
# Maze Dimensions: 12 10
# Starting Position: 0 0
# Exit Position: 4 8
# List of boulder positions (if there are any): [1 2, 2 5, 3 6, ...]
# Corresponding to this maze:
#
# +------------+
# |A           |
# |        # # |
# | #          |
# |           #|
# |           #|
# |  #         |
# |   #        |
# |          # |
# |    B       |
# |    # #     |
# +------------+
#
# Another Maze:
#
# 4 3
# 0 0
# 3 2
# 2 0
# 2 2
#
# +----+
# |A # |
# |    |
# |  #B|
# +----+
#
# Question:
# Q1:
# Model the maze as a data structure, and write a function to print it similarly to how it is shown here.
# You may choose to read the maze in from a string, or just encode it directly.
