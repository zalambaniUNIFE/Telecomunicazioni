#CODA MM1 RIT

from threading import Thread
from queue import Queue
import threading, time, random, math
from tkinter import *
from tkinter import Tk, Canvas, PhotoImage
import ctypes
from pathlib import Path

ctypes.windll.shcore.SetProcessDpiAwareness(1)

codaPK = Queue() #coda che contiene i pachetti
tempoI = [] #il tempo quando viene inserito il tempo di entrata del PKT nel sistema
tempoS = [] #il tempo quando viene inserito il tempo di entrata del PKT nel servitore
tempoF = [] #il tempo quando viene eliminato il pachetto dal sistema
mediaC = [0] #pachetti in un determinato tempo nella coda
mediaS = [0] #pachetti in un determinato tempo nella sistema
servitorePieno = False #bool che determina quando il servitore è pieno
modificatore = 1

def setModi(val):
    global modificatore
    modificatore = val

def modi():
    global modificatore
    return modificatore

def mediaSistema():
    global mediaS
    return mediaS

def mediaCoda():
    global mediaC
    return mediaC

def tempoFine ():
    global tempoF
    return tempoF

def servitorePieno ():
    global servitorePieno
    return servitorePieno

def tempoServizio ():
    global tempoS
    return tempoS

def codaPK ():
    global codaPK
    return codaPK

def tempoInizio ():
    global tempoI
    return tempoI

def reset ():
    global codaPK
    global tempoI
    global tempoS
    global tempoF
    global mediaC
    global mediaS
    global servitorePieno
    codaPK = Queue()
    tempoI = []
    tempoS = []
    tempoF = []
    mediaC = [0]
    mediaS = [0]
    servitorePieno = False

def attendi (sec):
    time.sleep(sec*modificatore)

class generaPKG (Thread):
    def __init__(self, nome, alfa):
        Thread.__init__(self)
        self.nome = nome
        self.alf = alfa
        self.killed = False
    def run(self):
        global codaPK
        global tempoI
        print ("\n Thread '" + self.nome + "' inizio " + "per alfa: " + str(self.alf) + 'pkt/s')
        while not self.killed:
            lam = self.alf/(codaPK.qsize()+1)
            delta = random.expovariate(lam)
            attendi(delta)
            codaPK.put(1)
            tempoI.append(time.time())
    def kill(self):
        if self.is_alive():
            print ("\n Thread '" + self.nome + "' fine ")
        self.killed = True

class coda (Thread):
    def __init__(self, nome):
        Thread.__init__(self)
        self.nome = nome
        self.killed = False
    def run(self):
        global codaPK
        global mediaC
        global mediaS
        print ("\n Thread '" + self.nome + "' inizio ")
        while not self.killed:
            mediaC[0] += 1
            mediaS[0] += 1                
            mediaC.append(codaPK.qsize())
            mediaS.append(codaPK.qsize())
            if servitorePieno:
                mediaS[len(mediaS)-1] += 1
            attendi(0.001)
    def kill(self):
        if self.is_alive():
            print ("\n Thread '" + self.nome + "' fine ")
        self.killed = True
                  
class servitore (Thread):
    def __init__(self, nome, TassoMorte):
        Thread.__init__(self)
        self.nome = nome
        self.mu = TassoMorte
        self.killed = False
    def run(self):
        global codaPK
        global tempoF
        global tempoS
        global servitorePieno        
        print ("\n Thread '" + self.nome + "' inizio " + "per mu: " + str(self.mu) + 'pkt/s')
        while not self.killed:
            while codaPK.empty():
                pass
            servitorePieno = True
            data = codaPK.get()
            tempoS.append(time.time())
            delta = random.expovariate(self.mu)
            attendi(delta)
            tempoF.append(time.time())
            servitorePieno = False
    def kill(self):
        if self.is_alive():
            print ("\n Thread '" + self.nome + "' fine ")
        self.killed = True




class grafica (Thread):
    def __init__(self, nome, alfa, mu):
        Thread.__init__(self)
        self.nome = nome
        self.alpha = alfa
        self.mu = mu
        self.killed = False  
        
    def run(self):
        global codaPK
        global servitorePieno
        print ("\n Thread '" + self.nome + "' inizio ")
        window = Tk()
        window.attributes("-fullscreen",True)
        window.geometry('1920x1080+0+0')
        window.configure(bg = "#FFFFFF")
        window.title("Simulazione Grafica")
        window.protocol("WM_DELETE_WINDOW", self.kill)

        canvas = Canvas(window, bg = "#FFFFFF", height = 1080, width = 1920, bd = 0, highlightthickness = 0, relief = "ridge")
        canvas.place(x = 0, y = 0)

        canvas.create_text(
            430.0,
            106.0,
            anchor="nw",
            text="SIMULAZIONE VISIVA DI UN SISTEMA M/M/1 CON ARRIVI RALLENTATI",
            fill="#C22020",
            font=('RobotoRoman', 20, 'bold')
        )
        image_image_1 = PhotoImage(file=r"./frame0")
        canvas.create_image(
            960,
            450,
            image=image_image_1
        )

        canvas.create_text(
            710.0,
            580.0,
            anchor="nw",
            text="CODA",
            fill="#000000",
            font=('RobotoRoman', 20, 'bold')
        )

        canvas.create_text(
            1060.0,
            580.0,
            anchor="nw",
            text="SERVITORE",
            fill="#000000",
            font=('RobotoRoman', 20, 'bold')
        )

        canvas.create_text(
            900.0,
            700.0,
            anchor="nw",
            text="α = " + str(self.alpha) + 'pkt/s',
            fill="#000000",
            font=('RobotoRoman', 20, 'bold')
        )

        canvas.create_text(
            900.0,
            750.0,
            anchor="nw",
            text="μ = " + str(self.mu) + 'pkt/s',
            fill="#000000",
            font=('RobotoRoman', 20, 'bold')
        )

        while not self.killed:
            lengthC = codaPK.qsize()
            service = servitorePieno
            
            canvas.delete("pkt")
            if lengthC >= 0  and lengthC <= 24:
                coordX = 650
                coordY = 300
                for i in range(lengthC):
                    if (i == 8):
                        coordY-=40
                        coordX = 650
                    elif (i == 16):
                        coordY-=40
                        coordX = 650
                    elif (i == 24):
                        coordY-=40
                        coordX = 650
                    canvas.create_oval(coordX,coordY,coordX+30,coordY+30, outline="red", fill="red", width = 2, tags= "pkt")
                    coordX+=40
                    canvas.update()
            elif lengthC > 32:
                coordX = 500
                coordY = 300
                canvas.create_text(coordX,coordY,anchor="nw",text="Numero di pacchetti maggiore di 32",fill="red",font=('RobotoRoman', 20, 'bold'), tags="pkt")
                canvas.update()
                
            if servitorePieno >= 0:
                coordX = 1140
                coordY = 300
                for k in range(service):
                    canvas.create_oval(coordX,coordY,coordX+30,coordY+30, outline="blue", fill="blue", width = 2, tags= "pkt")
                    coordX+=40
                    canvas.update()
                
                canvas.update()
                #window.resizable(False, False)
            
            
            attendi(0.01)
        window.destroy()

    def kill(self):
        if self.is_alive():
            print ("\n Thread '" + self.nome + "' fine ")
        self.killed = True
