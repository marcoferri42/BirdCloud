from calendar import c
from cmath import log
from glob import glob
from lib2to3.pgen2.token import COMMENT
from operator import indexOf
import random
from xml.etree.ElementTree import Comment
import numpy as np
from math import cos, sin
from tkinter import *
import time

# xIncrement, yIncrement =np.loadtxt('coordBirds.dat',unpack=True, usecols=(0,1,2)) #Load from C
# subprocess.call(["gcc",cmd]) #Compiling C
# subprocess.call("./a.out") #Run C

# Varaibles
cmd = "birds.c"
nBirds = 1
displayedBirds = []
screenWidth = 800
screenHeight = 800
birdWidth = 5
birdHeight = 5
xIncrement = 4
yIncrement = 2
maxVel = xIncrement + yIncrement
initialX = screenWidth / 2
initialY = screenHeight / 2
x = initialX
y = initialY
# Setting up display
gui = Tk()
gui.geometry("800x800")
gui.title("BirdCloud")
canvas = Canvas(gui, width=screenWidth, height=screenHeight, bg="white")
canvas.pack()
frame = 0

# Changes direction
def incrementChange(param):
    global xIncrement, yIncrement
    if param == "x":
        xIncrement = -xIncrement
    else:
        yIncrement = -yIncrement


# Calculates new coordinates
def calculateCoords():
    global x, y, xIncrement, yIncrement
    x = abs(canvas.coords(displayedBirds[i])[0]) + xIncrement - 1
    y = abs(canvas.coords(displayedBirds[i])[1]) + yIncrement - 1

# Main loop
while True:
    # Frame loop
    for i in range(nBirds):
        if frame == 0:
            print("|----simulation-start----|")
            displayedBirds.append(
                canvas.create_rectangle(0, 0, birdWidth, birdHeight, fill="black")
            )
            canvas.moveto(displayedBirds[i], initialX, initialY)

            x = abs(canvas.coords(displayedBirds[i])[0])
            y = abs(canvas.coords(displayedBirds[i])[1])
            displayText = canvas.create_text(
                screenWidth / 2,
                12.5,
                font="Monospace 10 bold",
                text="x: "
                + str(x)
                + " y: "
                + str(y)
                + "    increments: "
                + str(xIncrement)
                + ","
                + str(yIncrement)
                + "  frame:"
                + str(frame),
            )

        # Border checking
        if x + xIncrement >= screenWidth or x + xIncrement <= 0:
            print("|----x-asxis-bordercollision----|")
            incrementChange("x")
            calculateCoords()

        if y + yIncrement >= screenHeight or y + yIncrement <= 0:
            print("|----y-axis-bordercollision----|")
            incrementChange("y")
            calculateCoords()
        else:
            calculateCoords()

        # Display of object w new coords
        canvas.moveto(displayedBirds[i], x, y)
        canvas.itemconfigure(
            displayText,
            text="x: "
            + str(x)
            + " y: "
            + str(y)
            + "    increments: "
            + str(xIncrement)
            + ","
            + str(yIncrement)
            + "  frame:"
            + str(frame),
        )

    frame = frame+1
    gui.update()
    time.sleep(0.001)
