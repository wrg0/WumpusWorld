# Totaram Ramrattan
# CS 370
# Wumpus World

#WumpusWorld Module/Class

import random
import Tkinter as tk
from WumpusWorldVars import *
from Square import *
from PIL import Image, ImageTk

class Application(tk.Frame):
    def __init__(self, dim, master=None):
        tk.Frame.__init__(self, master, height=500,width=600,bg='#cccccc',pady=10,padx=10)
        self.grid_propagate(0)
        self.grid(padx=20,pady=20)
        self.dim=dim
        self.mapper = [[0]*dim for i in range(dim)]
        # create wumpus image
        wumpus_img=Image.open('./images/wumpus.gif')
        wumpus_img.thumbnail(img_size, Image.ANTIALIAS)
        self.wumpus_img = ImageTk.PhotoImage(wumpus_img)
        #create pit image
        pit_img=Image.open('./images/pit.gif')
        pit_img.thumbnail(img_size, Image.ANTIALIAS)
        self.pit_img = ImageTk.PhotoImage(pit_img)
        self.createWidgets()
        #create gold image
        gold_img=Image.open('./images/gold.gif')
        gold_img.thumbnail(img_size, Image.ANTIALIAS)
        self.gold_img = ImageTk.PhotoImage(gold_img)
        self.createWidgets()
        #create gold image
        hunter_img=Image.open('./images/hunter.png')
        hunter_img.thumbnail(img_size, Image.ANTIALIAS)
        self.hunter_img = ImageTk.PhotoImage(hunter_img)
        self.createWidgets()

    def createWidgets(self):
        for i in range(self.dim):
            for j in range(self.dim):
                tk.LabelFrame(self,height=80,width=80,bg='#ffffff').grid(row=i, column=j)
        self.startButton = tk.Button(self,text='Start',command='').grid(row=self.dim,column=0,pady=10)
        self.quitButton = tk.Button(self,text='Reset',command='').grid(row=self.dim,column=1,pady=10)
        self.startButton = tk.Button(self,text='Quit',command=self.quit).grid(row=self.dim,column=2,pady=10)


    def insertWidget(self, x, y, type):
        container = self.mapper[x][y]
        print ('(%i,%i)',x,y)
        if type == HUNTER:
            tk.Label(self,height=75,width=75,image=self.hunter_img).grid(row=x,column=y)
        elif type == WUMPUS:
            tk.Label(self,height=75,width=75,image=self.wumpus_img).grid(row=x,column=y)
        elif type == PIT:
            tk.Label(self,height=75,width=75,image=self.pit_img).grid(row=x,column=y)
        elif type == GOLD:
            tk.Label(self,height=75,width=75,image=self.gold_img).grid(row=x,column=y)


class WumpusWorld:

    def __init__(self,dim):
        self.dim = dim
        self.app = Application(dim);
        self.app.master.title("Wumpus World")
        self.map = [[0]*dim for i in range(dim)]
        self.initWorld()
        self.app.mainloop()

    def size(self):
        return self.dim*self.dim;

    def getCell(self,x,y):
        return self.map[x][y]


    def getRandCell(self):
        x=0
        y=0
        while (x == 0 and y == 0):
            x = random.randint(0,self.dim-1)
            y = random.randint(0,self.dim-1)
        print ('(%i,%i)',x,y)
        return self.map[x][y]

    def placeHunter(self,x,y):
        self.updateCellImage(x,y,HUNTER)

    def placeGold(self):
        cell = self.getRandCell()
        cell.insertPercept(GOLD)
        cell.insertAdjacents(GLITTER, cell.getX(),cell.getY(), self.dim, self)
        self.updateCellImage(cell.getX(), cell.getY(),GOLD)

    def placeWumpus(self):
        for i in range(self.dim-3):
            cell = self.getRandCell()
            cell.insertPercept(WUMPUS)
            cell.insertAdjacents(STENCH, cell.getX(),cell.getY(), self.dim, self)
            self.updateCellImage(cell.getX(), cell.getY(),WUMPUS)

    def placePit(self):
        for i in range(self.dim-2):
            cell = self.getRandCell()
            cell.insertPercept(PIT)
            cell.insertAdjacents(BREEZE, cell.getX(),cell.getY(), self.dim, self)
            self.updateCellImage(cell.getX(), cell.getY(),PIT)

    def updateCellImage(self,x,y,type):
        self.app.insertWidget(x,y,type)

    def initWorld(self):
        #init all cells as safe
        for i in range(self.dim):
            for j in range(self.dim):
                self.map[i][j]= Sqaure(i,j,[SAFE]);
        #insert gold pile
        self.placeGold()
        #insert pit
        self.placePit()
        #inser wumpus
        self.placeWumpus()
        #insert hunter
        self.placeHunter(0,0)
