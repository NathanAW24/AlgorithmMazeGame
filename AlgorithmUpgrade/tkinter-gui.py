import tkinter
from tkinter import ttk
from tkinter.constants import END, X
import turtle
import math
import time

# create the window
window = tkinter.Tk()

sisi = 300
canvas_width = sisi
canvas_height = sisi
canvas = tkinter.Canvas(
    master=window, width=canvas_width, height=canvas_height)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10,
            columnspan=10)

commandscanvas = tkinter.Canvas(master=window, width=sisi, height=100)
commandscanvas.grid(padx=2, pady=2, row=15, column=0,
                    rowspan=10, columnspan=10)


class Pen(turtle.RawTurtle):
    def __init__(self):
        turtle.RawTurtle.__init__(self, canvas)
        self.shape('square')
        self.color('blue')
        self.penup()
        self.speed(0)


class Player(turtle.RawTurtle):
    def __init__(self):
        turtle.RawTurtle.__init__(self, canvas)
        self.shape('turtle')
        self.color('red')
        self.penup()
        self.speed(0)
        # Create commands list
        # placeholder values only, for experimentation
        self.commands = []
        # test_commands = ['sl','f  ','f','f','tl','el','f']

    def forward(self):
        self.commands.append('f')
        # print(self.commands)  # comment this later
        show_commands()

    def turn_left(self):
        self.commands.append('tl')
        # self.left(90)
        # print(self.commands)
        show_commands()

    def turn_right(self):
        self.commands.append('tr')
        # self.right(90)
        # print(self.commands)
        show_commands()

    def start_loop(self):
        # n is the number of times you want to loop
        self.commands.append('sl')
        # print(self.commands)
        show_commands()

    def end_loop(self):
        self.commands.append('el')
        # print(self.commands)
        show_commands()

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a**2) + (b**2))

        if distance < 5:
            return True
        else:
            return False


class Treasure(turtle.RawTurtle):
    def __init__(self, x, y):
        turtle.RawTurtle.__init__(self, canvas)
        self.shape('circle')
        self.color('gold')
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        # self.goto(2000, 2000)
        self.hideturtle()


class CommandPen(turtle.RawTurtle):
    def __init__(self):
        turtle.RawTurtle.__init__(self, commandscanvas)
        self.shape('triangle')
        self.color('white')
        self.penup()
        self.speed(0)

    def frontstamp(self):
        self.shape('triangle')
        self.color('yellow')
        self.setheading(90)

    def leftstamp(self):
        self.shape('triangle')
        self.color('blue')
        self.setheading(180)

    def rightstamp(self):
        self.shape('triangle')
        self.color('red')
        self.setheading(0)

    def startloopstamp(self):
        self.shape('arrow')
        self.color('black')
        self.setheading(180)

    def endloopsstamp(self):
        self.shape('arrow')
        self.color('black')
        self.setheading(0)

    def newline(self):
        self.goto(-130, self.ycor()-24)


# Create Levels List
levels = []

# Define First Level
level_1 = [
    "00000",
    "0P T0",
    "00000"
]

level_2 = [
    "00000",
    "000T0",
    "000 0",
    "0P  0",
    "00000"
]

level_3 = [
    "00000",
    "0P  0",
    "000 0",
    "000T0",
    "00000"
]

level_4 = [
    "0000000",
    "000  T0",
    "000 000",
    "0P  000",
    "0000000"
]

level_5 = [
    "0000000",
    "0P  000",
    "000 000",
    "000  T0",
    "0000000"
]

level_6 = [
    "0000000",
    "0P    0",
    "00000 0",
    "0T    0",
    "0000000"
]

level_7 = [
    "0000000",
    "0T    0",
    "00000 0",
    "0P    0",
    "0000000"
]

level_8 = [
    "0000000",
    "0T    0",
    "00000 0",
    "0     0",
    "0 00000",
    "0    P0",
    "0000000"
]

level_9 = [
    "0000000",
    "0    T0",
    "0 00000",
    "0     0",
    "00000 0",
    "0P    0",
    "0000000"
]

level_10 = [
    "000000000",
    "0P0   0T0",
    "0 0 0 0 0",
    "0 0 0 0 0",
    "0 0 0 0 0",
    "0   0   0",
    "000000000"
]

level_11 = [
    "000000000",
    "0   0   0",
    "0 0 0 0 0",
    "0 0 0 0 0",
    "0 0 0 0 0",
    "0P0   0T0",
    "000000000"
]

level_12 = [
    "000000",
    "0000T0",
    "0000 0",
    "0000 0",
    "0P   0",
    "000000",
]

level_13 = [
    "000000",
    "0T0000",
    "0 0000",
    "0 0000",
    "0   P0",
    "000000",
]

level_14 = [
    "000000",
    "000T 0",
    "0000 0",
    "0000 0",
    "0P   0",
    "000000",
]

