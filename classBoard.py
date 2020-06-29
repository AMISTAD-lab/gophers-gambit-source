import abc
from abc import ABC, abstractmethod, ABCMeta

from typeCell import *
from typeAngle import *
from typeThick import *
from typeRotation import *

from classCell import *
from classDoor import *
from classFloor import *
from classFood import *
from classDirt import *
from classWire import *
from classArrow import *

import numpy as np
import math as m
import algorithms as alg

import designedTraps as dt


functionalTraps = [dt.test1] #list of handmade traps
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

class Board(metaclass = ABCMeta):

    def __init__(self, rowLength, colLength):
        self.rowLength = rowLength
        self.colLength = colLength
        self.board = self.emptyBoard(rowLength, colLength)

    def __repr__(self):
        """string representation of Board"""
        return alg.formatMatrix(self.board)

    def saveState(self):
        activecells = self.emptyBoard(self.rowLength, self.colLength)
        for y in range(self.colLength):
            for x in range(self.rowLength):
                activecells[y][x] = int(self.board[y][x].active == True)
        return activecells

    def saveCells(self):
        allcells = self.emptyBoard(self.rowLength, self.colLength)
        for y in range(self.colLength):
            for x in range(self.rowLength):
                allcells[y][x] = self.board[y][x].getBaseInfo()
        return allcells

    def emptyBoard(self, rowLength, colLength):  
        """generates a board full of dirt for a default terrain"""
        board = []
        for y in range(colLength):
            row = []
            for x in range(rowLength):
                row.append(Dirt(x,y, self))
            board.append(row)
        return board

    def realTrap(self, rowLength, colLength):
        """chooses a trap from the real selection, filtered to right dimensions"""
        dimCheck = lambda board: len(board[0]) == rowLength and len(board) == colLength
        filteredTraps = list(filter(dimCheck, functionalTraps))
        if len(filteredTraps) == 0:
            raise Exception("No traps met that specification")
        trapIndices = list(range(len(filteredTraps)))
        choice = np.random.choice(trapIndices, size=1)[0]
        board = filteredTraps[choice]
        #will want something to prevent repeated selection of a trap probably
        for cell in alg.flatten(board):
            cell.ownerBoard = self
        return board

    def randomTrap(self, rowLength, colLength):
        """randomly generates a trap with the given dimensions, with door at the bottom and food in the center"""
        #need to decide if inner cells have to be floor or can be trap pieces
        board = []
        bottom_y = colLength - 1
        center_x = m.ceil(rowLength / 2) - 1
        center_y = m.ceil(colLength / 2) - 1
        for y in range(colLength):
            row = []
            for x in range(rowLength):
                if x == center_x and y > center_y:
                    #allow path to food
                    piece = Floor
                else:
                    piece = np.random.choice(trapPieces, size=1)[0]
                    rotation = np.random.choice(rotationOptions[piece], size=1)[0]
                    angle = np.random.choice(angleOptions[piece], size=1)[0]
                    thick = np.random.choice(thickOptions[piece], size=1)[0]
                row.append(piece(x, y, self, angleType=angle, rotationType=rotation, thickType=thick))
            board.append(row)
        #overwrite food and door placement
        board[bottom_y][center_x] = Door(center_x, bottom_y, self)
        board[center_y][center_x] = Food(center_x, center_y, self)
        return board

    