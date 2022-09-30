from tkinter import * # import all aspects of tkinter
import tkinter as tk # import tkinter module
from tkinter import ttk # import tkinter extension
import math # import math module
import random # import random module
import time # import time module

#Version 2:
# added selection of key values
# added validation of the entry of these values

#CONSTANTS
G = 6.67 * 10**-11 #Newton's gravitational constant
pi = 3.141592653

#GLOBAL VARIABLES
m1 = int(0) #mass of object 1
m2 = int(0) #mass of object 2
d = int(0) #distance between object 1 and object 2
o1_x = 0 #x and y values of objects 1 and 2 in the canvas
o2_x = 0
o1_y = 0
o2_y = 0

class Window(): #class of the main window where the simulation will run
    
    def __init__(self):
        self.initUI() #runs the initUI subroutine when the Window class is called
        
    def initUI(self): # initialises the main window
        global m1, m2, d, o1_x, o2_x, o1_y, o2_y # call the global variables to be used within the class
        
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
        m1Select.config(command = lambda : self.enterMass1(m1Select, m1StatusMsg)) # set the command of the button to the enterMass1 subroutine
        m1StatusMsg = tk.Label(main, text = ("The mass of object 1 is",m1,"kg."), font = ("Courier New", 11))# create message informing of the value of mass 1
        m1StatusMsg.place(x = 802, y = 82)
        
        m2Select = tk.Button(main, text = "Choose mass of object 2", relief = FLAT, bg = "#666", fg = "white")# create the button that allows the selection of mass 2
        m2Select.place(x = 806, y = 202)
        m2Select.config(command = lambda : self.enterMass2(m2Select, m2StatusMsg))# set the command of the button to the enterMass2 subroutine
        m2StatusMsg = tk.Label(main, text = ("The mass of object 2 is",m2,"kg."), font = ("Courier New", 11))# create message informing of the value of mass 2
        m2StatusMsg.place(x = 802, y = 172)
        
        dSelect = tk.Button(main, text = "Choose distance between objects", relief = FLAT, bg = "#666", fg = "white") #create the button that allows the selection of distance
        dSelect.place(x = 806, y = 292)
        dSelect.config(command = lambda : self.enterDist(dSelect, dStatusMsg))# set the command of the button to the enterDist subroutine
        dStatusMsg = tk.Label(main, text = ("The distance between the objects is",d,"m."), font = ("Courier New", 11))# create message informing of the value of the distance
        dStatusMsg.place(x = 802, y = 262)
        
        startButton = tk.Button(main, text = "START SIMULATION", relief = FLAT, fg = "white", bg = "green")# create the start simulaton button
        startButton.pack(side = LEFT, anchor = S, padx = 5, pady = 5)
        #startButton.config(command = ) # command subroutine yet to be created
        
        quitButton = tk.Button(main, text = "QUIT", relief = FLAT, fg = "white", bg = "red", command = quit) # create the quit button with the inbuilt command 'quit'
        quitButton.pack(side = RIGHT, anchor = S, padx = 5, pady = 5)
        
        main.mainloop()# essential part of tkinter - without this the window does not open
    
    
    def enterMass1(self, m1Select, m1StatusMsg): # subroutine that allows the selection of mass1
        global m1, m2, d, o1_x, o2_x, o1_y, o2_y # import the global variables
        
        enterMass1Window = Tk() # define the new window to enter mass1
        enterMass1Window.title("Enter Mass 1") # define the title of the new window
        enterMass1Window.geometry("200x100+300+300") # define the dimensions and position of the new window
        
        m1Confirm = tk.Button(enterMass1Window, text = "Confirm", relief = FLAT, bg = "white") # create the button that confirms the selection
        m1Confirm.pack(side = BOTTOM, pady = 10)
        m1Confirm.config(command = lambda : self.confirmMass1(m1Select, m1StatusMsg, m1Confirm, m1Entry, enterMass1Window))# set the command of the button to the confirmMass1 subroutine
        
        m1Entry = tk.Entry(enterMass1Window) # create the entry field for the user to type their value into
        m1Entry.pack(side = TOP, pady = 10)
    
    def confirmMass1(self, m1Select, m1StatusMsg, m1Confirm, m1Entry, enterMass1Window): #subroutine that confirms and changes the value of mass1
        global m1, m2, d, o1_x, o2_x, o1_y, o2_y # import the global variables
        
        correct = False # sets the correct variable to false
        while correct == False: # runs this loop only if correct = false
            try: # exception - tries to do this
                m1 = int(m1Entry.get()) # sets mass1 to the value that the user has typed
                correct = True # sets the correct variable to true, ending the loop
                enterMass1Window.destroy() # closes the new window
                break
            except: # if there is an error, then it runs this instead
                m1Error = tk.Label(enterMass1Window, text = "That value is not valid.", font = ("Courier New", 8), fg = "red") # creates an error message
                m1Error.place(x = 15, y = 35)
                correct = False # loop still continues
                break
        
        m1StatusMsg.config(text = ("The centre mass is",m1,"kg.")) # updates the status message
        
    def enterMass2(self, m2Select, m2StatusMsg): # subroutine that allows the selection of mass2
        global m1, m2, d, o1_x, o2_x, o1_y, o2_y # import the global variables
        
        enterMass2Window = Tk() # define the new window to enter mass2
        enterMass2Window.title("Enter Mass 2") # define the title of the new window
        enterMass2Window.geometry("200x100+300+300") # define the dimensions and position of the new window
        
        m2Confirm = tk.Button(enterMass2Window, text = "Confirm", relief = FLAT, bg = "white") # create the button that confirms the selection
        m2Confirm.pack(side = BOTTOM, pady = 10)
        m2Confirm.config(command = lambda : self.confirmMass2(m2Select, m2StatusMsg, m2Confirm, m2Entry, enterMass2Window)) # set the command of the button to the confirmMass2 subroutine
        
        m2Entry = tk.Entry(enterMass2Window) # create the entry field for the user to type their value into
        m2Entry.pack(side = TOP, pady = 10)
    
    def confirmMass2(self, m2Select, m2StatusMsg, m2Confirm, m2Entry, enterMass2Window): #subroutine that confirms and changes the value of mass2
        global m1, m2, d, o1_x, o2_x, o1_y, o2_y# import the global variables
        
        correct = False # sets the correct variable to false
        while correct == False: # runs this loop only if correct = false
            try:# exception - tries to do this
                m2 = int(m2Entry.get()) # sets mass2 to the value that the user has typed
                correct = True# sets the correct variable to true, ending the loop
                enterMass2Window.destroy() # closes the new window
                break
            except: # if there is an error, then it runs this instead
                m2Error = tk.Label(enterMass2Window, text = "That value is not valid.", font = ("Courier New", 8), fg = "red")  # creates an error message
                m2Error.place(x = 15, y = 35)
                correct = False # loop still continues
                break
        
        m2StatusMsg.config(text = ("The orbiting mass is",m2,"kg.")) # updates the status message
        
    def enterDist(self, dSelect, dStatusMsg): # subroutine that allows the selection of dist
        global m1, m2, d, o1_x, o2_x, o1_y, o2_y # import the global variables
        
        enterDistWindow = Tk()# define the new window to enter mass2
        enterDistWindow.title("Enter Distance")# define the title of the new window
        enterDistWindow.geometry("200x100+300+300")# define the dimensions and position of the new window
        
        dConfirm = tk.Button(enterDistWindow, text = "Confirm", relief = FLAT, bg = "white") # create the button that confirms the selection
        dConfirm.pack(side = BOTTOM, pady = 10)
        dConfirm.config(command = lambda : self.confirmDist(dSelect, dStatusMsg, dConfirm, dEntry, enterDistWindow))# set the command of the button to the confirmDist subroutine
        
        dEntry = tk.Entry(enterDistWindow) # create the entry field for the user to type their value into
        dEntry.pack(side = TOP, pady = 10)
        
    def confirmDist(self, dSelect, dStatusMsg, dConfirm, dEntry, enterDistWindow):#subroutine that confirms and changes the value of dist
        global m1, m2, d, o1_x, o2_x, o1_y, o2_y# import the global variables
        
        correct = False # sets the correct variable to false
        while correct == False:# runs this loop only if correct = false
            try:# exception - tries to do this
                d = int(dEntry.get())# sets dist to the value that the user has typed
                correct = True# sets the correct variable to true, ending the loop
                enterDistWindow.destroy()# closes the new window
                break
            except:# if there is an error, then it runs this instead
                dError = tk.Label(enterDistWindow, text = "That value is not valid.", font = ("Courier New", 8), fg = "red")# creates an error message
                dError.place(x = 15, y = 35)
                correct = False# loop still continues
                break
        
        dStatusMsg.config(text = ("The distance between the objects is",d,"m.")) # updates the status message
        
def Run(): # runs the program
    sim = Window()  # call the Window class which runs the simulation program

while __name__ == "__main__":# only runs the Run subroutine if this is ran from the main program and not from an imported module
    Run()