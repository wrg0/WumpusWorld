# Totaram Ramrattan
# CS 370
# Wumpus World

#WumpusWorld-Square Module/Class
from WumpusWorldVars import *
from WumpusWorld import *


class Sqaure:
    def __init__( self, x, y, p):
        self.x = x
        self.y = y
        self.percepts = p

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getPercepts(self):
        return self.percepts;

    def insertPercept(self,percept):
        if percept == PIT or percept == WUMPUS:
            for i in range(len(self.percepts)):
                if self.percepts[i] == SAFE:
                    self.percepts = self.percepts[0:i]+self.percepts[i:len(self.percepts)]
                    break

        self.percepts.append(percept)

    def insertAdjacents(self,percept, x, y, dim, world):
        #insert to right
        if x+1 < dim:
            cell = world.getCell(x+1,y)
            cell.insertPercept(percept)
        #insert to left
        if x-1 > -1:
            cell = world.getCell(x-1,y)
            cell.insertPercept(percept)
        #insert to top
        if y+1 < dim:
            cell = world.getCell(x,y+1)
            cell.insertPercept(percept)
        #insert to bottom
        if y-1 > -1:
            cell = world.getCell(x,y-1)
            cell.insertPercept(percept)

    def toString(self):
        return 'cell:'+'('+str(self.getX())+', '+str(self.getY())+') :'+str(self.getPercepts())
