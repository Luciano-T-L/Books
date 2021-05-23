# Unfinished

# Find some python program to read...


# Imports
from tkinter import *
import random
import time

# Input to difficulty level
level = int(input("Qual nível você gostaria de jogar? 1/2/3/4/5 \n"))
# variable that changes with the chosen level.
length = 500/level

# Variables for some tkinter functions and some values defined in tkinter pack)
root = Tk()
root.title("Ping Pong")
root.resizable(0,0)
root.wm_attributes("-topmost", -1)

# Telling the size of the game window.
canvas = Canvas(root, width=800, height=600, bd=0,highlightthickness=0)
canvas.pack()

root.update()

# Variável
count = 0
lost = False

# Creating class and some atributes
class Bola:
    def __init__(self, canvas, Barra, color):
        self.canvas = canvas
        self.Barra = Barra
        # He is using canvas to give some atributes for the class Bola
        self.id = canvas.create_oval(0, 0, 15, 15, fill=color)
        self.canvas.move(self.id, 245, 200)
        
        # Where the boll will be in te windows when the game starts (randomvalue)
        starts_x = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts_x)

        self.x = starts_x[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    # Really don't know what this class will do, but it describe the interaction
    # Between boll and bar.
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

# Some conditions, really don't undertanding how it's working
        if pos[1] <= 0:
            self.y = 3

        if pos[3] >= self.canvas_height:
            self.y = -3

        if pos[0] <= 0:
            self.x = 3
            
        if pos[2] >= self.canvas_width:
            self.x = -3

        self.Barra_pos = self.canvas.coords(self.Barra.id)


        if pos[2] >= self.Barra_pos[0] and pos[0] <= self.Barra_pos[2]:
            if pos[3] >= self.Barra_pos[1] and pos[3] <= self.Barra_pos[3]:
                self.y = -3
                global count
                count +=1
                score()


        if pos[3] <= self.canvas_height:
            self.canvas.after(10, self.draw)
        else:
            game_over()
            global lost
            lost = True

# Defining bar class, it's a rectangle, moves between two points
class Barra:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, length, 10, fill=color)
        self.canvas.move(self.id, 200, 400)

        self.x = 0

        self.canvas_width = self.canvas.winfo_width()

# Describing how to make the bar move with keyboard keys
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)
# Antoher draw fuctions, really don't know what it's doing.
# Something about the moviment of the bar, but really don't know what
    def draw(self):
        self.canvas.move(self.id, self.x, 0)

        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x = 0
        
        if self.pos[2] >= self.canvas_width:
            self.x = 0
        
        global lost
        
        if lost == False:
            self.canvas.after(10, self.draw)
# Defining parameters for the bar moviment
    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3

    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3

# Fuctions to start the game, calling the created classes 
def start_game(event):
    global lost, count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")

# calling functions, don't know what this "draws" fuctions does
    time.sleep(1)
    Barra.draw()
    Bola.draw()

# Creating function for scores
def score():
    canvas.itemconfig(score_now, text="Pontos: " + str(count))

# Creating function to end the game
def game_over():
    canvas.itemconfig(game, text="Game over!")

# Calling the classes
Barra = Barra(canvas, "orange")
Bola = Bola(canvas, Barra, "purple")

# This canvas things... but it's printing score informations
score_now = canvas.create_text(430, 20, text="Pontos: " + str(count), fill = "green", font=("Arial", 16))
# I didn't undertand this function, but a variable call this function!
game = canvas.create_text(400, 300, text=" ", fill="red", font=("Arial", 40))

# Canvas...
canvas.bind_all("<Button-1>", start_game)
# Probably to keep the game runing in loop.
root.mainloop()