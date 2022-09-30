from tkinter import * # import all aspects of tkinter
import tkinter as tk # import tkintor module
from tkinter import ttk # import tkinter extension
import math # import math module
import random # import random module
import time # import time module

#Version 1:
# basic GUI set up.
# class for the main window.
# global variables for future values used in calculations and animation.

G = 6.67 * 10**-11 # Newton's gravitational constant
pi = 3.141592653

#x and y values of objects 1 and 2 in the canvas
o1_x = 0
o2_x = 0
o1_y = 0
o2_y = 0

m1 = float(0) #mass of object 1
m2 = float(0) #mass of object 2
r = float(0) #distance between object 1 and object 2

class Window(): #class of the main window where the simulation will run
    
    def __init__(self):
        self.initUI() # runs the initUI subroutine when the Window class is called
        
    def initUI(self): # initialises the main window
        global m1, m2, r # call the global variables to be used within the class
        
        main = Tk() # call the Tkinter function
        main.title("Gravitational Fields Simulation") # set the title of the window
        main.geometry("1280x720") # set the dimensions of the window
        
        simFrame = tk.Canvas(main, relief = FLAT, width = 800, height = 720, bg = "black", borderwidth = 0) # initialise the canvas that the sim will be run in
        simFrame.pack(side = LEFT) # place the canvas on the left
        
        welcomeMsg = tk.Label(main, text = "Welcome!", font = ("Courier New", 16)) # create a welcome message
        welcomeMsg.pack(anchor = N) # place the message at the top and to the right of the canvas
        infoMsgLine1 = tk.Label(main, text = "To begin, set the key values below", font = ("Courier New", 10)) # create line 1 of an info message
        infoMsgLine1.pack(anchor = N) # place the message at the top and to the right of the canvas
        infoMsgLine2 = tk.Label(main, text = "and press the start simulation button.", font = ("Courier New", 10)) # create line 2 of an info message
        infoMsgLine2.pack(anchor = N) # place the message at the top and to the right of the canvas
        
        m1Select = tk.Button(main, text = "Choose mass of object 1", relief = FLAT, bg = "#666", fg = "white") # create the button that allows the selection of mass 1
        m1Select.place(x = 806, y = 112)
        #m1Select.config(command = ) # command subroutine yet to be created
        m1StatusMsg = tk.Label(main, text = ("The mass of object 1 is",m1,"kg."), font = ("Courier New", 11)) # create message informing of the value of mass 1
        m1StatusMsg.place(x = 802, y = 82)
        
        m2Select = tk.Button(main, text = "Choose mass of object 2", relief = FLAT, bg = "#666", fg = "white") # create the button that allows the selection of mass 2
        m2Select.place(x = 806, y = 202)
        #m2Select.config(command = ) # command subroutine yet to be created
        m2StatusMsg = tk.Label(main, text = ("The mass of object 2 is",m2,"kg."), font = ("Courier New", 11)) # create message informing of the value of mass 2
        m2StatusMsg.place(x = 802, y = 172)
        
        rSelect = tk.Button(main, text = "Choose orbit radius", relief = FLAT, bg = "#666", fg = "white") # create the button that allows the selection of distance
        rSelect.place(x = 806, y = 292)
        #rSelect.config(command = ) # command subroutine yet to be created
        rStatusMsg = tk.Label(main, text = ("The distance between the objects is",r,"m."), font = ("Courier New", 11)) # create message informing of the value of distance
        rStatusMsg.place(x = 802, y = 262)
        
        startButton = tk.Button(main, text = "START SIMULATION", relief = FLAT, fg = "white", bg = "green") # create the start simulaton button
        startButton.pack(side = LEFT, anchor = S, padx = 5, pady = 5)
        #startButton.config(command = ) # command subroutine yet to be created
        
        quitButton = tk.Button(main, text = "QUIT", relief = FLAT, fg = "white", bg = "red", command = quit) # create the quit button with the inbuilt command 'quit'
        quitButton.pack(side = RIGHT, anchor = S, padx = 5, pady = 5)
        
        main.mainloop() # essential part of tkinter - without this the window does not open
        
def Run(): # runs the program
    sim = Window() # call the Window class which runs the simulation program

while __name__ == "__main__": # only runs the Run subroutine if this is ran from the main program and not from an imported module
    Run()