from tkinter import *
import tkinter as tk
from tkinter import ttk
import math
import random
import time

#Version 1:
# basic GUI set up.
# class for the main window.
# global variables for future values used in calculations and animation.

G = 6.67 * 10**-11 #Newton's gravitational constant
pi = 3.141592653

m1 = float(0) #mass of object 1
m2 = float(0) #mass of object 2
r = float(0) #distance between object 1 and object 2

#x and y values of objects 1 and 2 in the canvas
o1_x = 0
o2_x = 0
o1_y = 0
o2_y = 0

class Window(): #class of the main window where the simulation will run
    
    def __init__(self):
        self.initUI()
        
    def initUI(self):
        main = Tk()
        main.title("Gravitational Fields Simulation")
        main.geometry("1280x720")
        
        simFrame = tk.Canvas(main, relief = FLAT, width = 800, height = 720, bg = "black", borderwidth = 0)
        simFrame.pack(side = LEFT)
        
        welcomeMsg = tk.Label(main, text = "Welcome!", font = ("Courier New", 16))
        welcomeMsg.pack(anchor = N)
        infoMsgLine1 = tk.Label(main, text = "To begin, set the key values below", font = ("Courier New", 10))
        infoMsgLine1.pack(anchor = N)
        infoMsgLine2 = tk.Label(main, text = "and press the start simulation button.", font = ("Courier New", 10))
        infoMsgLine2.pack(anchor = N)
        
        m1Select = tk.Button(main, text = "Choose mass of object 1", relief = FLAT, bg = "#666", fg = "white")
        m1Select.place(x = 806, y = 112)
        #m1Select.config(command = )
        m1StatusMsg = tk.Label(main, text = ("The mass of object 1 is",m1,"kg."), font = ("Courier New", 11))
        m1StatusMsg.place(x = 802, y = 82)
        
        m2Select = tk.Button(main, text = "Choose mass of object 2", relief = FLAT, bg = "#666", fg = "white")
        m2Select.place(x = 806, y = 202)
        #m2Select.config(command = )
        m2StatusMsg = tk.Label(main, text = ("The mass of object 2 is",m2,"kg."), font = ("Courier New", 11))
        m2StatusMsg.place(x = 802, y = 172)
        
        rSelect = tk.Button(main, text = "Choose orbit radius", relief = FLAT, bg = "#666", fg = "white")
        rSelect.place(x = 806, y = 292)
        #rSelect.config(command = )
        rStatusMsg = tk.Label(main, text = ("The distance between the objects is",r,"m."), font = ("Courier New", 11))
        rStatusMsg.place(x = 802, y = 262)
        
        startButton = tk.Button(main, text = "START SIMULATION", relief = FLAT, fg = "white", bg = "green")
        startButton.pack(side = LEFT, anchor = S, padx = 5, pady = 5)
        #startButton.config(command = )
        
        quitButton = tk.Button(main, text = "QUIT", relief = FLAT, fg = "white", bg = "red", command = quit)
        quitButton.pack(side = RIGHT, anchor = S, padx = 5, pady = 5)
        
        main.mainloop()
        
def Run():
    sim = Window()

while __name__ == "__main__":
    Run()