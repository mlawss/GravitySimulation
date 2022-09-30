from tkinter import *
import tkinter as tk
from tkinter import ttk
import math
import random
import time

#Version 10:
# added preset sims selection system

#CONSTANTS
G = 6.67 * 10**-11 # Newton's gravitational constant
PI = 3.141592653
BOWLING_MASS = int(6)
BOULDER_MASS = int(45)

#GLOBAL VARIABLES
m1 = int(10) # mass of object 1
m2 = int(5) # mass of object 2
d = int(200) # distance between object 1 and object 2
d0 = int(200) # initial distance between each object [for calculations of velocity etc]
running = True # tells the program whether it is running or not
xpos_1 = 1
ypos_1 = 1
xpos_2 = 1
ypos_2 = 1
scenario_choice = int(0) # user's choice of the scenario
fps = int(5)# frames per second the sim is run at
v1 = 0 #velocity 1
v2 = 0 #velocity 2
gf = 0 #gforce
gp = 0 #g potential
gfs1 = 0 #g field strength 1
gfs2 = 0 #g field strength 2
ke1 = 0 #kinetic energy 1
ke2 = 0 #kinetic energy 2
vol1 = 0 #volume 1
vol2 = 0 #volume 2
dens1 = 0 #density 1
dens2 = 0 #density 2
# these below are all global placeholders for the tk labels inside the table of values
# fixes problems with variables not being recognised.
Distance_1 = None
Distance_2 = None
Mass_1 = None
Mass_2 = None
Velocity_1 = None
Velocity_2 = None
Grav_Force1 = None
Grav_Force2 = None
Grav_Pot1 = None
Grav_Pot2 = None
Grav_FS1 = None
Grav_FS2 = None
KE_1 = None
KE_2 = None
Volume_1 = None
Volume_2 = None
Density_1 = None
Desnity_2 = None

