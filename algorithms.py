from typeRotation import *
from typeDirection import *
from typeAngle import *
from typeCell import *
from typeThick import *
import classCell as c
import numpy as np
import copy
import csv
import math as m

def findDir(rotationType, angleType):
    """returns the direction from our perspective (primarily for the arrow)"""

    if(rotationType == RotationType.left):
        if(angleType == AngleType.lacute):
            return DirectionType.lowerright 
        elif(angleType == AngleType.racute):
            return DirectionType.upperright
        elif(angleType == AngleType.lright):
            return DirectionType.down
        elif(angleType == AngleType.rright):
            return DirectionType.up
        elif(angleType == AngleType.lobtuse):
            return DirectionType.lowerleft
        elif(angleType == AngleType.robtuse):
            return DirectionType.upperleft
        elif(angleType == AngleType.straight):
            return DirectionType.left
        else:
            raise Exception("uh oh, either angleType is NA or arrow is somehow going in a straight line :O")
    
    elif(rotationType == RotationType.right): 
        if(angleType == AngleType.lacute):
            return DirectionType.upperleft
        elif(angleType == AngleType.racute):
            return DirectionType.lowerleft
        elif(angleType == AngleType.lright):
            return DirectionType.up
        elif(angleType == AngleType.rright):
            return DirectionType.down
        elif(angleType == AngleType.lobtuse):
            return DirectionType.upperright
        elif(angleType == AngleType.robtuse):
            return DirectionType.lowerright
        elif(angleType == AngleType.straight):
            return DirectionType.right
        else:
            raise Exception("uh oh, either angleType is NA or arrow is somehow going in a straight line :O")

    elif(rotationType == RotationType.up): 
        if(angleType == AngleType.lacute):
            return DirectionType.lowerleft
        elif(angleType == AngleType.racute):
            return DirectionType.lowerright
        elif(angleType == AngleType.lright):
            return DirectionType.left
        elif(angleType == AngleType.rright):
            return DirectionType.right
        elif(angleType == AngleType.lobtuse):
            return DirectionType.upperleft
        elif(angleType == AngleType.robtuse):
            return DirectionType.upperright
        elif(angleType == AngleType.straight):
            return DirectionType.up
        else:
            raise Exception("uh oh, either angleType is NA or arrow is somehow going in a straight line :O")

    elif(rotationType == RotationType.down):
        if(angleType == AngleType.lacute):
            return DirectionType.upperright
        elif(angleType == AngleType.racute):
            return DirectionType.upperleft
        elif(angleType == AngleType.lright):
            return DirectionType.right
        elif(angleType == AngleType.rright):
            return DirectionType.left
        elif(angleType == AngleType.lobtuse):
            return DirectionType.lowerright
        elif(angleType == AngleType.robtuse):
            return DirectionType.lowerleft
        elif(angleType == AngleType.straight):
            return DirectionType.down
        else:
            raise Exception("uh oh, either angleType is NA or arrow is somehow going in a straight line :O")


def formatMatrix(matrix):  
    string = ""
    colLength = len(matrix)
    rowLength = len(matrix[0])
    for y in range(colLength):
        for x in range(rowLength):
            string += str(matrix[y][x]) + "\t"
        string += "\n\n\n"
    return string

def flatten(l):
    return [item for sublist in l for item in sublist]


def rotateInitialBoard(initialboard):
    initialboard = copy.deepcopy(initialboard)
    colLength = len(initialboard)
    rowLength = len(initialboard[0])
    for y in range(colLength):
        for x in range(rowLength):
            cellInfo = initialboard[y][x]
            if cellInfo[3] != RotationType.na.value:
                print(initialboard[y][x])
                initialboard[y][x] = cellInfo[:3] + str((int(cellInfo[3]) + 6) % 8) + cellInfo[4:] #rotate 90 degrees
                print(initialboard[y][x])
    return rotateMatrix(initialboard)

