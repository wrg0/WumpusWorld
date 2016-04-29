#Knowledgebase Class
from Sentence import *
from WumpusWorldVars import *

class KnowledgeBase():

    #constructer
    def __init__(self,dim):
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
