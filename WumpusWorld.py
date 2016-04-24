# Totaram Ramrattan
# CS 370
# Wumpus World

#WumpusWorld Module/Class

import random
from WumpusWorldVars import *
from Square import *

class WumpusWorld:
    def __init__(self,dim):
        self.dim = dim
        self.map = [[0]*dim for i in range(dim)]
        self.initWorld()

    def size(self):
        return self.dim*self.dim;

    def getCell(self,x,y):
        return self.map[x][y]


    def getRandCell(self):
        return self.map[random.randint(0,self.dim-1)]
        [random.randint(0,self.dim-1)]

    def placeGold(self):
        # cell = self.getRandCell()
        cell = self.getCell(1,1)
        cell.insertPercept(GOLD)

    def initWorld(self):
        #init all cells as safe
        for i in range(self.dim):
            for j in range(self.dim):
                self.map[i][j]= Sqaure(i,j,[SAFE]);
        #insert gold pile
        self.placeGold()
