# Wumpus world [5][5]
# [0][0] = start point, no pits
# breeze on adject sqaure of pits
# 1 square has a gorl bar
# 1 sqaure has wumpus
# can shoot a wumpus only if wumpus is facing you
# move left right forward

import sys
import Tkinter as tk
from WumpusWorld import *

class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)
        self.grid(column=5)
        self.squares = [[0]*5 for i in range(5)]
        self.createView()

    def createView(self):
        for i in range(5):
            for j in range(5):
                parent = tk.Frame(height=62,width=62,bg='#ffffff').grid(row=i,column=j)
                self.squares[i]=tk.Frame(parent,height=60,width=60,bd=2, bg='#000000')

        # self.quiteButton = tk.Button(height=2,width=4,text='quite',command=self.quit)
        # self.quiteButton.grid(row=6,column=3)

    def helloWorld(self):
        print 'hello wumpus world'

def main():
    world = WumpusWorld(5);

    x=0
    y=0
    cell1 = world.getCell(x,y);
    print cell1.toString()

    #to right
    cell2 = world.getCell(x+1,y);
    print 'right: '+cell2.toString()

    #to left
    cell2 = world.getCell(x-1,y);
    print 'left: '+cell2.toString()

    # top of
    cell2 = world.getCell(x,y+1);
    print 'top: '+cell2.toString()

    #botom of
    cell2 = world.getCell(x,y-1);
    print 'bottom: '+cell2.toString()

    #build gui
    app = Application();
    app.mainloop()


main()
