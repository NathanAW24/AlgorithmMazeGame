import turtle
import math
import tkinter as tk

wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Maze Game')
wn.setup(700, 700)

# Create Pen


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed(0)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('blue')
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


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
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
levels = [""]

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
# Add treasures list
treasures = []


# Add maze to mazes list
levels.append(level_1)
levels.append(level_2)


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


# Create class instances
pen = Pen()
player = Player()

# Create wall coordinate list
walls = []

# Set up the level
setup_maze(levels[2])
# print(walls)

# Keyboard Binding
turtle.listen()
turtle.onkey(player.go_left, 'Left')
turtle.onkey(player.go_right, 'Right')
turtle.onkey(player.go_up, 'Up')
turtle.onkey(player.go_down, 'Down')

# Turn off screen updates
wn.tracer(0)

# Main Game Loop
while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)
            turtle.Screen().bye()
    wn.update()
