# This file serves as a code line counter, so only the lines in the file that gives significance to the program is counted.

path1 = 'turtleMaze.py'
path2 = 'TkinterMaze.py'
file = open(path2, "r")
line_count = 0
for line in file:
    if (line != "\n") and ('#' not in line):
        line_count += 1
file.close()

print(line_count)
