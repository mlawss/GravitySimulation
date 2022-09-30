from tkinter import *
import tkinter as tk
from tkinter import ttk
import math
import random
import time

#Version 5:
# added calculations to update subroutine
# added updating labels to the simulation frame
# added animations of objects

#CONSTANTS
G = 6.67 * 10**-11 # Newton's gravitational constant
PI = 3.141592653

#GLOBAL VARIABLES
m1 = int(2) # mass of object 1
m2 = int(1) # mass of object 2
d = int(50) # distance between object 1 and object 2
d0 = int(50) # initial distance between each object [for calculations of velocity etc]

class Window(): #class of the main window where the simulation will run
    
    def __init__(self): # call the initUI subroutine when the window class is called
        self.initUI()
        
    def initUI(self): # this method is the same as in previous versions.
        global m1, m2, d
        
        main = Tk()
        main.title("Gravitational Fields Simulation")
        main.geometry("1280x720")
        
        simFrame = tk.Canvas(main, relief = FLAT, width = 800, height = 720, bg = "black", borderwidth = 0)
        simFrame.pack(side = LEFT, fill = BOTH)
        
        welcomeMsg = tk.Label(main, text = "Welcome!", font = ("Courier New", 16))
        welcomeMsg.pack(anchor = N)
        infoMsgLine1 = tk.Label(main, text = "To begin, set the key values below", font = ("Courier New", 10))
        infoMsgLine1.pack(anchor = N)
        infoMsgLine2 = tk.Label(main, text = "and press the start simulation button.", font = ("Courier New", 10))
        infoMsgLine2.pack(anchor = N)
        scaleInfo1 = tk.Label(main, text = "1 PIXEL = 1 METRE. VALUES HIGHER THAN ~700M WILL BE OUT OF RANGE.", font = ("Dotum", 9), fg = "red")
        scaleInfo1.place(x = 805, y = 322)
        scaleInfo2 = tk.Label(main, text = "SIMILARLY, 1 KG = 5 PIXELS WIDE. VALUES HIGHER THAN ~50KG WILL BE", font = ("Dotum", 9), fg = "red")
        scaleInfo2.place(x = 805, y = 352)
        scaleInfo3 = tk.Label(main, text = "OUT OF RANGE.", font = ("Dotum", 9), fg = "red")
        scaleInfo3.place(x = 805, y = 372)
        
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
        startButton.config(command = lambda : self.runSim(m1Select, m2Select, dSelect, startButton, simFrame, main))
        
        quitButton = tk.Button(main, text = "QUIT", relief = FLAT, fg = "white", bg = "red", command = quit)
        quitButton.pack(side = RIGHT, anchor = S, padx = 5, pady = 5)
        
        main.mainloop()
    
    
    def enterMass1(self, m1Select, m1StatusMsg): # these methods are also the same for value selection.
        global m1
        
        enterMass1Window = Tk()
        enterMass1Window.title("Enter Mass 1")
        enterMass1Window.geometry("200x100+300+300")
        
        m1Confirm = tk.Button(enterMass1Window, text = "Confirm", relief = FLAT, bg = "white")
        m1Confirm.pack(side = BOTTOM, pady = 10)
        m1Confirm.config(command = lambda : self.confirmMass1(m1Select, m1StatusMsg, m1Confirm, m1Entry, enterMass1Window))
        
        m1Entry = tk.Entry(enterMass1Window)
        m1Entry.pack(side = TOP, pady = 10)
    
    def confirmMass1(self, m1Select, m1StatusMsg, m1Confirm, m1Entry, enterMass1Window):
        global m1
        
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
        
        m1StatusMsg.config(text = ("The mass of object 1 is",m1,"kg."))
        
    def enterMass2(self, m2Select, m2StatusMsg):
        global m2
        
        enterMass2Window = Tk()
        enterMass2Window.title("Enter Mass 2")
        enterMass2Window.geometry("200x100+300+300")
        
        m2Confirm = tk.Button(enterMass2Window, text = "Confirm", relief = FLAT, bg = "white")
        m2Confirm.pack(side = BOTTOM, pady = 10)
        m2Confirm.config(command = lambda : self.confirmMass2(m2Select, m2StatusMsg, m2Confirm, m2Entry, enterMass2Window))
        
        m2Entry = tk.Entry(enterMass2Window)
        m2Entry.pack(side = TOP, pady = 10)
    
    def confirmMass2(self, m2Select, m2StatusMsg, m2Confirm, m2Entry, enterMass2Window):
        global m2
        
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
        
        m2StatusMsg.config(text = ("The mass of object 2 is",m2,"kg."))
        
    def enterDist(self, dSelect, dStatusMsg):
        global d, d0
        
        enterDistWindow = Tk()
        enterDistWindow.title("Enter Distance")
        enterDistWindow.geometry("200x100+300+300")
        
        dConfirm = tk.Button(enterDistWindow, text = "Confirm", relief = FLAT, bg = "white")
        dConfirm.pack(side = BOTTOM, pady = 10)
        dConfirm.config(command = lambda : self.confirmDist(dSelect, dStatusMsg, dConfirm, dEntry, enterDistWindow))
        
        dEntry = tk.Entry(enterDistWindow)
        dEntry.pack(side = TOP, pady = 10)
        
    def confirmDist(self, dSelect, dStatusMsg, dConfirm, dEntry, enterDistWindow):
        global d, d0
        
        correct = False
        while correct == False:
            try:
                d = int(dEntry.get())
                d0 = int(dEntry.get())
                correct = True
                enterDistWindow.destroy()
                break
            except:
                dError = tk.Label(enterDistWindow, text = "That value is not valid.", font = ("Courier New", 8), fg = "red")
                dError.place(x = 15, y = 35)
                correct = False
                break
        
        dStatusMsg.config(text = ("The distance between the objects is",d,"m."))
        
    class Object(): # class of the object - creates instances of objects using OOP
        # this has already been covered in object initialisation/calculation steps.
        def __init__(self, mass, dist, simFrame):
            self.mass = mass # set internal variables of class
            self.dist = dist
            self.initObject(mass, dist, simFrame)
            
        def initObject(self, mass, dist, simFrame):
            global m1, m2, d
            
            xpos_1 = 400 - (d/2) # x position of obj 1 - the distance is taken away so that it is to the left
            ypos_1 = 360 # y position of obj 1
            xpos_2 = 400 + (d/2) # x position of obj 2 - distance is added so that it is to the right
            ypos_2 = 360 # y position of obj 2
            
            if mass == m1:
                xradius = xpos_1 - mass*5 # multiplied by 5 --> each kg adds 5 pixels to the object's diameter
                yradius = ypos_1 - mass*5
                
                obj = simFrame.create_oval(xpos_1, ypos_1, xradius, yradius, fill = "red")
                return obj
            
            elif mass == m2:
                xradius = xpos_2 - mass*5
                yradius = ypos_2 - mass*5
                
                obj = simFrame.create_oval(xpos_2, ypos_2, xradius, yradius, fill = "red")
                return obj
            
            else:
                print("Something went very wrong. Mass not found for object created.") # just in case...
            
        def calcGravForce(self, simFrame):
            global m1, m2, d
            
            if d > 0 or d < 0:
                f = (G * m1 * m2) / (d**2)
                return f
            
            elif d == 0:
                f = (G * m1 * m2) / ((d+(10 ** -99)) ** 2)
                return f
        
        def calcGravPotential(self, simFrame):
            global m1, m2, d
            
            if d > 0 or d < 0:
                if m1 >= m2:
                    gpe = (G * m1) / d
                    return gpe
                    
                elif m1 < m2:
                    gpe = (G * m2) / d
                    return gpe
                
            elif d == 0:
                if m1 >= m2:
                    gpe = (G * m1) / (d+(10 ** -99))
                    return gpe
                    
                elif m1 < m2:
                    gpe = (G * m2) / (d+(10 ** -99))
                    return gpe
        
        def calcGravFieldStrength(self, simFrame): # can also be acceleration towards the other object in m/s^2
            global m1, m2, d
            
            if d > 0 or d < 0:
                if m1 >= m2:
                    gl = (G * m1) / (d**2) # field acting on / acceleration of smaller object
                    gs = (G * m2) / (d**2) # field acting on / acceleration of larger object
                    
                    return gl, gs
                    
                elif m1 < m2:
                    gl = (G * m2) / (d**2) # field acting on / acceleration of smaller object
                    gs = (G * m1) / (d**2) # field acting on / acceleration of larger object
                    
                    return gl, gs
            
            elif d == 0:
                if m1 >= m2:
                    gl = (G * m1) / ((d+(10 ** -99))**2) # field acting on / acceleration of smaller object
                    gs = (G * m2) / ((d+(10 ** -99))**2) # field acting on / acceleration of larger object
                    
                    return gl, gs
                    
                elif m1 < m2:
                    gl = (G * m2) / ((d+(10 ** -99))**2) # field acting on / acceleration of smaller object
                    gs = (G * m1) / ((d+(10 ** -99))**2) # field acting on / acceleration of larger object
                    
                    return gl, gs

            
        def calcVelocity(self, gl, gs, simFrame):
            global m1, m2, d, d0
            
            if d > 0 or d < 0:
                if d0 - d <= 0:
                    if m1 >= m2:
                        vel_obj1 = math.sqrt(2 * (d - d0) * (gs)) # v^2 = u^2 + 2as where u = 0 as the objects are initially stationary
                        vel_obj2 = math.sqrt(2 * (d - d0) * (gl)) # therefore v = sqrt(2as) where v is velocity, a is acceleration and s is distance travelled
                        return vel_obj1, vel_obj2
                    
                    elif m1 < m2:
                        vel_obj1 = math.sqrt(2 * (d - d0) * (gl))
                        vel_obj2 = math.sqrt(2 * (d - d0) * (gs))
                        return vel_obj1, vel_obj2
                    
                elif d0 - d > 0:
                    if m1 >= m2:
                        vel_obj1 = math.sqrt(2 * (d0 - d) * (gs))
                        vel_obj2 = math.sqrt(2 * (d0 - d) * (gl))
                        return vel_obj1, vel_obj2
                    
                    elif m1 < m2:
                        vel_obj1 = math.sqrt(2 * (d0 - d) * (gl))
                        vel_obj2 = math.sqrt(2 * (d0 - d) * (gs))
                        return vel_obj1, vel_obj2
                    
            elif d == 0:
                if d0 - d <= 0:
                    if m1 >= m2:
                        vel_obj1 = math.sqrt(2 * ((d+(10 ** -99)) - d0) * (gs)) # v^2 = u^2 + 2as where u = 0 as the objects are initially stationary
                        vel_obj2 = math.sqrt(2 * ((d+(10 ** -99)) - d0) * (gl)) # therefore v = sqrt(2as) where v is velocity, a is acceleration and s is distance travelled
                        return vel_obj1, vel_obj2
                    
                    elif m1 < m2:
                        vel_obj1 = math.sqrt(2 * ((d+(10 ** -99)) - d0) * (gl))
                        vel_obj2 = math.sqrt(2 * ((d+(10 ** -99)) - d0) * (gs))
                        return vel_obj1, vel_obj2
                    
                elif d0 - d > 0:
                    if m1 >= m2:
                        vel_obj1 = math.sqrt(2 * (d0 - (d+(10 ** -99))) * (gs))
                        vel_obj2 = math.sqrt(2 * (d0 - (d+(10 ** -99))) * (gl))
                        return vel_obj1, vel_obj2
                    
                    elif m1 < m2:
                        vel_obj1 = math.sqrt(2 * (d0 - (d+(10 ** -99))) * (gl))
                        vel_obj2 = math.sqrt(2 * (d0 - (d+(10 ** -99))) * (gs))
                        return vel_obj1, vel_obj2
            
        def calcKineticEnergy(self, vel_obj1, vel_obj2, simFrame):
            global m1, m2, d
            
            ke_obj1 = (1/2) * m1 * (vel_obj1 ** 2) # KE = 1/2(m)(v^2)
            ke_obj2 = (1/2) * m2 * (vel_obj2 ** 2)
            
            return ke_obj1, ke_obj2
            
    
    def Update(self, simFrame): # update method
        global m1, m2, d # import global variables
        
        simFrame.delete("all") # delete all objects from canvas to update it
        
        Object1 = self.Object(m1, d, simFrame) # initialise (or re-initialise) each object
        Object2 = self.Object(m2, d, simFrame)
        
        G_Force = Object1.calcGravForce(simFrame) # calculate values
        G_Pot = Object1.calcGravPotential(simFrame)
        G_FieldS_1, G_FieldS_2 = Object1.calcGravFieldStrength(simFrame)
        Vel_1, Vel_2 = Object1.calcVelocity(G_FieldS_1, G_FieldS_2, simFrame)
        KE_1, KE_2 = Object1.calcKineticEnergy(Vel_1, Vel_2, simFrame)
        
        # place status messages of each value inside the canvas - this is temporary and a replacement for the table of values.
        G_Force_StatusMsg = tk.Label(simFrame, text = ("Grav force:",G_Force*(10**9),"nN"), fg = "white", bg = "black", font = ("Dotum", 8))
        G_Force_StatusMsg.place(x = 5, y = 5)
        
        G_Pot_StatusMsg = tk.Label(simFrame, text = ("Grav potential:",G_Pot*(10**9),"nJ/kg"), fg = "white", bg = "black", font = ("Dotum", 8))
        G_Pot_StatusMsg.place(x = 5, y = 25)
        
        G_FieldS_1_StatusMsg = tk.Label(simFrame, text = ("Acceleration [smaller obj]:",G_FieldS_1*(10**9),"nm/s^2"), fg = "white", bg = "black", font = ("Dotum", 8))
        G_FieldS_1_StatusMsg.place(x = 5, y = 45)
        G_FieldS_2_StatusMsg = tk.Label(simFrame, text = ("Acceleration [larger obj]:",G_FieldS_2*(10**9),"nm/s^2"), fg = "white", bg = "black", font = ("Dotum", 8))
        G_FieldS_2_StatusMsg.place(x = 5, y = 65)
        
        Vel_1_StatusMsg = tk.Label(simFrame, text = ("Velocity [smaller obj]:",Vel_1*(10**6),"μm/s"), fg = "white", bg = "black", font = ("Dotum", 8))
        Vel_1_StatusMsg.place(x = 5, y = 85)
        Vel_2_StatusMsg = tk.Label(simFrame, text = ("Velocity [larger obj]:",Vel_2*(10**6),"μm/s"), fg = "white", bg = "black", font = ("Dotum", 8))
        Vel_2_StatusMsg.place(x = 5, y = 105)
        
        KE_1_StatusMsg = tk.Label(simFrame, text = ("Kinetic energy [smaller obj]:",KE_1*(10**9),"nJ"), fg = "white", bg = "black", font = ("Dotum", 8))
        KE_1_StatusMsg.place(x = 5, y = 125)
        KE_2_StatusMsg = tk.Label(simFrame, text = ("Kinetic energy [larger obj]:",KE_2*(10**9),"nJ"), fg = "white", bg = "black", font = ("Dotum", 8))
        KE_2_StatusMsg.place(x = 5, y = 145)
        
        d-=1 # distance -1 to animate objects
        
        simFrame.after(32) # 30 FPS
        simFrame.update() # updates user's view of the canvas
        
        G_Force_StatusMsg.destroy() # destroys the status messages so they do not stack on top of each other
        G_Pot_StatusMsg.destroy()
        G_FieldS_1_StatusMsg.destroy()
        G_FieldS_2_StatusMsg.destroy()
        Vel_1_StatusMsg.destroy()
        Vel_2_StatusMsg.destroy()
        KE_1_StatusMsg.destroy()
        KE_2_StatusMsg.destroy()
    
    def runSim(self, m1Select, m2Select, dSelect, startButton, simFrame, main): # nothing changed since last step.
        global m1, m2, d
        
        m1Select.config(bg = "#555", fg = "white", state = "disabled")
        m2Select.config(bg = "#555", fg = "white", state = "disabled")
        dSelect.config(bg = "#555", fg = "white", state = "disabled")
        startButton.config(bg = "#555", fg = "white", state = "disabled")
        
        stopButton = tk.Button(main, text = "STOP SIMULATION", bg = "red", fg = "white", relief = FLAT)
        stopButton.pack(side = LEFT, anchor = S, padx = 5, pady = 5)
        stopButton.config(command = lambda : self.stopSim(m1Select, m2Select, dSelect, startButton, stopButton, simFrame, main))
        
        running = True
        while running == True:
            simFrame.delete("all")
            
            self.Update(simFrame)
            
            if m1 <= 0 or m2 <= 0: # stops the sim if the masses become negative/0.
                running = False
            
    def stopSim(self, m1Select, m2Select, dSelect, startButton, stopButton, simFrame, main): # nothing changed since last step.
        stopButton.destroy()
        simFrame.delete("all")
        
        m1Select.config(bg = "#666", fg = "white", state = "normal")
        m2Select.config(bg = "#666", fg = "white", state = "normal")
        dSelect.config(bg = "#666", fg = "white", state = "normal")
        startButton.config(bg = "green", fg = "white", state = "normal")
        
        
def Run(): # nothing changed.
    sim = Window()
    
while __name__ == "__main__": # nothing changed.
    Run()