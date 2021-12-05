path = 'tkinter-gui.py'
file = open(path, "r")
line_count = 0
for line in file:
    if (line != "\n") and not(line[0] == '#'):
        line_count += 1
file.close()

print(line_count)
