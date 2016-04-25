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
        tk.Frame.__init__(self, master, height=600,width=760)
        self.grid_propagate(0)
        self.grid(padx=20,pady=20)
        self.dim=dim
        self.mapper = [[0]*dim for i in range(dim)]
        # create wumpus image
        wumpus_img=Image.open('./images/wumpus.gif')
        wumpus_img.thumbnail(img_size, Image.ANTIALIAS)
        self.wumpus_img = ImageTk.PhotoImage(wumpus_img)
        self.createWidgets()

    def createWidgets(self):
        for i in range(self.dim):
            for j in range(self.dim):
                tk.LabelFrame(self,height=80,width=80,bg='#000000').grid(row=i, column=j)
        self.quitButton = tk.Button(self,text='Quit',command=self.quit).grid(row=self.dim+1,pady=10)
    def insertWidget(self, x, y, type):
        container = self.mapper[x][y]
        print ('(%i,%i)',x,y)
        if type == WUMPUS:
            tk.Label(self,height=80,width=80,image=self.wumpus_img).grid(row=x,column=y)


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
        return self.map[random.randint(0,self.dim-1)][random.randint(0,self.dim-1)]

    def placeGold(self):
        cell = self.getRandCell()
        cell.insertPercept(GOLD)
        cell.insertAdjacents(GLITTER, cell.getX(),cell.getY(), self.dim, self)

    def placeWumpus(self):
        cell = self.getRandCell()
        cell.insertPercept(WUMPUS)
        cell.insertAdjacents(STENCH, cell.getX(),cell.getY(), self.dim, self)
        self.updateCellImage(cell.getX(), cell.getY(),WUMPUS)

    def placePit(self):
        cell = self.getRandCell()
        cell.insertPercept(PIT)
        cell.insertAdjacents(BREEZE, cell.getX(),cell.getY(), self.dim, self)

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