def rotateMatrix(matrix):
    newRowLength = len(matrix)
    newColLength = len(matrix[0])
    newMatrix = []
    for y in range(newColLength):
        row = []
        for x in range(newRowLength):
            row.append(copy.deepcopy(matrix[x][newColLength-1-y]))
        newMatrix.append(row)
    return newMatrix

def rotateGopherCell(gopherCell, originalrowlength):
    oldx, oldy, oldrotation, state = gopherCell
    newx = oldy
    newy = originalrowlength - 1 - oldx
    newrotation = (oldrotation + 6) % 8
    return (newx, newy, newrotation, state)

def rotateSimulation(initialboard, activeCells, gopherCells):
    newac = []
    newgc = []
    originalrowlength = len(initialboard[0])
    for step in range(len(activeCells)):
        newac.append(rotateMatrix(activeCells[step]))
        newgc.append(rotateGopherCell(gopherCells[step], originalrowlength))
    newib = rotateInitialBoard(initialboard)
    return newib, newac, newgc

def addTrapToTerrain(terrain, start_x, start_y, trapboard):
        """adds a 'miniboard' to self's board with the top left corner at the indicated position"""
        rowLength = len(trapboard[0])
        colLength = len(trapboard)
        trLength = len(terrain[0])
        tcLength = len(terrain)
        if start_x + rowLength <= trLength:
            if start_y + colLength <= tcLength:
                for x in range(rowLength):
                    for y in range(colLength):
                        terrain[start_y + y][start_x + x] = trapboard[y][x]
                return terrain
        raise Exception("This board does not fit")


def findCohesionPercent(filename, cohesionVal, returnVals=False):
    cohesionCounter = 0.0
    elementCounter = 0.0
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        rows = [row[0] for row in readCSV]
        numVals = int(rows[0])
        for row in rows[1 : numVals]:
            elementCounter += 1
            if float(row) >= cohesionVal:
                cohesionCounter += 1
        if cohesionCounter == 0:
            cohesionCounter += 1
            elementCounter += 1
        percent = cohesionCounter / elementCounter
        if returnVals:
            p_hat = float(rows[-2])
            r_hat = float(rows[-1])
            return percent, p_hat, r_hat
        else:
            return percent

def fsc(cohesion, filename="cohesionVals.csv"):
    fsc = 0.0
    for val in findCohesionPercent(filename, cohesion, True):
        fsc += -m.log(val, 2)
    return fsc

def isTrap(trap, alg, sigVal=4.33):
    cohesion = alg(trap)
    if fsc(cohesion) > sigVal:
        return True
    else:
        return False
        



################
## The below is so bad my heart cringes
###############

def whatConnections(trap):
    """
    this function returns how many connections a trap has
    """
    doorCell
    for cell in allCells: # flattens board into 1d  array
        if cell.cellType == CellType.door:
            doorCell = cell

    ## specified path in order to go around a trap
    x = [1,0,2,0,0,1,2,1,2,2]
    y = [3,3,0,1,0,0,0,2,2,3]

    numConnect = 0
    for i in len(x) and j in len(y):  #wrong syntax!!!!!!!!
        if i=1 and j=3: #[1,3]
            if (trap[0,3]).cellType = arrow and (trap[0,3]).rotationtype = down:
                numConnect += 1
            elif (trap[0,3]).cellType = wire:
                if (trap[0,3]).angleType = lright and ((trap[0,3]).rotationtype = down or left):
                    numConnect += 1
                elif (trap[0,3]).angleType = rright and ((trap[0,3]).rotationtype = up or left):
                    numConnect += 1
                elif (trap[0,3]).angleType = straight and ((trap[0,3]).rotationtype = right or left):
                    umConnect += 1
        
        elif i=0 and j=3:
        elif i=2 and j=0:
        elif i=0 and j=1:
        elif i=0 and j=0:
        elif i=1 and j=0:
        elif i=2 and j=0:
        elif i=1 and j=2:
        elif i=2 and j=2:
        elif i=2 and j=3:

            ## mmm... maybe not do this for every one





