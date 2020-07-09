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


functionalTraps = dt.traps #list of handmade traps
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
                activecells[y][x] = int(self.board[y][x].active)
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

    def realTrap(self, rowLength, colLength, chosenTrap=None):
        """chooses a trap from the real selection, filtered to right dimensions"""
        if chosenTrap:
            board = chosenTrap
        else:
            dimCheck = lambda board: len(board[0]) == rowLength and len(board) == colLength
            filteredTraps = list(filter(dimCheck, functionalTraps))
            if len(filteredTraps) == 0:
                raise Exception("No traps met that specification")
            trapIndices = list(range(len(filteredTraps)))
            choice = np.random.choice(trapIndices, size=1)[0]
            board = filteredTraps[choice]

        for cell in alg.flatten(board):
            cell.ownerBoard = self
            cell.active = False
        return board



    