class Window(): #class of the main window where the simulation will run
    
    def __init__(self):
        self.initUI()
        
    def initUI(self):
        global m1, m2, d
        
        main = Tk()
        main.title("Gravitational Fields Simulation")
        main.geometry("1280x720+600+0")
        
        simFrame = tk.Canvas(main, relief = FLAT, width = 800, height = 720, bg = "black", borderwidth = 0)
        simFrame.pack(side = LEFT, fill = BOTH)
        
        welcomeMsg = tk.Label(main, text = "Welcome!", font = ("Courier New", 16))
        welcomeMsg.pack(anchor = N)
        infoMsgLine1 = tk.Label(main, text = "To begin, set the key values below", font = ("Courier New", 10))
        infoMsgLine1.pack(anchor = N)
        infoMsgLine2 = tk.Label(main, text = "and press the start simulation button.", font = ("Courier New", 10))
        infoMsgLine2.pack(anchor = N)
        scaleInfo1 = tk.Label(main, text = "1 PIXEL = 1 METRE. VALUES HIGHER THAN ~700M WILL BE OUT OF RANGE.", font = ("Dotum", 9), fg = "red")
        scaleInfo1.place(x = 805, y = 612)
        scaleInfo2 = tk.Label(main, text = "SIMILARLY, 1 KG = 5 PIXELS WIDE. VALUES HIGHER THAN ~50KG WILL BE", font = ("Dotum", 9), fg = "red")
        scaleInfo2.place(x = 805, y = 642)
        scaleInfo3 = tk.Label(main, text = "OUT OF RANGE.", font = ("Dotum", 9), fg = "red")
        scaleInfo3.place(x = 805, y = 662)
        
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
        
        fpsSelect = tk.Button(main, text = "Choose FPS", relief = FLAT, bg = "#666", fg = "white")
        fpsSelect.place(x = 806, y = 382)
        fpsSelect.config(command = lambda : self.enterFPS(fpsSelect, fpsStatusMsg))
        fpsStatusMsg = tk.Label(main, text = ("The frames per second is",fps,"FPS."), font = ("Courier New", 11))
        fpsStatusMsg.place(x = 802, y = 352)
        
        presetMsg = tk.Label(main, text = "Or choose from the presets below:")
        presetMsg.place(x = 802, y = 450)
        
        preset1 = tk.Button(main, text = "2 BOWLING BALLS", relief = FLAT, bg = "#666", fg = "white")
        preset1.place(x=802, y=490)
        preset1.config(command = lambda : self.choosePreset1(main, preset1, m1StatusMsg, m2StatusMsg, dStatusMsg))
        preset2 = tk.Button(main, text = "1 BOWLING BALL, 1 BOULDER", relief = FLAT, bg = "#666", fg = "white")
        preset2.place(x=802, y=530)
        preset2.config(command = lambda : self.choosePreset2(main, preset2, m1StatusMsg, m2StatusMsg, dStatusMsg))
        preset3 = tk.Button(main, text = "2 BOULDERS", relief = FLAT, bg = "#666", fg = "white")
        preset3.place(x=802, y=570)
        preset3.config(command = lambda : self.choosePreset3(main, preset3, m1StatusMsg, m2StatusMsg, dStatusMsg))
        
        startButton = tk.Button(main, text = "START SIMULATION", relief = FLAT, fg = "white", bg = "green")
        startButton.pack(side = LEFT, anchor = S, padx = 5, pady = 5)
        startButton.config(command = lambda : self.enterScenario(fpsSelect, m1Select, m2Select, dSelect, startButton, simFrame, main))
        
        quitButton = tk.Button(main, text = "QUIT", relief = FLAT, fg = "white", bg = "red", command = quit)
        quitButton.pack(side = RIGHT, anchor = S, padx = 5, pady = 5)
        
        main.mainloop()
    
    def choosePreset1(self, main, preset1, m1StatusMsg, m2StatusMsg, dStatusMsg):
        global m1, m2, d
        
        m1 = BOWLING_MASS
        m2 = BOWLING_MASS
        
        m1StatusMsg.config(text = ("The mass of object 1 is",m1,"kg."))
        m2StatusMsg.config(text = ("The mass of object 2 is",m2,"kg."))
        
    def choosePreset2(self, main, preset2, m1StatusMsg, m2StatusMsg, dStatusMsg):
        global m1, m2, d
        
        m1 = BOWLING_MASS
        m2 = BOULDER_MASS
        
        m1StatusMsg.config(text = ("The mass of object 1 is",m1,"kg."))
        m2StatusMsg.config(text = ("The mass of object 2 is",m2,"kg."))
    
    def choosePreset3(self, main, preset3, m1StatusMsg, m2StatusMsg, dStatusMsg):
        global m1, m2, d
        
        m1 = BOULDER_MASS
        m2 = BOULDER_MASS
        
        m1StatusMsg.config(text = ("The mass of object 1 is",m1,"kg."))
        m2StatusMsg.config(text = ("The mass of object 2 is",m2,"kg."))
    
    def enterMass1(self, m1Select, m1StatusMsg):
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
        
    def enterFPS(self, fpsSelect, fpsStatusMsg):
        global fps
        
        enterFPSWindow = Tk()
        enterFPSWindow.title("Enter FPS")
        enterFPSWindow.geometry("200x100+300+300")
        
        fpsConfirm = tk.Button(enterFPSWindow, text = "Confirm", relief = FLAT, bg = "white")
        fpsConfirm.pack(side = BOTTOM, pady = 10)
        fpsConfirm.config(command = lambda : self.confirmFPS(fpsSelect, fpsStatusMsg, fpsConfirm, fpsEntry, enterFPSWindow))
        
        fpsEntry = tk.Entry(enterFPSWindow)
        fpsEntry.pack(side = TOP, pady = 10)
    
    def confirmFPS(self, fpsSelect, fpsStatusMsg, fpsConfirm, fpsEntry, enterFPSWindow):
        global fps
        
        correct = False
        while correct == False:
            try:
                fps = int(fpsEntry.get())
                correct = True
                enterFPSWindow.destroy()
                break
            except:
                fpsError = tk.Label(enterFPSWindow, text = "That value is not valid.", font = ("Courier New", 8), fg = "red")
                fpsError.place(x = 15, y = 35)
                correct = False
                break
        
        fpsStatusMsg.config(text = ("The frames per second is",fps,"FPS."))
        
    class Object(): # class of the object - creates instances of objects using OOP
        
        def __init__(self, mass, dist, simFrame):
            self.mass = mass # set internal variables of class
            self.dist = dist
            self.initObject(mass, dist, simFrame)
            
        def initObject(self, mass, dist, simFrame):
            global m1, m2, d, xpos_1, xpos_2, ypos_1, ypos_2
            
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
        
        def calcVolume(self, simFrame):
            global m1, m2, d, PI
            
            #v = 4/3*pi*r^3
            vol_obj1 = (4/3) * PI * (((m1*5)/2)**3)
            vol_obj2 = (4/3) * PI * (((m2*5)/2)**3)
            
            return vol_obj1, vol_obj2
        
        def calcDensity(self, vol_obj1, vol_obj2, simFrame):
            global m1, m2
            
            #p = m/v
            dens_obj1 = m1 / vol_obj1
            dens_obj2 = m2 / vol_obj2
            
            return dens_obj1, dens_obj2
    
    def enterScenario(self, fpsSelect, m1Select, m2Select, dSelect, startButton, simFrame, main):
        global m1, m2, d
        
        scenarioWindow = Tk()
        scenarioWindow.title("Select Scenario")
        scenarioWindow.geometry("600x600")
        
        scenarioEntry = tk.Entry(scenarioWindow)
        scenarioEntry.pack(anchor = N)
        
        confirmButton = tk.Button(scenarioWindow, text = "CONFIRM AND START", fg = "white", bg = "black", relief = FLAT)
        confirmButton.pack(side = BOTTOM)
        confirmButton.config(command = lambda : self.confirmScenario(fpsSelect, confirmButton, scenarioEntry, scenarioWindow, m1Select, m2Select, dSelect, startButton, simFrame, main))
        
        info = tk.Label(scenarioWindow, text = ("In the box above, enter the corresponding number for your choice:"), font = ("", 11))
        info.place(x=5, y=40)
        
        sce1 = tk.Label(scenarioWindow, text = ("0 --- No changes, values stay the same"), font = ("", 11))
        sce1.place(x=5, y=80)
        sce2 = tk.Label(scenarioWindow, text = ("1 --- Decrease distance slowly (-1m each frame)"), font = ("", 11))
        sce2.place(x=5, y=120)
        sce3 = tk.Label(scenarioWindow, text = ("2 --- Decrease distance quickly (-4m each frame)"), font = ("", 11))
        sce3.place(x=5, y=160)
        sce4 = tk.Label(scenarioWindow, text = ("3 --- Increase distance slowly (+1m each frame)"), font = ("", 11))
        sce4.place(x=5, y=200)
        sce5 = tk.Label(scenarioWindow, text = ("4 --- Increase distance quickly (+4m each frame)"), font = ("", 11))
        sce5.place(x=5, y=240)
        sce6 = tk.Label(scenarioWindow, text = ("5 --- Increase the mass of object 1 (+1kg each frame)"), font = ("", 11))
        sce6.place(x=5, y=280)
        sce7 = tk.Label(scenarioWindow, text = ("6 --- Increase the mass of object 1/decrease the mass of object 2 (+1kg/-1kg each frame)"), font = ("", 11))
        sce7.place(x=5, y=320)
        sce8 = tk.Label(scenarioWindow, text = ("7 --- Increase both masses (+1kg each frame)"), font = ("", 11))
        sce8.place(x=5, y=360)
        sce9 = tk.Label(scenarioWindow, text = ("8 --- Decrease both masses (-1kg each frame)"), font = ("", 11))
        sce9.place(x=5, y=400)
        sce10 = tk.Label(scenarioWindow, text = ("9 --- Increase the mass of object 1/decrease distance (+1kg/-1m each frame)"), font = ("", 11))
        sce10.place(x=5, y=440)
        sce11 = tk.Label(scenarioWindow, text = ("10 --- Decrease the mass of object 1/increase distance (-1kg/+1m each frame)"), font = ("", 11))
        sce11.place(x=5, y=480)
        
    def confirmScenario(self, fpsSelect, confirmButton, scenarioEntry, scenarioWindow, m1Select, m2Select, dSelect, startButton, simFrame, main):
        global m1, m2, d, scenario_choice
        
        valid = False
        while valid == False:
            try:
                scenario_choice = int(scenarioEntry.get())
                if scenario_choice > 10 or scenario_choice < 0:
                    sceError = tk.Label(scenarioWindow, text = "That choice is not valid. Make sure it is a number from 0 to 10.", fg = "red", font = ("", 11))
                    sceError.pack(side = BOTTOM)
                    valid = False
                else:
                    scenarioWindow.destroy()
                    self.runSim(fpsSelect, m1Select, m2Select, dSelect, startButton, simFrame, main)
                    valid = True
                break
            except:
                sceError = tk.Label(scenarioWindow, text = "That choice is not valid. Make sure it is a number from 0 to 10.", fg = "red", font = ("", 11))
                sceError.pack(side = BOTTOM)
                valid = False
                break
    
    def createTableOfValues(self, simFrame, main):
        global m1, m2, d, d0, v1, v2, gf, gp, gfs1, gfs2, ke1, ke2, vol1, vol2, dens1, dens2, Velocity_1, Velocity_2, Grav_Force1, Grav_Force2, Grav_Pot1, Grav_Pot2, Grav_FS1, Grav_FS2, KE_1, KE_2, Volume_1, Volume_2, Density_1, Density_2, Distance_1, Distance_2, Mass_1, Mass_2
        
        TableOfValues = Tk()
        TableOfValues.title("Table of Values")
        TableOfValues.geometry("500x600+0+200")
        
        Obj1 = tk.Label(TableOfValues, text = "Object 1", font = ("", 12))
        Obj1.place(x=225, y=5)
        Obj2 = tk.Label(TableOfValues, text = "Object 2", font = ("", 12))
        Obj2.place(x=385, y=5)
        
        Mass = tk.Label(TableOfValues, text = "Mass (kg)", font = ("", 12))
        Mass.place(x=5, y=50)
        Distance = tk.Label(TableOfValues, text = "Distance (m)", font = ("", 12))
        Distance.place(x=5, y=100)
        Velocity = tk.Label(TableOfValues, text = "Velocity (nm/s)", font = ("", 12))
        Velocity.place(x=5, y=150)
        Grav_Force = tk.Label(TableOfValues, text = "Grav. Force (pN)", font = ("", 12))
        Grav_Force.place(x=5, y=200)
        Grav_Pot = tk.Label(TableOfValues, text = "Grav. Potential (pJ/kg)", font = ("", 12))
        Grav_Pot.place(x=5, y=250)
        Grav_FieldS = tk.Label(TableOfValues, text = "Grav. Field Strength (pN/kg)", font = ("", 9))
        Grav_FieldS.place(x=5, y=290)
        Acceleration = tk.Label(TableOfValues, text = "Acceleration (pm/s^2)", font = ("", 9))
        Acceleration.place(x=5, y=310)
        Kin_Energy = tk.Label(TableOfValues, text = "Kinetic Energy (pJ)", font = ("",12))
        Kin_Energy.place(x=5, y=350)
        Volume = tk.Label(TableOfValues, text = "Volume (m^3)", font = ("",12))
        Volume.place(x=5, y=400)
        Density = tk.Label(TableOfValues, text = "Density (mkg/m^3)", font = ("",12))
        Density.place(x=5, y=450)
        
        vert_line1 = tk.Canvas(TableOfValues, width = 2, height = 485, bg = "black", relief = FLAT, borderwidth = 0)
        vert_line1.place(x=175,y=0)
        vert_line2 = tk.Canvas(TableOfValues, width = 2, height = 485, bg = "black", relief = FLAT, borderwidth = 0)
        vert_line2.place(x=335,y=0)
        hor_line1 = tk.Canvas(TableOfValues, width = 500, height = 2, bg = "black", relief = FLAT, borderwidth = 0)
        hor_line1.place(x=0, y=30)
        hor_line2 = tk.Canvas(TableOfValues, width = 500, height = 2, bg = "black", relief = FLAT, borderwidth = 0)
        hor_line2.place(x=0, y=85)
        hor_line3 = tk.Canvas(TableOfValues, width = 500, height = 2, bg = "black", relief = FLAT, borderwidth = 0)
        hor_line3.place(x=0, y=135)
        hor_line4 = tk.Canvas(TableOfValues, width = 500, height = 2, bg = "black", relief = FLAT, borderwidth = 0)
        hor_line4.place(x=0, y=185)
        hor_line5 = tk.Canvas(TableOfValues, width = 500, height = 2, bg = "black", relief = FLAT, borderwidth = 0)
        hor_line5.place(x=0, y=235)
        hor_line6 = tk.Canvas(TableOfValues, width = 500, height = 2, bg = "black", relief = FLAT, borderwidth = 0)
        hor_line6.place(x=0, y=285)
        hor_line7 = tk.Canvas(TableOfValues, width = 500, height = 2, bg = "black", relief = FLAT, borderwidth = 0)
        hor_line7.place(x=0, y=335)
        hor_line8 = tk.Canvas(TableOfValues, width = 500, height = 2, bg = "black", relief = FLAT, borderwidth = 0)
        hor_line8.place(x=0, y=385)
        hor_line9 = tk.Canvas(TableOfValues, width = 500, height = 2, bg = "black", relief = FLAT, borderwidth = 0)
        hor_line9.place(x=0, y=435)
        hor_line10 = tk.Canvas(TableOfValues, width = 500, height = 2, bg = "black", relief = FLAT, borderwidth = 0)
        hor_line10.place(x=0, y=485)
        
        #obj1 = 205
        #obj2 = 365
        
        Mass_1 = tk.Label(TableOfValues, text = (round(m1, 2)), font = ("",12))
        Mass_1.place(x=205, y=50)
        Mass_2 = tk.Label(TableOfValues, text = (round(m2, 2)), font = ("",12))
        Mass_2.place(x=365, y=50)
        Distance_1 = tk.Label(TableOfValues, text = (round(d, 2)), font = ("",12))
        Distance_1.place(x=205, y=100)
        Distance_2 = tk.Label(TableOfValues, text = (round(d, 2)), font = ("",12))
        Distance_2.place(x=365, y=100)
        Velocity_1 = tk.Label(TableOfValues, text = (v1), font = ("",12))
        Velocity_1.place(x=205, y=150)
        Velocity_2 = tk.Label(TableOfValues, text = (v2), font = ("",12))
        Velocity_2.place(x=365, y=150)
        Grav_Force1 = tk.Label(TableOfValues, text = (gf), font = ("",12))
        Grav_Force1.place(x=205, y=200)
        Grav_Force2 = tk.Label(TableOfValues, text = (gf), font = ("",12))
        Grav_Force2.place(x=365, y=200)
        Grav_Pot1 = tk.Label(TableOfValues, text = (gp), font = ("",12))
        Grav_Pot1.place(x=205, y=250)
        Grav_Pot2 = tk.Label(TableOfValues, text = (gp), font = ("",12))
        Grav_Pot2.place(x=365, y=250)
        Grav_FS1 = tk.Label(TableOfValues, text = (gfs1), font = ("",12))
        Grav_FS1.place(x=205, y=300)
        Grav_FS2 = tk.Label(TableOfValues, text = (gfs2), font = ("",12))
        Grav_FS2.place(x=365, y=300)
        KE_1 = tk.Label(TableOfValues, text = (ke1), font = ("",12))
        KE_1.place(x=205, y=350)
        KE_2 = tk.Label(TableOfValues, text = (ke2), font = ("",12))
        KE_2.place(x=365, y=350)
        Volume_1 = tk.Label(TableOfValues, text = (vol1), font = ("",12))
        Volume_1.place(x=205, y=400)
        Volume_2 = tk.Label(TableOfValues, text = (vol2), font = ("",12))
        Volume_2.place(x=365, y=400)
        Density_1 = tk.Label(TableOfValues, text = (dens1), font = ("",12))
        Density_1.place(x=205, y=450)
        Density_2 = tk.Label(TableOfValues, text = (dens2), font = ("",12))
        Density_2.place(x=365, y=450)
        
        
    def closeTableOfValues(self, simFrame, main):
        TableOfValues.destroy()
        
    #def displayDataSummary(self, simFrame, main):
    
    def Update(self, simFrame):
        global m1, m2, d, d0, v1, v2, gf, gp, gfs1, gfs2, ke1, ke2, vol1, vol2, dens1, dens2, Velocity_1, Velocity_2, Grav_Force1, Grav_Force2, Grav_Pot1, Grav_Pot2, Grav_FS1, Grav_FS2, KE_1, KE_2, Volume_1, Volume_2, Density_1, Density_2, Distance_1, Distance_2, Mass_1, Mass_2, scenario_choice, fps
        
        simFrame.delete("all")
        
        Object1 = self.Object(m1, d, simFrame)
        Object2 = self.Object(m2, d, simFrame)
        
        gf = Object1.calcGravForce(simFrame)
        gp = Object1.calcGravPotential(simFrame)
        gfs1, gfs2 = Object1.calcGravFieldStrength(simFrame)
        v1, v2 = Object1.calcVelocity(gfs1, gfs2, simFrame)
        ke1, ke2 = Object1.calcKineticEnergy(v1, v2, simFrame)
        vol1, vol2 = Object1.calcVolume(simFrame)
        dens1, dens2 = Object1.calcDensity(vol1, vol2, simFrame)
        
        if scenario_choice == 0:
            None #do nothing
        elif scenario_choice == 1:
            d -= 1
        elif scenario_choice == 2:
            d -= 4
        elif scenario_choice == 3:
            d += 1
        elif scenario_choice == 4:
            d += 4
        elif scenario_choice == 5:
            m1 += 1
        elif scenario_choice == 6:
            m1 += 1
            m2 -= 1
        elif scenario_choice == 7:
            m1 += 1
            m2 += 1
        elif scenario_choice == 8:
            m1 -= 1
            m2 -= 1
        elif scenario_choice == 9:
            m1 += 1
            d -= 1
        elif scenario_choice == 10:
            m1 -= 1
            d += 1
        
        Distance_1.config(text = (d))
        Distance_2.config(text = (d))
        Mass_1.config(text = (m1))
        Mass_2.config(text = (m2))
        Velocity_1.config(text = round((v1*(10**9)),3))
        Velocity_2.config(text = round((v2*(10**9)),3))
        Grav_Force1.config(text = round((gf*(10**12)),3))
        Grav_Force2.config(text = round((gf*(10**12)),3))
        Grav_Pot1.config(text = round((gp*(10**12)),3))
        Grav_Pot2.config(text = round((gp*(10**12)),3))
        Grav_FS1.config(text = round((gfs1*(10**12)),3))
        Grav_FS2.config(text = round((gfs2*(10**12)),3))
        KE_1.config(text = round((ke1*(10**12)),3))
        KE_2.config(text = round((ke2*(10**12)),3))
        Volume_1.config(text = round((vol1),3))
        Volume_2.config(text = round((vol2),3))
        Density_1.config(text = round((dens1*(10**3)),3))
        Density_2.config(text = round((dens2*(10**3)),3))
        
        simFrame.after(int(round((1000/fps),0)))
        simFrame.update()
    
    def runSim(self, fpsSelect, m1Select, m2Select, dSelect, startButton, simFrame, main):
        global m1, m2, d, running
        
        m1Select.config(bg = "#555", fg = "white", state = "disabled")
        m2Select.config(bg = "#555", fg = "white", state = "disabled")
        dSelect.config(bg = "#555", fg = "white", state = "disabled")
        startButton.config(bg = "#555", fg = "white", state = "disabled")
        fpsSelect.config(bg = "#555", fg = "white", state = "disabled")
        
        stopButton = tk.Button(main, text = "STOP SIMULATION", bg = "red", fg = "white", relief = FLAT)
        stopButton.pack(side = LEFT, anchor = S, padx = 5, pady = 5)
        stopButton.config(command = lambda : self.stopSim(fpsSelect, m1Select, m2Select, dSelect, startButton, stopButton, simFrame, main))
        
        self.createTableOfValues(simFrame, main)
        
        while running == True:
            self.Update(simFrame)
            
            if m1 <= 0 or m2 <= 0 or d <= 0: # stops the sim if the masses become negative/0, or if distance becomes 0.
                running = False
                
            if running == False:
                self.stopSim(fpsSelect, m1Select, m2Select, dSelect, startButton, stopButton, simFrame, main)
            
    def stopSim(self, fpsSelect, m1Select, m2Select, dSelect, startButton, stopButton, simFrame, main):
        global running
        
        running = False
        stopButton.destroy()
        simFrame.delete("all")
        
        m1Select.config(bg = "#666", fg = "white", state = "normal")
        m2Select.config(bg = "#666", fg = "white", state = "normal")
        dSelect.config(bg = "#666", fg = "white", state = "normal")
        startButton.config(bg = "green", fg = "white", state = "normal")
        fpsSelect.config(bg = "#666", fg = "white", state = "normal")
        
        
        
def Run():
    sim = Window()
    
while __name__ == "__main__":
    Run()