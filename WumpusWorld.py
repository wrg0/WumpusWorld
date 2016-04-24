# Totaram Ramrattan
# CS 370
# Wumpus World

#WumpusWorld Module/Class

import random

class WumpusWorld:
    def __init__(self,dim):
        self.dim = dim
        self.map = [[0]*dim for i in range(dim)]
        self.initWorld()

    def size(self):
        return self.dim*self.dim;

    def getCell(self,x,y):
        return self.map[x][y][0]


    def getRandCell(self):
        return self.map[random.randint(0,self.dim)][random.randint(0,self.dim)]

    def placeGold(self):
        cell = self.getRandCell()


    def initWorld(self):

        #init all cells as safe
        for i in range(self.dim):
            for j in range(self.dim):
                self.map[i][j]=['safe'];


        #place pit
        cell = self.getRandCell()
