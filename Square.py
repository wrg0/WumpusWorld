# Totaram Ramrattan
# CS 370
# Wumpus World

#WumpusWorld-Square Module/Class
PIT = 'pit';
WUMPUS = 'wumpus'
BREEZE = 'breeze'
GOLD = 'gold'
GLITTER = 'glitter'
SAFE = 'safe'

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

    def insertPercept(percept):
        if percept == PIT:
            for i in range(len(self.percepts)):
                if self.percepts[i] == SAFE :
                    self.percepts = self.percepts[0:i]+self.percepts[i+1:len(self.percepts)]
                    
        self.percepts.append(percept)

    def insertAdjacents(self, x, y, dim, world):

        #insert to right
        if x+1 < dim:
            world.getCell(x+1,y).insertPercept(percept)

        #insert to left
        if x-1 >= 0:
            if percept != 'pit':
                world.getCell(x-1,y).insertPercept(percept)
            elif x-1 !=0:
                world.getCell(x-1,y).insertPercept(percept)

        #insert to bottom
        if y-1 >= 0:
            if percept != 'pit':
                world.getCell(x,y-1).insertPercept(percept)
            elif y-1 != 0:
                world.getCell(x,y-1).insertPercept(percept)

        #insert to top
        if y+1 < dim:
            world.getCell(x,y-1).insertPercept(percept)




    def toString(self):
        return 'cell:'+'('+str(self.getX())+', '+str(self.getY())+') :'+str(self.getPercepts())
