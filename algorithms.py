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


TOTAL = 427929800129788411
r = TOTAL * (1 + m.log(TOTAL))
p = 1 / TOTAL
f_g = {
    (0.0, 1.0): 427929800129788411 / TOTAL, 
    (1.0, 9.0): 325433210760000000 / TOTAL, 
    (1.0, 8.0): 27894275208000000 / TOTAL, 
    (1.0, 7.0): 1044600429600000 / TOTAL, 
    (1.0, 6.0): 22320522000000 / TOTAL, 
    (1.0, 5.0): 297606960000 / TOTAL, 
    (1.0, 4.0): 6634219686620400 / TOTAL, 
    (1.0, 3.0): 11484970933030920 / TOTAL, 
    (1.0, 2.0): 23517963156798 / TOTAL,
    (1.0, 1.0): 26730 / TOTAL,
    (2.0, 9.0): 94491857267100000 / TOTAL,
    (2.0, 7.0): 198206235360000 / TOTAL, 
    (2.0, 5.0): 31903190550 / TOTAL, 
    (2.0, 3.0): 234190287720 / TOTAL, 
    (3.0, 8.0): 605992606362000 / TOTAL, 
    (3.0, 7.0): 12883086433800 / TOTAL, 
    (3.0, 5.0): 783120960 / TOTAL, 
    (3.0, 4.0): 2472025149 / TOTAL, 
    (4.0, 9.0): 653221475739450 / TOTAL, 
    (4.0, 7.0): 305813393190 / TOTAL, 
    (4.0, 5.0): 3863700 / TOTAL, 
    (5.0, 9.0): 17872285365378 / TOTAL, 
    (5.0, 8.0): 378560698308 / TOTAL, 
    (5.0, 7.0): 2498533776 / TOTAL, 
    (5.0, 6.0): 5531652 / TOTAL, 
    (6.0, 7.0): 6510699 / TOTAL, 
    (7.0, 9.0): 1437497604 / TOTAL, 
    (7.0, 8.0): 6269400 / TOTAL, 
    (8.0, 9.0): 4276314 / TOTAL, 
    (10.0, 9.0): 3 / TOTAL
}

def functional_specified_complexity(connectionTuple):
    global r
    global p
    v = 1 / f_g[connectionTuple]
    k = r * p / v
    fsc = -m.log(k, 2)
    return fsc

def isTrap(trap, sigVal=13.29):
    connectionTuple = connectionsPerPiece(trap)
    if functional_specified_complexity(connectionTuple) >= sigVal:
        return True
    else:
        return False

def connectionsPerPiece(trap):
    connections = totalConnections(trap)
    if connections == 0:
        return (0, 1.0)
    numPieces = 0
    for cell in flatten(trap.board):
        if cell.cellType == CellType.wire or cell.cellType == CellType.arrow:
            numPieces += 1
    return simplifyRatioTuple(connections, numPieces)


def simplifyRatioTuple(num, denom):
	"""Simplifies the tuple, which represents the numerator and denominator of a fraction.
	Inputs: 
		num: the numerator
		denom: the denominator"""
	if num == 0:# group anything with num 0 into the (0, 1) category
		return (0.0, 1.0)
	elif num != 0 and denom == 0:
		raise Exception("ERROR: All cells are floor cells, but connections were found.")

	gcd = int(np.gcd(num, denom))
	num = num/gcd
	denom = denom/gcd
	return (num, denom) 


usedCells = []

def totalConnections(trap):
    """
    returns how many connections a trap has
    """
    global usedCells
    usedCells = []
    endpoints = 0
    allCells = flatten(trap.board)
    for cell in allCells:
        if cell.cellType == CellType.arrow or cell.cellType == CellType.wire or cell.cellType == CellType.door:
            for endpoint in cell.endpoints:
                neighbor = cell.getNeighboringCell(endpoint)
                if neighbor != None:
                    if (neighbor.cellType == CellType.wire) or ((cell.cellType == CellType.wire or cell.cellType == CellType.door) and neighbor.cellType == CellType.arrow):
                        if checkConnection(cell, endpoint):
                            endpoints += 1
                            usedCells.append(cell)   
    return endpoints


def checkConnection(cell, endpoint):
    """
    Helper func:
    returns true if that cell is connected and thicktypes match
    """
    global usedCells
    cellAtEndpoint = cell.getNeighboringCell(endpoint)
    matchingEndpoint = c.getOppositeEndpoint(endpoint)
    
    if cell.cellType == CellType.door:
        if (cellAtEndpoint not in usedCells) and (matchingEndpoint in cellAtEndpoint.endpoints):
            return True
    ## arrow or wire cell
    elif (cellAtEndpoint not in usedCells) and (matchingEndpoint in cellAtEndpoint.endpoints):
        if (cell.thickType == cellAtEndpoint.thickType):
            return True
    return False

def isDoorArrow(trap):
    """
    checks if door has door connections and arrow cells
    """
    cellList = flatten(trap.board)
    doorCell = []
    for cell in cellList:
        if cell.cellType == CellType.door:
            doorCell.append(cell)
    cleft = doorCell[0].getNeighboringCell(6)
    cright = doorCell[0].getNeighboringCell(2)
    if cleft.cellType == (CellType.arrow or CellType.wire):
        if cleft.rotationType == RotationType.left:
            if hasArrow:
                return 0.1
    elif cright.cellType == (CellType.arrow or CellType.wire):
        if cright.rotationType == (RotationType.right):
            if hasArrow:
                return 0.1
    return 1 # not dangerous trap


def trapDanger2(trap):
    cellList = flatten(trap.board)
    if not hasArrow(cellList):
        return 0
    else:
        return threatAssessment(cellList)

def trapDanger3(trap):
    row = trap.rowLength
    cellList = flatten(trap.board)
    if not hasArrow(cellList):
        return 0
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
    threat = (0.8 * cohesion) + (0.2 * damage_potential) #cohesion is more important
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













