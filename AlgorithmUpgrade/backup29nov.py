import tkinter
from tkinter.constants import END
import turtle
import tkinter.messagebox
import math
import time

# create the window
window = tkinter.Tk()

sisi = 300
canvas_width = sisi
canvas_height = sisi
canvas = tkinter.Canvas(master=window, width=canvas_width, height=canvas_height)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10,
            columnspan=10)

commandscanvas = tkinter.Canvas(master = window, width = 200, height = 100)
commandscanvas.grid(padx=2, pady=2, row=3, column=12)

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
        self.shape()
        self.color('red')
        self.penup()
        self.speed(0)
        self.gold = 0
        # Create commands list
        # placeholder values only, for experimentation
        self.commands = []

    def forward(self):
        self.commands.append('f')
        print(self.commands)
        show_commands()

        # # Calculate spot to move to
        # direction = self.heading()
        # print(direction)
        # if (direction == 0):
        #     move_to_x = self.xcor() + 24
        #     move_to_y = self.ycor()
        # elif (direction == 90):
        #     move_to_x = self.xcor()
        #     move_to_y = self.ycor() + 24
        # elif (direction == 180):
        #     move_to_x = self.xcor() - 24
        #     move_to_y = self.ycor()
        # elif (direction == 270):
        #     move_to_x = self.xcor()
        #     move_to_y = self.ycor() - 24
        # elif (direction == 360):
        #     direction = 0
        #     move_to_x = self.xcor() + 24
        #     move_to_y = self.ycor()
        # else:
        #     print('direction is weird')

        # # Check if the space has a wall
        # if(move_to_x, move_to_y) not in walls:
        #     self.goto(move_to_x, move_to_y)
        # else:
        #     tkinter.messagebox.showinfo("Message", "U hit wall")

    def turn_left(self):
        self.commands.append('tl')
        # self.left(90)
        show_commands()

    def turn_right(self):
        self.commands.append('tr')
        # self.right(90)
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
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class CommandPen(turtle.RawTurtle):
    def __init__(self):
        turtle.RawTurtle.__init__(self, commandscanvas)
        self.shape('square')
        self.color('yellow')
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

# Add maze to mazes list
levels.append(level_1)
levels.append(level_2)
levels.append(level_3)
levels.append(level_4)
levels.append(level_5)
levels.append(level_6)
levels.append(level_7)
print(levels)

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
    commandpen.goto((-60,0))
    commandstext.delete('1.0',END)
    for x in range(len(player.commands)):
        commandstext.insert(
            '1.0', player.commands[len(player.commands)-x-1] + '\n')
    for i in range(len(player.commands)):
        cp_xcor = commandpen.xcor()
        cp_ycor = commandpen.ycor()

        if player.commands[i] == 'f':
            commandpen.frontstamp()
            commandpen.goto(cp_xcor + 24, cp_ycor)
            commandpen.stamp()
        elif player.commands[i] == 'tl':
            commandpen.leftstamp()
            commandpen.goto(cp_xcor + 24, cp_ycor)
            commandpen.stamp()
        elif player.commands[i] == 'tr':
            commandpen.rightstamp()
            commandpen.goto(cp_xcor + 24, cp_ycor)
            commandpen.stamp()

        # commandpen.color('white')
        
        
        
            


def execute_commands():
    for x in player.commands:
        if x == 'f':
            # Calculate spot to move to
            direction = player.heading()
            print(direction)
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
                print('direction is weird')

            # Check if the space has a wall
            if(move_to_x, move_to_y) not in walls:
                player.goto(move_to_x, move_to_y)
            else:
                tkinter.messagebox.showinfo("Message", "U hit wall")
        elif x == 'tl':
            player.left(90)
        elif x == 'tr':
            player.right(90)
        time.sleep(0.2)
    player.commands = []

def clear_commands():
    player.commands = []
    show_commands()

    commandpen.clear()
    commandpen.color('white')



def next_level():
    global current_level_idx, treasures
    if len(treasures) == 0:  # theres no treasure before the first level is created and after it is collected/destroyed
        print('current level idx', current_level_idx, 'len levels', len(levels))
        if current_level_idx < len(levels):
            print('current level idx now', current_level_idx)
        else:
            current_level_idx = 0
        setup_maze(levels[current_level_idx])
        current_level_idx += 1
        # clear commands
        clear_commands()


Play_Button = tkinter.Button(
    master=window, text="Play!", command=lambda: next_level())
Play_Button.config(bg="cyan", fg="black")
Play_Button.grid(padx=2, pady=2, row=0, column=11, sticky='nsew')

print('the current level main ', current_level_idx)

Board_Button = tkinter.Button(
    master=window, text="Next Level", command=lambda: next_level())
Board_Button.config(bg="cyan", fg="black")
Board_Button.grid(padx=2, pady=2, row=1, column=11, sticky='nsew')

Board_Button = tkinter.Button(
    master=window, text="Turn left", command=player.turn_left)
Board_Button.config(bg="blue", fg="black")
Board_Button.grid(padx=2, pady=2, row=2, column=11, sticky='nsew')

Board_Button = tkinter.Button(
    master=window, text="Turn right", command=player.turn_right)
Board_Button.config(bg="red", fg="black")
Board_Button.grid(padx=2, pady=2, row=2, column=13, sticky='nsew')

Board_Button = tkinter.Button(
    master=window, text="Forward", command=player.forward)
Board_Button.config(bg="yellow", fg="black")
Board_Button.grid(padx=2, pady=2, row=2, column=12, sticky='nsew')

Play_Button = tkinter.Button(master=window, text="Execute commands", command=lambda: execute_commands())
Play_Button.config(bg="green", fg="black")
Play_Button.grid(padx=2, pady=2, row=4, column=12, sticky='nsew')

Play_Button = tkinter.Button(master=window, text="Clear commands", command=lambda: clear_commands())
Play_Button.config(bg="orange", fg="black")
Play_Button.grid(padx=2, pady=2, row=4, column=13, sticky='nsew')

# Commands text, will be updated to commands canvas
commandstext = tkinter.Text(master=window, width = 20, height = 20)
commandstext.grid(padx=2, pady=2, row=3, column=14)




# Turn off screen updates
# window.tracer(0)

# Main Game Loop
while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            tkinter.messagebox.showinfo(
                "Message", "Congratulations")  # not neat
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            treasure.destroy()
            # len(treasures) will always be 1 after the first initiation of 'next level'
            treasures.remove(treasure)
            pen.clear()  # not neat
            commandpen.clear()
            walls = []  # not neat
            # turtle.Screen().bye()
    window.update()