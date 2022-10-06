import numpy as np
import math
from tkinter import *
import time

gui = Tk()
gui.geometry("1000x1000")
gui.title("Pi Animation")
canvas = Canvas(gui, width=1000,height=1000,bg='white')
canvas.pack()

nBirds = 500
bird = []
vk = 3
Vx = [vk] * nBirds
Vy = [vk] * nBirds

#Carico dati da C
x,y=np.loadtxt('coordBirds.dat',unpack=True, usecols=(0,1))

#Creazione n uccelli con coordinate random in canvas
for i in range(nBirds):
    bird.append(canvas.create_oval(10,10,10,10, fill='black'))
    canvas.move(bird[i],x[i],y[i])

while True:
    for i in range(nBirds):

        pos=canvas.coords(bird[i])

        if pos[3] >=1000 or pos[1] <=0:
            Vy[i] = -Vy[i]
        if pos[2] >=1000 or pos[0] <=0:
            Vx[i] = -Vx[i]

        canvas.move(bird[i],Vx[i],Vy[i])

        gui.update()

gui.mainloop()
