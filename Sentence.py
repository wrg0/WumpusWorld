class Sentence():
    def __init__(self):
        self.wumpus = None
        self.stench = None
        self.pit = None
        self.breeze = None
        self.gold= None
        self.glitter = None

    def toString(self):
        return 'wumpus:{}, stench:{}, pit:{}, breeze:{}, gold:{}, glitter:{}'\
        .format(self.wumpus,self.stench,self.pit\
        ,self.breeze,self.gold,self.glitter)
