# Wumpus world [5][5]
# [0][0] = start point, no pits
# breeze on adject sqaure of pits
# 1 square has a gorl bar
# 1 sqaure has wumpus
# can shoot a wumpus only if wumpus is facing you
# move left right forward

import sys
from WumpusWorld import *

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

main()
