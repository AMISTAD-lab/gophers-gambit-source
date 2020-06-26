import numpy as np
import shutil as sh 
from classTerrain import *
import simulation as s

# random walk stuff here! (generate terrainList)

def visualRun(rowLength, colLength, intention, trapList):
    trapInfo = []
    trapboardList = []
    for trap, x, y in trapList:
        ib, ac, gc, alive = s.simulateTrap(trap, intention, maxSteps=20)
        trapInfo.append([ib, ac, gc])
        trapboardList.append([ib, x, y])
    terrain = Terrain(rowLength, colLength, trapboardList)
    #create random walk frames
    gopherWalkCells = []
    #####
    terrainInfo = [terrain.board, gopherWalkCells]
    return trapInfo, terrainInfo

newjsFileName = "animation.js"
jsTemplateName = "template.js"

def writeTojs(trapList, terrainList):
    """ 
    Inputs:
        trapList: a list with elements of the form [initTrapBoard, activeTrapCells, gopherTrapCells]
            initTrapBoard: initial board for a trap.
            activeTrapCells: list of 2d lists with 1's in positions that are active, 0's otherwise.
            gopherTrapCells: List of tuples (each tuple is: [x, y, rotationType, state])
        terrainList: a list of the form [initTerrainBoard, gopherTerrainCells]
            initTerrainBoard: the initial board for the terrain (just a single 2d list!)
            gopherTerrainCells: list of tuples (each tuple is: [x, y, rotationType]) (state is always alive)
    """  
    newFile = open(newjsFileName, "w") # create new file
    newFile.close()
    sh.copy(jsTemplateName, newjsFileName) # copy contents of template to new file
    jsFile = open(newjsFileName, "a") # open the file to append to
    jsFile.write("function getInput(){\n")
    jsFile.write("trapList = " + str(trapList) + ";\n")
    jsFile.write("terrainList = " + str(terrainList) + ";\n")
    jsFile.write("}")
    jsFile.close()