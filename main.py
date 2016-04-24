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
    cell = world.getCell(4,4);
    print cell.toString()


main()
