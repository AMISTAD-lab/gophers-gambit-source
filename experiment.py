import simulation as s
import copy
from classTrap import *
from classTerrain import *
import numpy as np


def simulate(intention, probreal, nTrapsWithoutFood=3):
    stillAlive = True
    trapsWithoutFood = 0
    numTraps = 0
    killedByHunger = False
    trapInfo = []
    while stillAlive:
        rowLength = 3 #should generate randomly within a small range instead
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















def expectedLethality(rowLength, colLength, n, r):
    lethal = 0.0
    traps = trapEnumerator(rowLength, colLength, n)
    total = len(traps)
    runs = total*r
    trapInfo = []
    for i in range(total):
        for j in range(r):
            printProgressBar(i*r + j + 1, runs)
            ib, ac, gc, alive, eaten = s.simulateTrap(traps[i], False)
            if alive == False:
                lethal += 1
    print("\nlethal runs:", lethal, "\ntotal runs:", runs, "\nnum traps:", total)
    runs = float(runs)
    p = lethal / runs
    ci = 1.96*(p*(1-p))/runs
    p *= 100
    ci *= 100
    print("%s +/- %s" % (p, ci))
    return trapInfo


trapPieces = [Wire, Arrow, Floor]
rotationOptions = {
    Wire : [RotationType.up, RotationType.left, RotationType.right, RotationType.down],
    Arrow : [RotationType.up, RotationType.left, RotationType.right, RotationType.down],
    Floor : [RotationType.na],
}
thickOptions = {
    Wire : [ThickType.skinny, ThickType.normal, ThickType.wide],
    Arrow : [ThickType.skinny, ThickType.normal, ThickType.wide],
    Floor : [ThickType.na],
}
angleOptions = {
    Wire : [AngleType.straight, AngleType.lright], #excluding rright bc they're same for wires
    Arrow : [AngleType.lacute, AngleType.racute, AngleType.lright, AngleType.rright, AngleType.lobtuse, AngleType.robtuse],
    Floor : [AngleType.na],
}


def trapEnumerator(rowLength, colLength, n):
    trapPossibilities = enumeratorHelper(0, 0, rowLength, colLength, n)
    allTraps = []
    for trapPossibility in trapPossibilities:
        trap = Trap(rowLength, colLength, False)
        for i in range(len(trapPossibility)):
            cell = trapPossibility[i]
            cell.ownerBoard = trap
            trap.board[cell.y][cell.x] = cell
        allTraps.append(trap)
    return allTraps


def enumeratorHelper(x,y, rowLength, colLength, n):

    bottom_y = colLength - 1
    center_x = m.ceil(rowLength / 2) - 1
    center_y = m.ceil(colLength / 2) - 1

    cellPossibilities = []
    if x == center_x and y == bottom_y:
        cellPossibilities.append(Door(x, y, None))
    elif x == center_x and y == center_y:
        cellPossibilities.append(Food(x,y, None))
    elif x == center_x and y > center_y:
        cellPossibilities.append(Floor(x,y, None))
    else:
        for piece in trapPieces:
            for rotation in rotationOptions[piece]:
                for angle in angleOptions[piece]:
                    for thick in thickOptions[piece]:
                        cellPossibilities.append(piece(x, y, None, angleType=angle, rotationType=rotation, thickType=thick))

    next_x = x+1
    next_y = y
    if next_x == rowLength:
        next_x = 0
        next_y = y + 1

    if len(cellPossibilities) > n:
        cellPossibilities = np.random.choice(cellPossibilities, size=n, replace=False).tolist()
    
    if next_y == colLength:
        return copy.deepcopy([[cell] for cell in cellPossibilities])

    trapPossibilities = []
    for cell in cellPossibilities:
         for possibility in enumeratorHelper(next_x, next_y, rowLength, colLength, n):
             trapPossibilities.append(copy.deepcopy([cell] + possibility))

    return trapPossibilities





def printProgressBar (iteration, total, prefix = 'Progress:', suffix = 'Complete', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

