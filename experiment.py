import simulation as s
import copy
from classTrap import *
from classTerrain import *
import numpy as np
import magicVariables as mv
import data as d

pref = {
    "intention" : True, #if gopher has intention
    "defaultProbEnter" : 0.8, #probability of gopher entering trap (not intention)
    "probReal" : 0.5, #percentage of traps that are designed as opposed to random
    "nTrapsWithoutFood" : 3, #the amount of traps a gopher can survive without entering (due to starvation)
    "maxProjectileStrength" : 0.45, #thickWire strength
}



def runExperiment(filename, inputToVary, numSimulations):
    inputfile = createExpInputFile(inputToVary)
    seedList = createSeedListFromFile(inputfile)
    allData = simulateManySetups(numSimulations, seedList)
    d.allDataToCSV(allData, filename)



def createExpInputFile(inputToVary):
    """Inputs:
        inputToVary: String, the input to vary. 
            eg. "predSightDistance"
        startValue: the starting value of input, inclusive
        endingValue: the ending value of input, inclusive
        stepValue: the stepValue for input
    """
    filename = "experimentInput.txt"
    file = open(filename, "w")
    for intention in [True, False]:
        toWrite = "intention " + str(intention) + "\n" 
        if inputToVary == "probReal":
            for percent in range(0, 100+1, 5):
                percent /= 100
                file.write(toWrite)
                file.write("probReal " + str(percent) + "\n\n")
        elif inputToVary == "nTrapsWithoutFood":
            for n in range(1, 20+1, 1):
                file.write(toWrite)
                file.write("nTrapsWithout Food " + str(n) + "\n\n")
        elif inputToVary == "maxProjectileStrength":
            for probKill in range(3, 99+1, 6):
                probKill /= 100
                file.write(toWrite)
                file.write("maxProjectileStrength " + str(probKill) + "\n\n")
        elif inputToVary == "defaultProbEnter":
            for probEnter in range(0, 100+1, 5):
                probEnter /= 100
                file.write(toWrite)
                file.write("defaultProbEnter " + str(probEnter) + "\n\n")
        else:
            raise Exception("Something went wrong")
    file.close() 
    return filename


def createSeedListFromFile(filename):
    seedFile = open(filename, "r")
    lineList = seedFile.readlines()
    seedFile.close()
    lineList = [x.strip("\n") for x in lineList]
    lineList = lineList[:-1] # crop out extra line in file (hacky ik)

    standardSeed = {
        "intention" : True,
        "defaultProbEnter" : 1,
        "probReal" : 0,
        "nTrapsWithoutFood" : 3,
        "maxProjectileStrength" : 0.45,
    }

    seedList = []
    preferences = copy.deepcopy(standardSeed)
    for line in lineList:
        if line == "":
            seedList.append(preferences)
            preferences = copy.deepcopy(standardSeed)
        else:
            key, value = line.split()
            if key in preferences:
                if value == "True":
                    preferences[key] = True
                elif value == "False":  
                    preferences[key] = False
                else:
                    preferences[key] = float(value)
            else:
                raise Exception(key + " is not a value in preferences!")
    seedList.append(preferences)
    return seedList


def simulateManySetups(numSimulations, seedList):
    allData = []
    numSeeds = len(seedList)
    for i in range(numSeeds):
        allData.append(batchSimulate(numSimulations, seedList[i], [True, i, numSeeds]))
    return allData


def batchSimulate(numSimulations, pref, manySetups=[False,0,0]):
    """runs simulate many times"""
    batchData = copy.deepcopy(pref) # holds runData, as well as averages for each set of parameters
    runsData = [] # holds data dictionaries for runs with a given set of parameters. (greater number of runs = greater precision)
    for i in range(numSimulations):
        data, trapInfo = simulate(pref)
        runsData.append(data)
        if manySetups[0]:
            printProgressBar((i+1) + (manySetups[1] * numSimulations), numSimulations * manySetups[2])
    batchData["runsData"] = runsData 
    return batchData

def simulate(pref):
    intention = pref["intention"]
    probReal = pref["probReal"]
    nTrapsWithoutFood = pref["nTrapsWithoutFood"]

    mv.initializeVariables(pref)

    stillAlive = True
    trapsWithoutFood = 0
    numTraps = 0
    killedByHunger = False
    trapInfo = []
    while stillAlive:
        rowLength = 3
        colLength = 4
        functional = np.random.binomial(1, probReal)
        trap = Trap(rowLength, colLength, functional)
        ib, ac, gc, alive, eaten = s.simulateTrap(trap, intention)
        trapInfo.append([ib, ac, gc])
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
    
    data = copy.deepcopy(pref)
    data["numTraps"] = numTraps
    data["killedByHunger"] = killedByHunger
    return data, trapInfo






def expectedLethality(rowLength, colLength, n, r):
    lethal = 0.0
    traps = trapEnumerator(rowLength, colLength, n)
    total = len(traps)
    runs = total*r
    trapInfo = []
    for i in range(total):
        for j in range(r):
            printProgressBar(i*r + j + 1, runs)
            ib, ac, gc, alive, eaten = s.simulateTrap(traps[i], True)
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

