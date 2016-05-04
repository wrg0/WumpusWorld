#Knowledgebase Class
from Sentence import *
from WumpusWorldVars import *

class KnowledgeBase():

    #constructer
    def __init__(self,dim):
        self.dim = dim
        self.models = [[None]*dim for i in range(dim)]
        for i in range(dim):
            for j in range(dim):
                self.models[i][j] = Sentence()

    def tell(self,x,y,statements):
            model = self.models[x][y]
            # ['stench','breeze']
            for p in statements:

                if p == WUMPUS:
                    model.wumpus = True
                elif p == STENCH:
                    model.stench = True
                elif p == PIT:
                    model.pit = True
                elif p == BREEZE:
                    model.breeze = True
                elif p == GOLD:
                    model.gold == True
                elif p == GLITTER:
                    model.glitter = True
                elif p == KILLED_WUMPUS:
                    model.wumpus = False
                    model.visited = True

            print 'told kb:({},{}) {}'.format(x,y,self.models[x][y].toString())

    def ask(self,current, next, compass):

        cX = current[0]
        cY = current[1]
        nX = next[0]
        nY = next[1]

        # models
        cModel = self.models[cX][cY]
        nModel = self.models[nX][nY]

        # check if nModel is safe or unknown if safe
        if nModel.wumpus == False:
            return True

        if not cModel.breeze and not cModel.stench:
            return True

        nLeft = None
        nRight = None

        if compass == 'N':

            #next left & right
            if nX+1 < self.dim:
                nRight = self.models[nX+1][nY]
            else:
                nRight = None
            if nX-1 > 0:
                nLeft = self.models[nX-1][nY]
            else:
                nLeft = None

        if compass == 'S':

            #next right & left
            if nX-1 > 0:
                nRight = self.models[nX-1][nY]
            else:
                nRight = None

            if nX+1 < self.dim:
                nLeft = self.models[nX+1][nY]
                nLpos = [nX+1,nY]
            else:
                nLeft = None

        if compass == 'E':

            if nY-1 > 0:
                nRight = self.models[nX][nY-1]
            else:
                cRight = None

            if nY+1 < self.dim:
                nLeft = self.models[nX][nY+1]
            else:
                nLeft = None


        if compass == 'W':

            if nY+1 < self.dim:
                nRight = self.models[nX][nY+1]
            else:
                nRight = None

            if cY-1 > 0:
                cLeft = self.models[cX][cY-1]
            else:
                cLeft = None


        if cModel.stench == True and nModel.wumpus == None:

            # no wall to left of right
            if nRight != None and nLeft != None:
                if nRight.stench == True or nLeft.stench == True:
                    print 'wumpus in: {}, {}'.format(nX,nY)
                    return WUMPUS
            # to right is wall
            elif nLeft != None and nRight == None:
                if nLeft.stench == True:
                    print 'wumpus in: {}, {}'.format(nX,nY)
                    return WUMPUS
            # to left is wall
            elif nRight != None and nLeft == None:
                if nRight.stench == True:
                    print 'wumpus in: {}, {}'.format(nX,nY)
                    return WUMPUS


        #check for pit and wumpus
        #visited both next left and right
        elif nLeft != None and nRight != None:
            if nLeft.visited and nRight.visited\
            and (not nLeft.stench) and (not nRight.stench)\
            and (not nLeft.breeze) and (not nRight.breeze):
                return True
            elif nLeft.visited and nRight.visited\
            and nLeft.breeze and nRight.breeze:
                nModel.visited = True
                nModel.pit = True
                return False
            elif nLeft.visited and nRight.visited\
            and nLeft.stench and nRight.stench:
                nModel.visited = True
                nModel.wumpus = True
                print 'wumpus in: {}, {}'.format(nX,nY)
                return False

        # visited left and nRight is wall
        elif nLeft != None and nRight == None:
            if nLeft.visited\
            and (not nLeft.stench) and (not nLeft.breeze):
                return True
            elif nLeft.visited and nLeft.breeze:
                nModel.visited = True
                nModel.pit = True
                return False
            elif nLeft.visited and nLeft.stench:
                nModel.visited = True
                nModel.wumpus = True
                print 'wumpus in: {}, {}'.format(nX,nY)
                return False

        # visited right and nLeft is wall
        elif nRight != None and nLeft == None:
            if nRight.visited\
            and (not nRight.stench) and (not nRight.breeze):
                return True
            elif nRight.visited and nRight.breeze:
                nModel.visited = True
                nModel.pit = True
                return False
            elif nRight.visited and nRight.stench:
                nModel.visited = True
                nModel.wumpus = True
                print 'wumpus in: {}, {}'.format(nX,nY)
                return False




        return False