level_15 = [
    "000000",
    "0 T000",
    "0 0000",
    "0 0000",
    "0   P0",
    "000000",
]

level_16 = [
    "000000",
    "0P0T 0",
    "0 00 0",
    "0 00 0",
    "0    0",
    "000000",
]

level_17 = [
    "000000",
    "0 T0P0",
    "0 00 0",
    "0 00 0",
    "0    0",
    "000000",
]

win_level = [
    "0 0      ",
    "0 0      ",
    "000      ",
    "         ",
    "0 0 0    ",
    "0 0   000",
    "000 0 0 0",
    "0 0 0 0 0"
]

# Add maze to mazes list
levels.append(level_1)
levels.append(level_2)
levels.append(level_3)
levels.append(level_4)
levels.append(level_5)
levels.append(level_6)
levels.append(level_7)
levels.append(level_8)
levels.append(level_9)
levels.append(level_10)
levels.append(level_11)
levels.append(level_12)
levels.append(level_13)
levels.append(level_14)
levels.append(level_15)
levels.append(level_16)
levels.append(level_17)
levels.append(win_level)

# Add treasures list
treasures = []

# Create wall coordinate list
walls = []

# Create class instances
pen = Pen()
player = Player()
commandpen = CommandPen()


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            # Get character at each x,y coordinate
            # Note the order of y and x in the next line
            character = level[y][x]

            # Calculate the screen x,y coordinates
            screen_x = -(canvas_width * 0.25) + (x * 24)

            screen_y = (canvas_height*0.25) - (y * 24)

            # Check if it is an 0 (representing a wall)
            if character == '0':
                pen.goto(screen_x, screen_y)
                pen.stamp()
                # Add coordinates to wall list
                walls.append((screen_x, screen_y))

            # Check player
            if character == 'P':
                player.goto(screen_x, screen_y)
                player.setheading(0)

            # Check treasure
            if character == 'T':
                treasures.append(Treasure(screen_x, screen_y))


current_level_idx = 0


def show_commands():
    commandpen.goto((-130, 30))

    for i in range(len(player.commands)):
        if commandpen.xcor() > 70:
            commandpen.newline()

        if player.commands[i] == 'f':
            commandpen.frontstamp()
            commandpen.goto(commandpen.xcor() + 24, commandpen.ycor())
            commandpen.stamp()
        elif player.commands[i] == 'tl':
            commandpen.leftstamp()
            commandpen.goto(commandpen.xcor() + 24, commandpen.ycor())
            commandpen.stamp()
        elif player.commands[i] == 'tr':
            commandpen.rightstamp()
            commandpen.goto(commandpen.xcor() + 24, commandpen.ycor())
            commandpen.stamp()
        elif player.commands[i] == 'sl':
            commandpen.startloopstamp()
            commandpen.goto(commandpen.xcor() + 24, commandpen.ycor())
            commandpen.stamp()
        elif player.commands[i] == 'el':
            commandpen.endloopsstamp()
            commandpen.goto(commandpen.xcor() + 24, commandpen.ycor())
            commandpen.stamp()


def loop_func(sl_idx, el_idx):
    loop_ls = [player.commands[i] for i in range(sl_idx+1, el_idx)]
    # length_loop = len(loop_ls)
    # update_ls = loop_ls[:]

    # for x in loop_ls:
    #     update_ls.append(x)
    #     # print(update_ls)

    for x in loop_ls:
        if x == 'f':
            # Calculate spot to move to
            direction = player.heading()
            # print(direction)
            if (direction == 0):
                move_to_x = player.xcor() + 24
                move_to_y = player.ycor()
            elif (direction == 90):
                move_to_x = player.xcor()
                move_to_y = player.ycor() + 24
            elif (direction == 180):
                move_to_x = player.xcor() - 24
                move_to_y = player.ycor()
            elif (direction == 270):
                move_to_x = player.xcor()
                move_to_y = player.ycor() - 24
            elif (direction == 360):
                direction = 0
                move_to_x = player.xcor() + 24
                move_to_y = player.ycor()
            else:
                # print('direction is weird')
                pass
                # Check if the space has a wall
            if(move_to_x, move_to_y) not in walls:
                player.goto(move_to_x, move_to_y)
            else:
                tkinter.messagebox.showinfo("You died", "Cause of Death: You faceplanted into a wall.")
                # repeat
                break
        elif x == 'tl':
            player.left(90)
        elif x == 'tr':
            player.right(90)
        time.sleep(0.2)
    pass


