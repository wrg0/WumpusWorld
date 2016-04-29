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

            print 'told kb: {}'.format(self.models[x][y].toString())

    def ask(self,current, next, compass):

        cX = current[0]
        cY = current[1]
        nX = next[0]
        nY = next[1]

        # models
        cModel = self.models[cX][cY]
        nModel = self.models[nX][nY]

        # check if nModel is not safe or unknown if safe
        if not cModel.breeze and not cModel.stench:
            return True
        else:
            print 'unknown, performing model enumeration...'

        cLeft=None
        cRight = None

        nLeft = None
        nRight = None

        bottom = None
        bLeft = None
        bRight = None

        if compass == 'N':

            #bottom
            if cY-1 > 0:
                bottom = self.models[cX][cY-1]
            else:
                bottom = None

            #bottom left
            if cY-1 > 0 and cX-1  > 0:
                bLeft = self.models[cX-1][cY-1]
            else:
                bLeft = None

            #bottom right
            if cY-1 > 0 and cX+1 < self.dim:
                bRight = self.models[cX+1][cY-1]

            #left
            if cX-1 > 0:
                cLeft = self.models[cX-1][cY]
            else:
                cLeft = None

            if nX-1 > 0:
                nLeft = self.models[nX-1][nY]
            else:
                nLeft = None

            #right
            if cX+1 < self.dim:
                cRight = self.models[cX+1][nY]
            else:
                cRight = None

            if nX+1 < self.dim:
                nRight = self.models[nX+1][nY]
            else:
                nRight = None


        if compass == 'S':

            #front
            if nY-1 > 0:
                front = self.models[nX][nY-1]

            #bottom
            if cY+1 < self.dim:
                bottom = self.models[cX][cY+1]
            else:
                bottom = None

            #bottom left
            if cY-1 > 0 and cX-1 > 0:
                bLeft = self.models[cX-1][cY-1]
            else:
                bLeft = None

            #bottom right
            if cY+1 < self.dim and cX-1 > 0:
                bRight = self.models[cX-1][cY+1]

            #left
            if cX+1 < self.dim:
                cLeft = self.models[cX+1][cY]
            else:
                cLeft = None

            if nX+1 < self.dim:
                nLeft = self.models[nX+1][nY]
            else:
                nLeft = None

            #right
            if cX-1 > 0:
                cRight = self.models[cX-1][cY]
            else:
                cRight = None

            if nX-1 > 0:
                nRight = self.models[nX-1][nY]
            else:
                nRight = None


        if compass == 'E':

            #front
            if nX+1 < self.dim:
                front = self.models[nX+1][nY]

            #bottom
            if cX-1 > 0:
                bottom = self.models[cX-1][cY]
            else:
                bottom = None



            #left
            if cY-1 > 0:
                cLeft = self.models[cX][cY-1]
            else:
                cLeft = None

            if nY-1 > 0:
                nRight = self.models[nX][nY-1]
            else:
                cRight = None

            #right
            if cY+1 < self.dim:
                cRight = self.models[cX][cY+1]
            else:
                cRight = None

            if nY+1 < self.dim:
                nRight = self.models[nX][nY+1]
            else:
                nRight = None

        if compass == 'W':

            #front
            if nX - 1 > 0:
                front = self.models[nX-1][nY]

            #bottom
            if cX+1 < self.dim:
                bottom = self.models[cX+1][cY]
            else:
                bottom = None

            #bottom left
            if cY+1 < self.dim and cX+1 < self.dim:
                bLeft = self.models[cX+1][cY+1]
            else:
                bLeft = None

            #bottom right
            if cY-1 > 0 and cX+1 < self.dim:
                bRight = self.models[cX+1][cY-1]

            #left
            if cY+1 < self.dim:
                cLeft = self.models[cX][cY+1]
            else:
                cLeft = None

            if nY+1 < self.dim:
                nRight = self.models[nX][nY+1]
            else:
                cRight = None

            #right
            if cY-1 > 0:
                cRight = self.models[cX][cY-1]
            else:
                cRight = None

            if nY-1 > 0:
                nRight = self.models[nX][nY-1]
            else:
                nRight = None

        #check for pit
        # [][][~]
        # [][C][?]
        # [][][~]
        if nLeft != None and nRight != None:
            if nLeft.visited and nRight.visited\
            and (not nLeft.stench) and (not nRight.stench)\
            and (not nLeft.breeze) and (not nRight.breeze):
                return True

        return False
