# Totaram Ramrattan
# CS 370
# Wumpus World

#WumpusWorld-Square Module/Class
from WumpusWorldVars import *
from WumpusWorld import *


class Position:
    def __init__( self, x, y, p):
        self.x = x
        self.y = y
        self.visited=False
        self.percepts = []

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getPercepts(self):
        return self.percepts;

    def insertPercept(self,percept):
        self.percepts.append(percept)

    def setAsVisited(self):
        self.visited=True

    def insertAdjacents(self,percept, x, y, dim, world):
        #insert to right
        if x+1 < dim:
            position = world.getPosition(x+1,y)
            position.insertPercept(percept)
        #insert to left
        if x-1 > -1:
            position = world.getPosition(x-1,y)
            position.insertPercept(percept)
        #insert to top
        if y+1 < dim:
            position = world.getPosition(x,y+1)
            position.insertPercept(percept)
        #insert to bottom
        if y-1 > -1:
            position = world.getPosition(x,y-1)
            position.insertPercept(percept)

    def toString(self):
        return 'position:'+'('+str(self.getX())+', '+str(self.getY())+') :'+str(self.getPercepts())
