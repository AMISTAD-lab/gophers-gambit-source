import simulation as s
from classTrap import *
from classTerrain import *

def simulate(intention, probreal, nTrapsWithoutFood=3):
    stillAlive = True
    trapsWithoutFood = 0
    numTraps = 0
    killedByHunger = False
    trapInfo = []
    while stillAlive:
        rowLength = 3 #generate randomly within a range
        colLength = 4
        functional = np.random.binomial(1, probreal)
        trap = Trap(rowLength, colLength, functional)
        ib, ac, gc, alive, eaten = s.simulateTrap(trap, intention)
        trapInfo.append([ib, ac, gc])
        #s.viewRun(ib, ac, gc)
        stillAlive = alive
        if alive:
            numTraps += 1
            if eaten:
                trapsWithoutFood = 0
            else:
                trapsWithoutFood += 1
            if trapsWithoutFood >= nTrapsWithoutFood:
                killedByHunger = True
                stillAlive = False
    return numTraps, killedByHunger, trapInfo





def test():
    terrain = Terrain(5,5)
    n, kh, trapinfo = simulate(False, 0, 3)
    terraininfo = [terrain.board, []]
    return trapinfo, terraininfo




def visualRun(rowLength, colLength, intention, trapList):
    trapInfo = []
    trapboardList = []
    for trap, x, y in trapList:
        ib, ac, gc, alive = s.simulateTrap(trap, intention, maxSteps=20)
        trapInfo.append([ib, ac, gc])
        trapboardList.append([ib, x, y])
    terrain = Terrain(rowLength, colLength, trapboardList)
    #create random walk frames
    gopherWalkCells = [] #NEED TO IMPLEMENT
    #####
    terrainInfo = [terrain.board, gopherWalkCells]
    return trapInfo, terrainInfo
