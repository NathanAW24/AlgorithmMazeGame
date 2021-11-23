import tkinter
import turtle
import tkinter.messagebox
import math

#create the window
window = tkinter.Tk()

canvas = tkinter.Canvas(master = window, width = 700, height = 700)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10) # , sticky='nsew')
#draw = turtle.Turtle()
# draw = turtle.RawTurtle(canvas)

# Create Pen
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

    def go_up(self):
        # Calculate spot to move to
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24

        # Check if the space has a wall
        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        # Calculate spot to move to
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24

        # Check if the space has a wall
        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        # Calculate spot to move to
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()

        # Check if the space has a wall
        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def check_left(self):
        # Calculate spot to move to
        check_x = self.xcor() - 24
        check_y = self.ycor()

        # Check if the space has a wall 
        if(check_x, check_y) in walls:
            # return True if there is a wall 
            return True
        return False

    def go_right(self):
        # Calculate spot to move to
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()

        # Check if the space has a wall
        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

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

# Create Levels List
levels = []

# Define First Level
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXX          XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "X       XX  XXX        XX",
    "XXXXXX  XX  XXX        XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",
    "X  XXX        XXXXT XXXXX",
    "X  XXX  XXXXXXXXXXXXXXXXX",
    "X         XXXXXXXXXXXXXXX",
    "X                XXXXXXXX",
    "XXXXXXXXXXXX     XXXXX  X",
    "XXXXXXXXXXXXXXX  XXXXX  X",
    "XXX  XXXXXXXXXX         X",
    "XXX                     X",
    "XXX         XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX              X",
    "XX   XXXXX              X",
    "XX   XXXXXXXXXXXXX  XXXXX",
    "XX     XXXXXXXXXXX  XXXXX",
    "XX          XXXX        X",
    "XXXX                    X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

level_2 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "X  XXXXXXX          XXXXX",
    "X  XXXXXXX  XXXXXX  XXXXX",
    "X       XX  XXXXXX  XXXXX",
    "X       XX  XXX        XX",
    "XXXXXX  XX  XXX        XX",
    "XXXXXX  XX  XXXXXX  XXXXX",
    "XXXXXX  XX    XXXX  XXXXX",
    "X PXXX        XXXX  XXXXX",
    "X TXXX  XXXXXXXXXXXXXXXXX",
    "X         XXXXXXXXXXXXXXX",
    "X                XXXXXXXX",
    "XXXXXXXXXXXX     XXXXX  X",
    "XXXXXXXXXXXXXXX  XXXXX  X",
    "XXX  XXXXXXXXXX         X",
    "XXX                     X",
    "XXX         XXXXXXXXXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXX",
    "XXXXXXXXXX              X",
    "XX   XXXXX              X",
    "XX   XXXXXXXXXXXXX  XXXXX",
    "XX     XXXXXXXXXXX  XXXXX",
    "XX          XXX         X",
    "XXXX                    X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

# Add maze to mazes list
levels.append(level_1)
levels.append(level_2)

# Add treasures list
treasures = []

# Create wall coordinate list
walls = []

# Create class instances
pen = Pen()
player = Player()   

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            # Get character at each x,y coordinate
            # Note the order of y and x in the next line
            character = level[y][x]

            # Calculate the screen x,y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # Check if it is an X (representing a wall)
            if character == 'X':
                pen.goto(screen_x, screen_y)
                pen.stamp()
                # Add coordinates to wall list
                walls.append((screen_x, screen_y))

            # Check player
            if character == 'P':
                player.goto(screen_x, screen_y)

            # Check treasure
            if character == 'T':
                treasures.append(Treasure(screen_x, screen_y))

current_level = 0
def next_level(current_level):
    print('current level', current_level, 'len levels', len(levels))
    if current_level+1 < len(levels):
        current_level += 1
        print('current level now', current_level)
    else:
        current_level = 0
    setup_maze(levels[current_level])

def Button_click ():
    tkinter.messagebox.showinfo("Game", "Maze Runners")

Play_Button = tkinter.Button(master = window, text ="Play!", command = Button_click)
Play_Button.config(bg="cyan",fg="black")
Play_Button.grid(padx=2, pady=2, row=0, column=11, sticky='nsew')

print('the current level main ', current_level)

Board_Button = tkinter.Button(master = window, text ="Next Level", command = next_level(current_level))
Board_Button.config(bg="cyan",fg="black")
Board_Button.grid(padx=2, pady=2, row=1, column=11, sticky='nsew')

Board_Button = tkinter.Button(master = window, text ="Go left", command = player.go_left)
Board_Button.config(bg="blue",fg="black")
Board_Button.grid(padx=2, pady=2, row=3, column=11, sticky='nsew')

Board_Button = tkinter.Button(master = window, text ="Go right", command = player.go_right)
Board_Button.config(bg="red",fg="black")
Board_Button.grid(padx=2, pady=2, row=3, column=13, sticky='nsew')

Board_Button = tkinter.Button(master = window, text ="Go up", command = player.go_up)
Board_Button.config(bg="yellow",fg="black")
Board_Button.grid(padx=2, pady=2, row=2, column=12, sticky='nsew')

Board_Button = tkinter.Button(master = window, text ="Go down", command = player.go_down)
Board_Button.config(bg="green",fg="black")
Board_Button.grid(padx=2, pady=2, row=4, column=12, sticky='nsew')



# Keyboard Binding
# turtle.listen()
turtle.onkey(player.go_left, 'Left')
turtle.onkey(player.go_right, 'Right')
turtle.onkey(player.go_up, 'Up')
turtle.onkey(player.go_down, 'Down')

# Turn off screen updates
# window.tracer(0)

# Main Game Loop
while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)
            turtle.Screen().bye()
    window.update()

