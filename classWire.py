from typeCell import *
from typeRotation import *
from typeDirection import *
import classCell as c
import algorithms as alg

class Wire(c.Cell):
    def __init__(self, x, y, ownerBoard, angleType, rotationType, thickType, active=False):
        self.directionType = alg.findDir(rotationType, angleType)
        endpoints = c.getEndpoints(self.directionType, rotationType)
        super().__init__(x, y, CellType.wire, ownerBoard, angleType=angleType, rotationType=rotationType, thickType=thickType, endpoints=endpoints, active=active)

    def updateCell(self, timeStep):
        """will be called once every time step from simulation"""
        if self.active and timeStep > self.activatedTimeStep:
            #do its thing if its active (and not same turn that it was activated) -- important so that this works independent of order of cells updating
            self.attemptTransfer(timeStep)
            self.active = False

    
"""
    wire would call the below for 1 direction
    door would call the below for 2 directions

    if my direction is this way
        get cell from that way
        transfer current to that cell
            (figures out whether it can or not and if so, does it)

"""
        







"""       
    def transferCurrent(self, timeStep):
        if(self.directionType == DirectionType.left): 
            if(self.x > 0):
                leftDestCell = self.ownerBoard.board[self.x - 1][self.y]
                if(leftDestCell.cellType == CellType.wire or CellType.arrow and leftDestCell.rotationType == RotationType.left and leftDestCell.thickType == self.thickType):
                    leftDestCell.toggleCell(True, timeStep)
        
        elif(self.directionType == DirectionType.right):
            if(self.x < self.ownerBoard.rowLength - 1):
                rightDestCell = self.ownerBoard.board[self.x + 1][self.y]
                if(rightDestCell.cellType == CellType.wire or CellType.arrow and rightDestCell.rotationType == RotationType.right and rightDestCell.thickType == self.thickType):
                    rightDestCell.toggleCell(True, timeStep)

        elif(self.directionType == DirectionType.down):
            if(self.y < self.ownerBoard.colLength - 1):
                upperDestCell = self.ownerBoard.board[self.x][self.y + 1]
                if(upperDestCell.cellType == CellType.wire or CellType.arrow and upperDestCell.rotationType == RotationType.down and upperDestCell.thickType == self.thickType):
                    upperDestCell.toggleCell(True, timeStep)

        elif(self.directionType == DirectionType.up):
            if(self.y > 0):
                lowerDestCell = self.ownerBoard.board[self.x][self.y - 1]
                if(lowerDestCell.cellType == CellType.wire or CellType.arrow and lowerDestCell.rotationType == RotationType.up and lowerDestCell.thickType == self.thickType):
                    lowerDestCell.toggleCell(True, timeStep)

        else:
            raise Exception("something aint right")
    
""" 