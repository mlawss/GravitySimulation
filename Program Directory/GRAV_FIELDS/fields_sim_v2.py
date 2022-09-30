from tkinter import *
import tkinter as tk
from tkinter import ttk
import math
import random
import time

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

class Window():
    
    def __init__(self):
        self.initUI() 
        
    def initUI(self):
        global m1, m2, d, o1_x, o2_x, o1_y, o2_y
        
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
        m1Select.config(command = lambda : self.enterMass1(m1Select, m1StatusMsg))
        m1StatusMsg = tk.Label(main, text = ("The mass of object 1 is",m1,"kg."), font = ("Courier New", 11))
        m1StatusMsg.place(x = 802, y = 82)
        
        m2Select = tk.Button(main, text = "Choose mass of object 2", relief = FLAT, bg = "#666", fg = "white")
        m2Select.place(x = 806, y = 202)
        m2Select.config(command = lambda : self.enterMass2(m2Select, m2StatusMsg))
        m2StatusMsg = tk.Label(main, text = ("The mass of object 2 is",m2,"kg."), font = ("Courier New", 11))
        m2StatusMsg.place(x = 802, y = 172)
        
        dSelect = tk.Button(main, text = "Choose distance between objects", relief = FLAT, bg = "#666", fg = "white")
        dSelect.place(x = 806, y = 292)
        dSelect.config(command = lambda : self.enterDist(dSelect, dStatusMsg))
        dStatusMsg = tk.Label(main, text = ("The distance between the objects is",d,"m."), font = ("Courier New", 11))
        dStatusMsg.place(x = 802, y = 262)
        
        startButton = tk.Button(main, text = "START SIMULATION", relief = FLAT, fg = "white", bg = "green")
        startButton.pack(side = LEFT, anchor = S, padx = 5, pady = 5)
        #startButton.config(command = )
        
        quitButton = tk.Button(main, text = "QUIT", relief = FLAT, fg = "white", bg = "red", command = quit)
        quitButton.pack(side = RIGHT, anchor = S, padx = 5, pady = 5)
        
        main.mainloop()
    
    
    def enterMass1(self, m1Select, m1StatusMsg):
        global m1, m2, d, o1_x, o2_x, o1_y, o2_y
        
        enterMass1Window = Tk()
        enterMass1Window.title("Enter Mass 1")
        enterMass1Window.geometry("200x100+300+300")
        
        m1Confirm = tk.Button(enterMass1Window, text = "Confirm", relief = FLAT, bg = "white")
        m1Confirm.pack(side = BOTTOM, pady = 10)
        m1Confirm.config(command = lambda : self.confirmMass1(m1Select, m1StatusMsg, m1Confirm, m1Entry, enterMass1Window))
        
        m1Entry = tk.Entry(enterMass1Window)
        m1Entry.pack(side = TOP, pady = 10)
    
    def confirmMass1(self, m1Select, m1StatusMsg, m1Confirm, m1Entry, enterMass1Window):
        global m1, m2, d, o1_x, o2_x, o1_y, o2_y
        
        correct = False
        while correct == False:
            try:
                m1 = int(m1Entry.get())
                correct = True
                enterMass1Window.destroy()
                break
            except:
                m1Error = tk.Label(enterMass1Window, text = "That value is not valid.", font = ("Courier New", 8), fg = "red")
                m1Error.place(x = 15, y = 35)
                correct = False
                break
        
        m1StatusMsg.config(text = ("The centre mass is",m1,"kg."))
        
    def enterMass2(self, m2Select, m2StatusMsg):
        global m1, m2, d, o1_x, o2_x, o1_y, o2_y
        
        enterMass2Window = Tk()
        enterMass2Window.title("Enter Mass 2")
        enterMass2Window.geometry("200x100+300+300")
        
        m2Confirm = tk.Button(enterMass2Window, text = "Confirm", relief = FLAT, bg = "white")
        m2Confirm.pack(side = BOTTOM, pady = 10)
        m2Confirm.config(command = lambda : self.confirmMass2(m2Select, m2StatusMsg, m2Confirm, m2Entry, enterMass2Window))
        
        m2Entry = tk.Entry(enterMass2Window)
        m2Entry.pack(side = TOP, pady = 10)
    
    def confirmMass2(self, m2Select, m2StatusMsg, m2Confirm, m2Entry, enterMass2Window):
        global m1, m2, d, o1_x, o2_x, o1_y, o2_y
        
        correct = False
        while correct == False:
            try:
                m2 = int(m2Entry.get())
                correct = True
                enterMass2Window.destroy()
                break
            except:
                m2Error = tk.Label(enterMass2Window, text = "That value is not valid.", font = ("Courier New", 8), fg = "red")
                m2Error.place(x = 15, y = 35)
                correct = False
                break
        
        m2StatusMsg.config(text = ("The orbiting mass is",m2,"kg."))
        
    def enterDist(self, dSelect, dStatusMsg):
        global m1, m2, d, o1_x, o2_x, o1_y, o2_y
        
        enterDistWindow = Tk()
        enterDistWindow.title("Enter Distance")
        enterDistWindow.geometry("200x100+300+300")
        
        dConfirm = tk.Button(enterDistWindow, text = "Confirm", relief = FLAT, bg = "white")
        dConfirm.pack(side = BOTTOM, pady = 10)
        dConfirm.config(command = lambda : self.confirmDist(dSelect, dStatusMsg, dConfirm, dEntry, enterDistWindow))
        
        dEntry = tk.Entry(enterDistWindow)
        dEntry.pack(side = TOP, pady = 10)
        
    def confirmDist(self, dSelect, dStatusMsg, dConfirm, dEntry, enterDistWindow):
        global m1, m2, d, o1_x, o2_x, o1_y, o2_y
        
        correct = False
        while correct == False:
            try:
                d = int(dEntry.get())
                correct = True
                enterDistWindow.destroy()
                break
            except:
                dError = tk.Label(enterDistWindow, text = "That value is not valid.", font = ("Courier New", 8), fg = "red")
                dError.place(x = 15, y = 35)
                correct = False
                break
        
        dStatusMsg.config(text = ("The orbit radius is",d,"m."))
        
def Run():
    sim = Window()

while __name__ == "__main__":
    Run()