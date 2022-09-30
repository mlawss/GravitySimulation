from tkinter import * # import modules
import tkinter as tk
from tkinter import ttk
import math
import random
import time

#Version 4:
# added calculation subroutines for different values
# changed/added some global variables to suit the needs of these calculations

#CONSTANTS
G = 6.67 * 10**-11 # Newton's gravitational constant
PI = 3.141592653

#GLOBAL VARIABLES
m1 = int(2) # mass of object 1
m2 = int(1) # mass of object 2
d = int(50) # distance between object 1 and object 2
d0 = int(50) # initial distance between each object [for calculations of velocity etc]

class Window(): #class of the main window where the simulation will run
    
    def __init__(self):
        self.initUI() #runs the initUI subroutine when the Window class is called
        
    def initUI(self): # initialises the main window
        global m1, m2, d  # call the global variables to be used within the class
        
        main = Tk() # call the Tkinter function
        main.title("Gravitational Fields Simulation") # set the title of the window
        main.geometry("1280x720") # set the dimensions of the window
        
        simFrame = tk.Canvas(main, relief = FLAT, width = 800, height = 720, bg = "black", borderwidth = 0) # initialise the canvas that the sim will be run in
        simFrame.pack(side = LEFT, fill = BOTH) # place the canvas on the left
        
        welcomeMsg = tk.Label(main, text = "Welcome!", font = ("Courier New", 16)) # create a welcome message
        welcomeMsg.pack(anchor = N) # place the message at the top and to the right of the canvas
        infoMsgLine1 = tk.Label(main, text = "To begin, set the key values below", font = ("Courier New", 10)) # create line 1 of an info message
        infoMsgLine1.pack(anchor = N) # place the message at the top and to the right of the canvas
        infoMsgLine2 = tk.Label(main, text = "and press the start simulation button.", font = ("Courier New", 10)) # create line 2 of an info message
        infoMsgLine2.pack(anchor = N)# place the message at the top and to the right of the canvas
        scaleInfo1 = tk.Label(main, text = "1 PIXEL = 1 METRE. VALUES HIGHER THAN ~600M WILL BE OUT OF RANGE.", font = ("Dotum", 9), fg = "red")
        scaleInfo1.place(x = 805, y = 322)
        scaleInfo2 = tk.Label(main, text = "SIMILARLY, 1 KG = 5 PIXELS WIDE. VALUES HIGHER THAN ~50KG WILL BE", font = ("Dotum", 9), fg = "red")
        scaleInfo2.place(x = 805, y = 352)
        scaleInfo3 = tk.Label(main, text = "OUT OF RANGE.", font = ("Dotum", 9), fg = "red")
        scaleInfo3.place(x = 805, y = 372)
        #messages to inform the user of the scale.
        
        m1Select = tk.Button(main, text = "Choose mass of object 1", relief = FLAT, bg = "#666", fg = "white")
         # create the button that allows the selection of mass 1
        m1Select.place(x = 806, y = 112)
        m1Select.config(command = lambda : self.enterMass1(m1Select, m1StatusMsg)) # set the command of the button to the enterMass1 subroutine
        m1StatusMsg = tk.Label(main, text = ("The mass of object 1 is",m1,"kg."), font = ("Courier New", 11))# create message informing of the value of mass 1
        m1StatusMsg.place(x = 802, y = 82)
        
        m2Select = tk.Button(main, text = "Choose mass of object 2", relief = FLAT, bg = "#666", fg = "white")
        # create the button that allows the selection of mass 2
        m2Select.place(x = 806, y = 202)
        m2Select.config(command = lambda : self.enterMass2(m2Select, m2StatusMsg))# set the command of the button to the enterMass2 suroutine
        m2StatusMsg = tk.Label(main, text = ("The mass of object 2 is",m2,"kg."), font = ("Courier New", 11))# create message informing of the value of mass 2
        m2StatusMsg.place(x = 802, y = 172)
        
        dSelect = tk.Button(main, text = "Choose distance between objects", relief = FLAT, bg = "#666", fg = "white")
        # create the button that allows the selection of distance
        dSelect.place(x = 806, y = 292)
        dSelect.config(command = lambda : self.enterDist(dSelect, dStatusMsg))# set the command of the button to the enterDist subroutine
        dStatusMsg = tk.Label(main, text = ("The distance between the objects is",d,"m."), font = ("Courier New", 11))# create status message for distance
        dStatusMsg.place(x = 802, y = 262)
        
        startButton = tk.Button(main, text = "START SIMULATION", relief = FLAT, fg = "white", bg = "green")# create the start simulaton button
        startButton.pack(side = LEFT, anchor = S, padx = 5, pady = 5)
        startButton.config(command = lambda : self.runSim(m1Select, m2Select, dSelect, startButton, simFrame, main))# set the command to the runSim subroutine
        
        quitButton = tk.Button(main, text = "QUIT", relief = FLAT, fg = "white", bg = "red", command = quit)# create the quit button
        quitButton.pack(side = RIGHT, anchor = S, padx = 5, pady = 5)
        
        main.mainloop()# essential part of tkinter - without this the window does not open
    
    
    def enterMass1(self, m1Select, m1StatusMsg): # subroutine that allows the selection of mass1
        global m1# import the global variables
        
        enterMass1Window = Tk() # define the new window to enter mass1
        enterMass1Window.title("Enter Mass 1") # define the title of the new window
        enterMass1Window.geometry("200x100+300+300") # define the dimensions and position of the new window
        
        m1Confirm = tk.Button(enterMass1Window, text = "Confirm", relief = FLAT, bg = "white") # create the button that confirms the selection
        m1Confirm.pack(side = BOTTOM, pady = 10)
        m1Confirm.config(command = lambda : self.confirmMass1(m1Select, m1StatusMsg, m1Confirm, m1Entry, enterMass1Window))
        # set the command of the button to the confirmMass1 subroutine
        
        m1Entry = tk.Entry(enterMass1Window)# create the entry field for the user to type their value into
        m1Entry.pack(side = TOP, pady = 10)
    
    def confirmMass1(self, m1Select, m1StatusMsg, m1Confirm, m1Entry, enterMass1Window): #subroutine that confirms and changes the value of mass1
        global m1# import the global variables
        
        correct = False # sets the correct variable to false
        while correct == False: # runs this loop only if correct = false
            try: # exception - tries to do this
                m1 = int(m1Entry.get()) # sets mass1 to the value that the user has typed
                correct = True# sets the correct variable to true, ending the loop
                enterMass1Window.destroy() # closes the new window
                break
            except: # if there is an error, then it runs this instead
                m1Error = tk.Label(enterMass1Window, text = "That value is not valid.", font = ("Courier New", 8), fg = "red") # creates an error message
                m1Error.place(x = 15, y = 35)
                correct = False # loop still continues
                break
        
        m1StatusMsg.config(text = ("The mass of object 1 is",m1,"kg.")) # updates the status message
        
    def enterMass2(self, m2Select, m2StatusMsg): #subroutine that confirms and changes the value of mass2
        global m2# import the global variables
        
        enterMass2Window = Tk() # define the new window to enter mass2
        enterMass2Window.title("Enter Mass 2") # define the title of the new window
        enterMass2Window.geometry("200x100+300+300") # define the dimensions and position of the new window
        
        m2Confirm = tk.Button(enterMass2Window, text = "Confirm", relief = FLAT, bg = "white") # create the button that confirms the selection
        m2Confirm.pack(side = BOTTOM, pady = 10)
        m2Confirm.config(command = lambda : self.confirmMass2(m2Select, m2StatusMsg, m2Confirm, m2Entry, enterMass2Window)) # set the command of the button to the confirmMass2 subroutine
        
        m2Entry = tk.Entry(enterMass2Window) # create the entry field for the user to type their value into
        m2Entry.pack(side = TOP, pady = 10)
    
    def confirmMass2(self, m2Select, m2StatusMsg, m2Confirm, m2Entry, enterMass2Window): #subroutine that confirms and changes the value of mass2
        global m2# import the global variables
        
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
        global d # import the global variables
        
        enterDistWindow = Tk()# define the new window to enter mass2
        enterDistWindow.title("Enter Distance")# define the title of the new window
        enterDistWindow.geometry("200x100+300+300")# define the dimensions and position of the new window
        
        dConfirm = tk.Button(enterDistWindow, text = "Confirm", relief = FLAT, bg = "white") # create the button that confirms the selection
        dConfirm.pack(side = BOTTOM, pady = 10)
        dConfirm.config(command = lambda : self.confirmDist(dSelect, dStatusMsg, dConfirm, dEntry, enterDistWindow))# set the command of the button to the confirmDist subroutine
        
        dEntry = tk.Entry(enterDistWindow) # create the entry field for the user to type their value into
        dEntry.pack(side = TOP, pady = 10)
        
    def confirmDist(self, dSelect, dStatusMsg, dConfirm, dEntry, enterDistWindow):#subroutine that confirms and changes the value of dist
        global d # import the global variables
        
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
        
    class Object(): # class of the object - creates instances of objects using OOP
        
        def __init__(self, mass, dist, simFrame): # init method
            self.mass = mass # creates the mass variable
            self.dist = dist # creates the dist variable
            self.initObject(mass, dist, simFrame)# runs the initObject method
            
        def initObject(self, mass, dist, simFrame):# intialises the object based on parameters
            global m1, m2, d
            
            xpos_1 = 400 - (d/2) # x position of obj 1 - the distance is taken away so that it is to the left
            ypos_1 = 360 # y position of obj 1
            xpos_2 = 400 + (d/2) # x position of obj 2 - distance is added so that it is to the right
            ypos_2 = 360 # y position of obj 2
            
            if mass == m1: # checks if the mass is equal to object 1's mass
                xradius = xpos_1 - mass*5 # set the size of the circle
                yradius = ypos_1 - mass*5
                
                obj = simFrame.create_oval(xpos_1, ypos_1, xradius, yradius, fill = "white") # initialises the object under obj variable
                return obj# returns the object
            
            elif mass == m2: # checks if the mass is equal object 2's mass
                xradius = xpos_2 - mass*5 # set the size of the cirlce
                yradius = ypos_2 - mass*5
                
                obj = simFrame.create_oval(xpos_2, ypos_2, xradius, yradius, fill = "white")# initialises the object under obj variable
                return obj# returns the object
            
            else:
                print("Something went very wrong. Mass not found for object created.") # validation just in case...
            
        def calcGravForce(self, simFrame): # calculation of the gravitational force
            global m1, m2, d
            
            f = (G * m1 * m2) / (d**2)
            
            return f # returns the value as a variable
        
        def calcGravPotential(self, simFrame): # calculation of the gravitational potential
            global m1, m2, d
            
            if m1 >= m2: # if statements to check if the mass of obj1 is > obj2 and if so it calculates the gpe of obj2 and vice versa.
                gpe = (G * m1) / d
                return gpe # returns the value as a variable
                
            elif m1 < m2:
                gpe = (G * m2) / d
                return gpe # returns the value as a variable
        
        def calcGravFieldStrength(self, simFrame): # calc of grav field strength, can also be acceleration towards the other object in m/s^2
            global m1, m2, d
            
            if m1 >= m2:
                gl = (G * m1) / (d**2) # field acting on / acceleration of smaller object
                gs = (G * m2) / (d**2) # field acting on / acceleration of larger object
                
                return gl, gs # returns the value as a variable
                
            elif m1 < m2:
                gl = (G * m2) / (d**2) # field acting on / acceleration of smaller object
                gs = (G * m1) / (d**2) # field acting on / acceleration of larger object
                
                return gl, gs # returns the value as a variable
            
        def calcVelocity(self, gl, gs, simFrame): # calc of velocity
            global m1, m2, d, d0
            
            if d0 - d <= 0: # if distance is greater than original distance
                if m1 >= m2:
                    vel_obj1 = math.sqrt(2 * (d - d0) * (gs)) # v^2 = u^2 + 2as where u = 0 as the objects are initially stationary
                    vel_obj2 = math.sqrt(2 * (d - d0) * (gl)) # therefore v = sqrt(2as) where v is velocity, a is acceleration and s is distance travelled
                    return vel_obj1, vel_obj2 # returns the value as a variable
                
                elif m1 < m2:
                    vel_obj1 = math.sqrt(2 * (d - d0) * (gl))
                    vel_obj2 = math.sqrt(2 * (d - d0) * (gs))
                    return vel_obj1, vel_obj2 # returns the value as a variable
                
            elif d0 - d > 0: # if distance is less than original distance
                if m1 >= m2:
                    vel_obj1 = math.sqrt(2 * (d0 - d) * (gs))
                    vel_obj2 = math.sqrt(2 * (d0 - d) * (gl))
                    return vel_obj1, vel_obj2 # returns the value as a variable
                
                elif m1 < m2:
                    vel_obj1 = math.sqrt(2 * (d0 - d) * (gl))
                    vel_obj2 = math.sqrt(2 * (d0 - d) * (gs))
                    return vel_obj1, vel_obj2 # returns the value as a variable
            
        def calcKineticEnergy(self, vel_obj1, vel_obj2, simFrame): # calculation of kinetic energy
            global m1, m2, d
            
            ke_obj1 = (1/2) * m1 * (vel_obj1 ** 2) # KE = 1/2(m)(v^2)
            ke_obj2 = (1/2) * m2 * (vel_obj2 ** 2)
            
            return ke_obj1, ke_obj2 # returns the value as a variable
            
    
    def Update(self, simFrame): # method which will run in a loop for each frame
        global m1, m2, d # import global variables
        
        simFrame.delete("all") # deletes all objects on the canvas
        
        Object1 = self.Object(m1, d, simFrame) # creates an object instance under Object1 variable
        Object2 = self.Object(m2, d, simFrame) # creates an object instance under Object2 variable
        
        simFrame.after(32) # sets the time for the frame rate
        simFrame.update() # updates the canvas
    
    def runSim(self, m1Select, m2Select, dSelect, startButton, simFrame, main):
        global m1, m2, d # import global variables
        
        m1Select.config(bg = "#555", fg = "white", state = "disabled") # disables the mass1 selection button
        m2Select.config(bg = "#555", fg = "white", state = "disabled") # disables the mass2 selection button
        dSelect.config(bg = "#555", fg = "white", state = "disabled") # disables the dist selection button
        startButton.config(bg = "#555", fg = "white", state = "disabled") # disables the start button
        
        stopButton = tk.Button(main, text = "STOP SIMULATION", bg = "red", fg = "white", relief = FLAT) # creates the stop simulation button
        stopButton.pack(side = LEFT, anchor = S, padx = 5, pady = 5)
        stopButton.config(command = lambda : self.stopSim(m1Select, m2Select, dSelect, startButton, stopButton, simFrame, main)) # sets the command to stopSim
        
        running = True # sets running variable to True
        while running == True: # runs loop while running stays true
            self.Update(simFrame)# updates the canvas every frame
            
            if m1 <= 0 or m2 <= 0 or d <= 0:
                running = False # if the objects collide, or masses reach 0, stop simulation
            
    def stopSim(self, m1Select, m2Select, dSelect, startButton, stopButton, simFrame, main): # runs if the simulation is stopped
        stopButton.destroy() # deletes the stop button
        simFrame.delete("all") # deletes everything in canvas
        
        m1Select.config(bg = "#666", fg = "white", state = "normal") # reenables the mass1 selection button
        m2Select.config(bg = "#666", fg = "white", state = "normal") # reenables the mass2 selection button
        dSelect.config(bg = "#666", fg = "white", state = "normal") # reenables the dist selection button
        startButton.config(bg = "green", fg = "white", state = "normal") # reenables the start button
        
        
def Run(): # runs the program
    sim = Window()  # call the Window class which runs the simulation program

while __name__ == "__main__":# only runs the Run subroutine if this is ran from the main program and not from an imported module
    Run()