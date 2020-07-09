import abc
from abc import ABC, abstractmethod, ABCMeta
from typeAngle import *
from typeRotation import *
from typeThick import *
from typeCell import *

class Cell(metaclass = ABCMeta):
    def __init__(self, x, y, cellType, ownerBoard, angleType=AngleType.na, rotationType=RotationType.na, thickType=ThickType.na, endpoints=[], active=False):
        self.x = x
        self.y = y
        self.cellType = cellType
        self.angleType = angleType
        self.rotationType = rotationType
        self.thickType = thickType
        self.active = active
        self.activatedTimeStep = 0
        self.ownerBoard = ownerBoard
        self.endpoints = endpoints
        self.inputEndpoint = None

    def __repr__(self):
        return str(self.cellType.name) + " " +str(self.active)

    # def __eq__(self, other):
    #     #does not care about owner, just position and typesn
    #     return self.x == other.x and self.y == other.y and self.getBaseInfo() == other.getBaseInfo()


    def getBaseInfo(self):
        cellStr = str(self.cellType.value)
        cellStr += str(self.angleType.value)
        cellStr += str(self.thickType.value)
        cellStr += str(self.rotationType.value)
        return cellStr

    def updateCell(self, step):
        ...
    
    def activateCell(self, timeStep, inputEndpointIn):
        self.activatedTimeStep = timeStep
        self.active = True
        self.inputEndpoint = inputEndpointIn

    def attemptTransfer(self, timeStep):
        """ Attempts to transfer current to any connecting cells
        Inputs:
            timeStep: the current timestep of the simulation"""
        # get all directions of wires except wire that initially received the pulse:
        for endpoint in self.endpoints:
            if endpoint != self.inputEndpoint:
                # get cell
                cell = self.getNeighboringCell(endpoint)
                # check if thickness, endpoints match
                matchingEndpoint = getOppositeEndpoint(endpoint)
                if (cell != None) and (self.cellType == CellType.door or cell.thickType == self.thickType) and (matchingEndpoint in cell.endpoints): 
                    cell.activateCell(timeStep, matchingEndpoint)

    def getNeighboringCell(self, endpoint):
        """Returns the adjacent cell in the direction of the given endpoint
        Inputs:
            endpoint: the endpoint we are using as the direction"""
        if endpoint == 0 and self.y > 0:
            return self.ownerBoard.board[self.y - 1][self.x]
        elif endpoint == 2 and self.x < self.ownerBoard.rowLength - 1:
            return self.ownerBoard.board[self.y][self.x + 1]
        elif endpoint == 4 and self.y < self.ownerBoard.colLength - 1:
            return self.ownerBoard.board[self.y + 1][self.x]
        elif endpoint == 6 and self.x > 0:
            return self.ownerBoard.board[self.y][self.x - 1]
        else:
            return None

def getOppositeEndpoint(endpoint):
    """Gets the opposite endpoint to the one passed in"""
    return (endpoint + 4) % 8

def getEndpoints(directionType, rotationType):
    startPoint = (rotationType.value + 4) % 8 #gets opposite direction
    endPoint = directionType.value
    return [startPoint, endPoint]