#################
## Get Trap Description


# List of Cells
# starting with cell adj to door and last is arrow
trapPaths = [[],[]]  # [[left path], [right path]]

def functionalPaths(trap):
    """
    Assess when traps are working.
    This will likely be run on random traps
    ...
    Returns list of two lists: Lpath and Rpath
    If a list is empty that path doesnt work
    """
    arrowCells, wireCells, arrowThickTypes, wireThickTypes, doorCell, leftDoor, rightDoor = organizeTrap(trap)

    if len(arrowCells) == 0: # no arrows? can't zap.
        return trapPaths
    elif workingSingleArrows(trap): # no wire trap
        return trapPaths
    #else:
    # for all other types of traps
        # check door
        # check others
     
    # elif isDoorSetUp(doorCell): # to begin with, does the door have proper wires attached?
    #     if workingSingleArrows(trap):
    #         return 0
    #     for i in range(len(arrowCells)):
    #         i += -1  ## oof I'll google prettier python for loops in a sec
    #         if not assessPath(arrowCells[i]):
    #             return False
    #     return True
    
def organizeTrap(trap):
    """
    Helper Function
    Streamlines making arrays for the cellTypes
    ...
    input: trap
    output: lists of lists?
    """
    allCells = flatten(trap.board)
    wireCells = []
    arrowCells = []
    wireThickTypes = [0,0,0]
    arrowThickTypes = [0,0,0]
    doorCell = []

    # [skinny, normal, wide]

    for cell in allCells: # flattens board into 1d  array
        if cell.cellType == CellType.wire:
            wireCells.append(cell)
        elif cell.cellType == CellType.arrow:
            arrowCells.append(cell)
        #     arrowLoc.append(cell)
        elif cell.cellType == CellType.door:
            doorCell.append(cell)

    for cell in wireCells:
        wireThickTypes[cell.thickType.value] += 1
    for cell in arrowCells:
        arrowThickTypes[cell.thickType.value] += 1
    
    # bad style to define vars here? but I need doorCell value first
    leftDoor = doorCell.getNeighboringCell(6) 
    rightDoor = doorCell.getNeighboringCell(2)

    typeLists =[arrowCells, wireCells, arrowThickTypes, wireThickTypes, doorCell, leftDoor, rightDoor]
    print("[arrowCells, wireCells, arrowThickTypes, wireThickTypes,  doorCell]")

    return typeLists


def workingSingleArrows(trap):
    """
    updates trapPaths if correct connection
    ...
    does not classify single right angles as functional traps
    """
    arrowCells, wireCells, arrowThickTypes, wireThickTypes, doorCell, leftDoor, rightDoor = organizeTrap(trap)

    if len(wireCells) == 0 and len(arrowCells) != 0: # no wire cells only arrows
        if leftDoor.angleType == 1 and leftDoor.rotationType == 6: #racute, left
            trapPaths[0].append(leftDoor)
        if rightDoor.angleType == 0 and rightDoor.rotationType == 2: #lacute, right
            trapPaths[1].append(rightDoor)


def doorConnected(doorCell):
    """ 
    Input: Door Cell
    adds to global lists if there are wires/arrows are connected properly
    ...
    only runs on traps with wires AND arrows
    Runs on the condition that it is not a single arrow trap
    """
    leftOfDoor = doorCell.getNeighboringCell(6)
    rightOfDoor = doorCell.getNeighboringCell(2)

    if (leftOfDoor.angleType == 3) and (leftOfDoor.rotationType == 6): #if rright3,left6 I_
        trapPaths[0].append(leftOfDoor)
    if (rightOfDoor.angleType == 2) and (rightOfDoor.rotationType == 2): #lright2, right2 _I
        trapPaths[1].append(leftOfDoor)



