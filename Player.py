import random

class Player():
    def __init__(self):
        self.NSEW = ['W','N','E','S']
        self.directions = ['L','R']
        self.compass = self.NSEW[random.randint(0,3)]
        self.direction = self.directions[random.randint(0,1)]
        self.arrows = 1
        self.steps = []
        #if visited and no gold mark safe
        #heck if visited 

    def turn(self, LR ):
        if LR == 'L':
            self.compass = self.NSEW[self.NSEW.index(self.compass)-1]
        else:
            if self.NSEW.index(self.compass) == len(self.NSEW)-1:
                self.compass = self.NSEW[0]
            else:
                self.compass = self.NSEW[self.NSEW.index(self.compass)+1]

    def getDirection(self):
        return self.direction

    def shoot(self):
        if self.arrows > 0:
            self.arrows = self.arrows-1;

    def nextMove(self,x,y,dim):
        #if compass is N move up 1
        direction = []
        if self.compass == 'N':
            y+=1
        elif self.compass == 'S':
            y-=1
        elif self.compass == 'E':
            x+=1
        elif self.compass == 'W':
            x-=1

        #check for wall
        if x < 0 or x >= dim or y < 0 or y >= dim:
            self.turn(self.directions[random.randint(0,1)])
            if x < 0:
                x+=1
            elif x >= dim:
                x-=1
            elif y < 0:
                y+=1
            else:
                y-=1

            direction = self.nextMove(x,y,dim)
        else:
            direction = [x,y]

        return direction