def execute_commands():
    global treasures
    flag = 0
    for x in player.commands:
        if x == 'f':
            # Calculate spot to move to
            direction = player.heading()
            # print(direction)
            if (direction == 0):
                move_to_x = player.xcor() + 24
                move_to_y = player.ycor()
            elif (direction == 90):
                move_to_x = player.xcor()
                move_to_y = player.ycor() + 24
            elif (direction == 180):
                move_to_x = player.xcor() - 24
                move_to_y = player.ycor()
            elif (direction == 270):
                move_to_x = player.xcor()
                move_to_y = player.ycor() - 24
            elif (direction == 360):
                direction = 0
                move_to_x = player.xcor() + 24
                move_to_y = player.ycor()
            else:
                # print('direction is weird')
                pass
                # Check if the space has a wall
            if(move_to_x, move_to_y) not in walls:
                player.goto(move_to_x, move_to_y)
            else:
                tkinter.messagebox.showinfo("You died", "Cause of Death: You faceplanted into a wall.")
                flag = 1
                # repeat
                repeat_maze()
                break
        elif x == 'tl':
            player.left(90)
        elif x == 'tr':
            player.right(90)
        elif x == 'sl':
            try:
                sl_idx = player.commands.index(x)
                el_idx = player.commands.index('el')
                loop_func(sl_idx, el_idx)
            except:
                pass
                # tkinter.messagebox.showinfo("Message", "you forgot end_loop")
                # repeat_maze()

        time.sleep(0.2)

    # if doesnt reach the end --> show u fail, and repeat ok
    if flag == 0:
        for treasure in treasures:
            if not player.is_collision(treasure):
                tkinter.messagebox.showinfo("You died", "Cause of Death: You didn't get to the end of the maze")
                repeat_maze()

    player.commands = []


def clear_commands():
    player.commands = []
    show_commands()

    commandpen.clear()
    commandpen.color('white')


def repeat_maze():
    global current_level_idx, treasures, walls
    for treasure in treasures:
        treasure.destroy()
        # len(treasures) will always be 1 after the first initiation of 'next level'
        treasures.remove(treasure)
        pen.clear()  # not neat
        walls = []  # not neat
        setup_maze(levels[current_level_idx-1])
    clear_commands()
    pass


def next_level():
    global current_level_idx, treasures
    if len(treasures) == 0:
        # theres no treasure before the first level is created and after it is collected/destroyed
        # print('current level idx', current_level_idx, 'len levels', len(levels))
        if current_level_idx < len(levels):
            pass
            # print('current level idx now', current_level_idx)
        else:
            current_level_idx = 0
        setup_maze(levels[current_level_idx])
        current_level_idx += 1
        # clear commands
        clear_commands()
        # player.commands = ['sl', 'f', 'f', 'f',
        #                    'tl', 'el', 'f']  # COMMENT THIS LATER


Play_Button = tkinter.Button(
    master=window, text="Play!", command=lambda: next_level())
Play_Button.config(bg="cyan", fg="black")
Play_Button.grid(padx=2, pady=2, row=11, column=1, sticky='nsew')

# print('the current level main ', current_level_idx)

Board_Button = tkinter.Button(
    master=window, text="Turn left", command=player.turn_left)
Board_Button.config(bg="blue", fg="black", width=15)
Board_Button.grid(padx=2, pady=2, row=12, column=0, sticky='nsew')

Board_Button = tkinter.Button(
    master=window, text="Forward", command=player.forward)
Board_Button.config(bg="yellow", fg="black")
Board_Button.grid(padx=2, pady=2, row=12, column=1, sticky='nsew')

Board_Button = tkinter.Button(
    master=window, text="Turn right", command=player.turn_right)
Board_Button.config(bg="red", fg="black")
Board_Button.grid(padx=2, pady=2, row=12, column=2, sticky='nsew')

Start_Loop_Button = tkinter.Button(
    master=window, text="Start Loop", command=player.start_loop)
Start_Loop_Button.config(bg="white", fg="black")
Start_Loop_Button.grid(padx=2, pady=2, row=13,
                       column=0, sticky='nsew')

End_Loop_Button = tkinter.Button(
    master=window, text="End Loop", command=player.end_loop)
End_Loop_Button.config(bg="white", fg="black")
End_Loop_Button.grid(padx=2, pady=2, row=13, column=1, sticky='nsew')

Execute_Button = tkinter.Button(
    master=window, text="Execute commands", command=lambda: execute_commands())
Execute_Button.config(bg="green", fg="white")
Execute_Button.grid(padx=2, pady=2, row=14, column=1, sticky='nsew')

Clear_Button = tkinter.Button(
    master=window, text="Clear commands", command=lambda: clear_commands())
Clear_Button.config(bg="orange", fg="black")
Clear_Button.grid(padx=2, pady=10, row=14, column=2, sticky='nsew')

# Turn off screen updates
# window.tracer(0)

# Main Game Loop
while True:
    try:
        for treasure in treasures:
            if player.is_collision(treasure):
                tkinter.messagebox.showinfo(
                    "You beat the level!", "Congratulations! Time for the next level")  # not neat
                treasure.destroy()
                # len(treasures) will always be 1 after the first initiation of 'next level'
                treasures.remove(treasure)
                pen.clear()  # not neat
                commandpen.clear()
                walls = []  # not neat
                next_level()
                # turtle.Screen().bye()
        window.update()
    except:
        pass
