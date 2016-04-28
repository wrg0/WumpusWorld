# Totaram Ramrattan
# CS 370
# Wumpus World

#WumpusWorld Module/Class

import random
import Tkinter as tk
from WumpusWorldVars import *
from Position import *
from PIL import Image, ImageTk
from Player import *


class WumpusWorld:

    def __init__(self,dim):
        self.dim = dim
        app = tk.Tk()
        #insert Buttons
        self.startButton = tk.Button(app,text='run',command='')
        self.startButton.grid_propagate(0)
        self.startButton.grid(pady=10, padx=5, row=0, column=0)

        self.stepButton = tk.Button(app,text='step',command=self.step)
        self.stepButton.grid_propagate(0)
        self.stepButton.grid(pady=10, padx=5, row=0, column=1)

        self.resetButton = tk.Button(app,text='reset',command=self.resetWorld)
        self.resetButton.grid_propagate(0)
        self.resetButton.grid(pady=10, padx=5, row=0, column=2)

        self.quitButton = tk.Button(app,text='quit',command=app.quit)
        self.quitButton.grid_propagate(0)
        self.quitButton.grid(pady=10, padx=5, row=0, column=4)

        self.app= app;
        self.initContainer()

    def initContainer(self):
        #insert container frame
        app = self.app
        self.container=tk.Frame(app,width=450,height=460,bg='#ffffff')
        self.container.grid_propagate(0)
        self.container.grid(row=1,columnspan=5,pady=5,padx=5)

        #create images
        self.createImages()
        self.createWidgets(self.container)
        self.initWorld()
        self.app.mainloop()

    def resetWorld(self):
        self.container.grid_remove()
        self.initContainer()

    def size(self):
        return self.dim*self.dim;

    def getposition(self,x,y):
        return self.map[x][y]


    def getRandposition(self):
        x=0
        y=0
        while (x == 0 and y == 0):
            x = random.randint(0,self.dim-1)
            y = random.randint(0,self.dim-1)
        return self.map[x][y]

    def placeHunter(self,x,y):
        percepts = self.getposition(x,y)
        print 'percepts: '+percepts.toString()
        self.hunterLoc = [x,y]
        self.updatepositionImage(x,y,HUNTER)

    def placeGold(self):
        position = self.getRandposition()
        position.insertPercept(GOLD)
        position.insertAdjacents(GLITTER, position.getX(),position.getY(), self.dim, self)
        self.updatepositionImage(position.getX(), position.getY(),GOLD)

    def placeWumpus(self):
        position = self.getRandposition()
        position.insertPercept(WUMPUS)
        position.insertAdjacents(STENCH, position.getX(),position.getY(), self.dim, self)
        self.updatepositionImage(position.getX(), position.getY(),WUMPUS)

    def placePit(self):
        for i in range(self.dim-2):
            position = self.getRandposition()
            position.insertPercept(PIT)
            position.insertAdjacents(BREEZE, position.getX(),position.getY(), self.dim, self)
            self.updatepositionImage(position.getX(), position.getY(),PIT)

    def updatepositionImage(self,x,y,type):
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

        print 'inserting: {} : ({},{})'.format(type,x,y)
        if type == HUNTER:
            self.mapper[x][y]=tk.Label(self.container,height=75,width=75,image=self.hunter_img)
            self.mapper[x][y].grid(row=x,column=y)
        elif type == WUMPUS:
            self.mapper[x][y]=tk.Label(self.container,height=75,width=75,image=self.wumpus_img)
            self.mapper[x][y].grid(row=x,column=y)
        elif type == PIT:
            self.mapper[x][y]=tk.Label(self.container,height=75,width=75,image=self.pit_img)
            self.mapper[x][y].grid(row=x,column=y)
        elif type == GOLD:
            self.mapper[x][y]=tk.Label(self.container,height=75,width=75,image=self.gold_img)
            self.mapper[x][y].grid(row=x,column=y)

    def initWorld(self):
        dim = self.dim
        self.map = [[0]*dim for i in range(dim)]
        self.mapper = [[0]*dim for i in range(dim)]

        #init all positions as safe
        for i in range(self.dim):
            for j in range(self.dim):
                self.map[i][j]= Position(i,j,[]);
        #insert gold pile
        self.placeGold()
        #insert pit
        self.placePit()
        #inser wumpus
        self.placeWumpus()
        #insert hunter
        self.placeHunter(0,0)
        #init player
        self.player = Player()


    def step(self):
        x=self.hunterLoc[0]
        y=self.hunterLoc[1]
        percepts = self.getposition(x,y)
        self.mapper[x][y].grid_remove()
        self.mapper[x][y]=None
        move = self.player.nextMove(x,y,self.dim)
        self.placeHunter(move[0],move[1])