def assessPath(currCell):
    """
    Follows the current from L or R of door to check if wire-arrow paths are valid
    ---
    returns false when cells or thicktype doesnt align.
    updates list when cells/thicktypes align
    If a path is false, it sets the list to empty
    Input: an door cell to begin with
    Output: boolean, activePath
    """

    leftOfDoor = currCell.getNeighboringCell(6)
    rightOfDoor = doorCell.getNeighboringCell(2)

    if len(trapPaths[0]) and len(trapPaths[1]) == 1:
        doorConnected(currCell)
        assessPath(currCell.getNeighbors(6)) #leftDoor
        assessPath(currCell.getNeighbors(2)) #rightDoor

    # Base case, if we reach this point the current has successfully traveled
    # if the cell is a door the arrow-wire path is valid
    if currCell.cellType == 3: #if arrow cell 
        # if -- check endpoints
        # check 
        return trapPaths

####### Cindy TODO: (if she ever figures out how to refer to endpts correctly)
## Steps: (for wire and arrow)
    # 1. find the arrowType/rotationType match
    # 2. check the neighboring cells matches one of these options
    # 3. check that the neighboring cell also matches the same WIRE THICCCNESSS
    # 4. append currCell to activePath = []
    # 5. if the neighboring cell DOES match, make a recursive call with
    # with the cell neighboring the endpoint
    # 6. If it's the correct path, it will eventually reach the door and return true. yay

    # 7. BONUS: Write a helper to save and return the value of activePath, so that we can
    # use it to determine danger and prob of trap

    # now unleash massive combinations
    
    elif currCell.cellType == 3: #arrow
        if currCell.rotationtype == 0: #lacute
            if currCell.rotationType == 0:
                activePath.append(currCell)
            

    #elif currCell.cellType == 2: #wire
    # if 
    #     elif currCell.rotationType == 0 or 4:
    #         c.getNeighboringCell(0,)
    #thickness
    #     activePath.append(currCell)
    
    # return activePath

###################################################################################
###################################################################################

def trapDanger2(trap):
    cellList = flatten(trap.board)
    if not hasArrow(cellList):
        return 1.0
    else:
        return threatAssessment(cellList)

def trapDanger3(trap):
    row = trap.rowLength
    cellList = flatten(trap.board)
    if not hasArrow(cellList):
        return 1
    else:
        leftCol = [cellList[i] for i in range(len(cellList)) if i % row == 0]
        rightCol = [cellList[i] for i in range(len(cellList)) if (i + 1) % row == 0 and i != 0]
        leftThreat = threatAssessment(leftCol)
        rightThreat = threatAssessment(rightCol)
        avgThreat = (leftThreat + rightThreat)/2.0
        return avgThreat


def hasArrow(cellList):
    hasArrow = False
    for cell in cellList:
        if cell.cellType == CellType.arrow:
            hasArrow = True
    return hasArrow


def threatAssessment(cellList):
    thickTypes = [0,0,0]
    for cell in cellList:
        if cell.thickType != ThickType.na:
            thickTypes[cell.thickType.value] += 1
    valuelist = []
    for value in range(3):
        valuelist += [value + 1] * thickTypes[value]
    if len(valuelist) == 0:
        return 0 #if nothing, no threat
    elif len(valuelist) == 1:
        std = 0 #if only one thing, maximum cohesion/minimum std
    else:
        std = np.std(valuelist)
    mean = np.mean(valuelist)

    cohesion = 1 - std #for 3 values, maximum standard deviation is 1, which is least threat
    damage_potential = mean / 3 #maximum mean is 3 (biggest threat)
    threat = (0.7 * cohesion) + (0.3 * damage_potential) #cohesion is more important
    return threat

    

