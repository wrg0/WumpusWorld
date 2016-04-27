# Totaram Ramrattan
# CS 370
# Wumpus World

#WumpusWorld Module/Class

import random
import Tkinter as tk
from WumpusWorldVars import *
from Square import *
from PIL import Image, ImageTk


class WumpusWorld:

    def __init__(self,dim):
        self.dim = dim
        self.app = tk.Tk()
        self.initContainer()

    def initContainer(self):
        #insert container frame
        app = self.app

        self.container=tk.Frame(app,width=600,height=460,bg='#ffffff')
        self.container.grid_propagate(0)
        self.container.grid(row=1,columnspan=5,pady=5,padx=5)
        #insert Buttons
        self.startButton = tk.Button(app,text='run',command='')
        self.startButton.grid_propagate(0)
        self.startButton.grid(pady=10, padx=10, row=0, column=0)

        self.stepButton = tk.Button(app,text='step',command='')
        self.stepButton.grid_propagate(0)
        self.stepButton.grid(pady=10, padx=10, row=0, column=1)

        self.resetButton = tk.Button(app,text='reset',command='')
        self.resetButton.grid_propagate(0)
        self.resetButton.grid(pady=10, padx=10, row=0, column=2)

        self.quitButton = tk.Button(app,text='quit',command=app.quit)
        self.quitButton.grid_propagate(0)
        self.quitButton.grid(pady=10, padx=10, row=0, column=3,columnspan=2)

        #create images
        self.createImages()
        self.createWidgets(self.container)
        self.initWorld()
        self.app.mainloop()

    def resetWorld(self):
        initContainer()
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
        self.insertWidget(x,y,type)

    def createWidgets(self,container):
        for i in range(self.dim):
            for j in range(self.dim):
                tk.LabelFrame(container,height=90,width=90,bg='#ffffff').grid(row=i, column=j)

    def createImages(self):

        wumpus_img=Image.open('./images/wumpus.gif')
        wumpus_img.thumbnail(img_size, Image.ANTIALIAS)
        self.wumpus_img = ImageTk.PhotoImage(wumpus_img)
        #create pit image
        pit_img=Image.open('./images/pit.gif')
        pit_img.thumbnail(img_size, Image.ANTIALIAS)
        self.pit_img = ImageTk.PhotoImage(pit_img)
        #create gold image
        gold_img=Image.open('./images/gold.gif')
        gold_img.thumbnail(img_size, Image.ANTIALIAS)
        self.gold_img = ImageTk.PhotoImage(gold_img)
        #create gold image
        hunter_img=Image.open('./images/hunter.gif')
        hunter_img.thumbnail(img_size, Image.ANTIALIAS)
        self.hunter_img = ImageTk.PhotoImage(hunter_img)


    def insertWidget(self, x, y, type):
        container = self.mapper[x][y]
        print ('(%i,%i)',x,y)
        if type == HUNTER:
            tk.Label(self.container,height=75,width=75,image=self.hunter_img).grid(row=x,column=y)
        elif type == WUMPUS:
            tk.Label(self.container,height=75,width=75,image=self.wumpus_img).grid(row=x,column=y)
        elif type == PIT:
            tk.Label(self.container,height=75,width=75,image=self.pit_img).grid(row=x,column=y)
        elif type == GOLD:
            tk.Label(self.container,height=75,width=75,image=self.gold_img).grid(row=x,column=y)

    def initWorld(self):
        dim = self.dim
        self.map = [[0]*dim for i in range(dim)]
        self.mapper = [[0]*dim for i in range(dim)]

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
