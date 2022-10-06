import numpy as np
import math
from tkinter import *
import time
import random as rnd
import subprocess

cmd = "birds.c"

subprocess.call(["gcc",cmd]) #Compiling C
subprocess.call("./a.out") #Run C

gui = Tk()
gui.geometry("1000x1000")
gui.title("Pi Animation")
canvas = Canvas(gui, width=1000,height=1000,bg='white')
canvas.pack()

nBirds = 500
bird = []
vk = 1

Vx = [vk] * nBirds
Vy = [vk] * nBirds



x,y,phi=np.loadtxt('coordBirds.dat',unpack=True, usecols=(0,1,2)) #Load from C

#Creazione n uccelli con coordinate random in canvas
for i in range(nBirds):
    bird.append(canvas.create_oval(10,10,10,10, fill='black'))
    canvas.move(bird[i],x[i],y[i])
    Vx[i]= x[i]+vk*math.cos(phi[i])
    Vy[i]= y[i]+vk*math.sin(phi[i])

while True:
    for i in range(nBirds):

        pos=canvas.coords(bird[i])
        if(i==1):
            print(pos[2])
            print(pos[3])

        Vx[i]=vk*math.cos(phi[i])
        Vy[i]=vk*math.sin(phi[i])

        if(pos[2] > 1000 or pos[2] <0):
            Vx[i]=-Vx[i]
            Vy[i]=-Vy[i]
        if(pos[3] > 1000 or pos[1] <0):
            Vx[i]=-Vx[i]
            Vy[i]=-Vy[i]

        canvas.move(bird[i],Vx[i],Vy[i])

        gui.update()

gui.mainloop()
