import turtle
import tkinter as tk


def do_stuff():
    for color in ["red", "yellow", "green"]:
        my_lovely_turtle.color(color)
        my_lovely_turtle.right(120)


if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root)
    canvas.config(width=600, height=200)
    canvas.pack(side=tk.LEFT)
    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("cyan")
    button = tk.Button(root, text="Press me", command=do_stuff)
    button.pack()
    my_lovely_turtle = turtle.RawTurtle(screen, shape="turtle")
    root.mainloop()