def gopherEatTimer(probEnter):
    """
    assigns probs for timer based on gopher's detection of threat.
    """
    idealTimer = probEnter * 5
    initialProbs = [0.05, 0.05, 0.05, 0.05, 0.05]
    for i in range(5):
        if idealTimer <= i + 1:
            initialProbs[i] = 0.6
            if i == 0:
                initialProbs[1] = 0.2
                initialProbs[2] = 0.1
            elif i == 4:
                initialProbs[3] = 0.2
                initialProbs[2] = 0.1
            else:
                initialProbs[i+1] = 0.15
                initialProbs[i-1] = 0.15
            break
    return np.random.choice([1,2,3,4,5], p=initialProbs, size=1)[0]


## revisit this code in specific case
def uniformTraps(trap):
    """
    This function is probably not helpful
    ...
    returns the probability gopher will enter given that
    the traps are uniform in thickType
    """
    arrowCells, wireCells, arrowThickTypes, wireThickTypes, doorCell = organizeTrap(trap)

    only = lambda ind, typelist: sum([typelist[i] > 0 for i in range(len(typelist)) if i != ind])==0
    
    # Case: when all arrows/wires are of uniform thickness
    if len(wireCells) and len(arrowCells) == 0:
        if len(arrowCells) == 0:
            print("No danger and highest probability")
            return 0.9
        else: #if more than one arrow, you gotta check that the arrow is next to the door 
            if doorCell: #connected to gate, placed filler
                if arrowThickTypes == 0: #not zero!!
                    return 0.7 # or a probability that reflects the 
            else:
                return 0.9 # or 1?

## checks if uniform
    if (wireThickTypes[2] and arrowThickTypes[2] > 0) and all(i is 0 for i in wireThickTypes[:2]) and all(j is 0 for j in arrowThickTypes[:2]):
        print("All wide thickness. very thicc. Highest danger and low probability of entering")
        return 0.1
    if (wireThickTypes[1] and arrowThickTypes[1] > 0) and all(i is 0 for i in wireThickTypes.remove(wireThickTypes[1])) and only(1, wireThickTypes):
        print("All normal thickness. Medium danger and medium probability of entering")
        return 0.5
    if (wireThickTypes[0] and arrowThickTypes[0] > 0) and all(i is 0 for i in wireThickTypes[0:]) and all(j is 0 for j in wireThickTypes[0:]):
        print("All skinny thickness. low danger and high probability of entering")
        return 0.8

    ### CASE: when >1 arrow AND not uniform thickness
















################### Older Codee BEGIN ##########################
# def gopherProbEnter1(trap):
#     """
#     This returns the probability that the gopher will enter for working traps.
#     Working traps are traps that are able to hurt the gopher
#     """

#     checkBrokenTrap(trap)
#     ## WORKING TRAP CASES
#     ## Case: only arrows with no wires, but arrows are connected to the gate so they still fire
#     allCells = flatten(trap.board)
#     wireCells = []
#     arrowCells = []
#     arrowLoc = [] #will be list of lists
#     doorLoc = []
#     wireThickTypes = [0,0,0]
#     arrowThickTypes = [0,0,0]
#     # [skinny, normal, wide]

#     # Collect the cells' info
#     for cell in allCells: # flattens board into 1d  array
#         if cell.cellType == CellType.wire:
#             wireCells.append(cell)
#         elif cell.cellType == CellType.arrow:
#             arrowCells.append(cell)
#             arrowLoc.append(cell)
#         elif cell.cellType == CellType.door:
#             doorLoc.append(cell)

#     for cell in wireCells:
#         wireThickTypes[cell.thickType.value] += 1
#     #for cell in arrowCells:

   
# wiree stuff:
 # elif leftDoor.angleType == 3 and leftDoor.rotationType == 6: #rright, left
        #     singleArrows[0] = 2
        # elif leftDoor.angleType == 2 and leftDoor.rotationType == 2: #lright, right
        #     singleArrows[1] = 2

  # if rightDoor.angleType == 0 and leftDoor.rotationType == 2: #lacute, right
        #         trapPaths[1].append(rightDoor)
        #         if rightDoor.angleType == 1 and rightDoor.rotationType == 6: #racute, left
        #             trapPaths[0].append(rightDoor)