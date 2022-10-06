import numpy as np
import math
import random as rnd
import subprocess
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

subprocess.call(["gcc","birds.c"]) #Compiling C
subprocess.call("./a.out") #Run C
x,y,phi,v=np.loadtxt('coordBirds.dat',unpack=True, usecols=(0,1,2,3)) #Load from C


rad=30

def init2D(r,g,b):
    glPointSize(3.0)
    glLoadIdentity()
    glClearColor(r,g,b,0.0)
    glMatrixMode (GL_PROJECTION)
    gluOrtho2D(0, 1000,0, 1000)


def detect(x,y,phi,j):
    x_temp=x[j]
    y_temp=y[j]
    sum_phi=0
    num=0
    for i in range(len(x)):
        if int(x[i]) in range(int(x_temp-rad),int(x_temp+rad)) and int(y[i]) in np.linspace(int(y_temp-rad),int(y_temp+rad)) :
            sum_phi+=phi[i]
            num+=1
        if num != 0 :
            phi2=sum_phi/num
        else :
            phi2=phi[j]
    if(phi2>360):
        phi2=phi2-360
    return phi2


def display():
    while(True):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(0.0, 0.0, 0.0)

        #draw points
        glBegin (GL_POINTS);
        for  i in range(len(x)) :
            if(x[i]>1000 or x[i]<0):
                phi[i]=180+phi[i]
            if(y[i]>1000 or y[i]<0):
                phi[i]=-phi[i]

            phi[i]=detect(x,y,phi,i)

            x[i]+=v[i]*math.cos(phi[i])
            y[i]+=v[i]*math.sin(phi[i])
            glVertex2f (x[i], y[i])


        glEnd ()
        glFlush()

glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (1000, 1000)
glutInitWindowPosition (0, 0)
glutCreateWindow ('Stormo di uccelli scemi')
init2D(0.6,0.8,1.0)
glutDisplayFunc(display)
glutMainLoop()
