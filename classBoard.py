import abc
from abc import ABC, abstractmethod, ABCMeta
from typeCell import *
from classCell import *
import numpy as np
import math as m

functionalTraps = [] #list of handmade traps
trapPieces = [CellType.wire, CellType.arrow, CellType.floor]

class Board(metaclass = ABCMeta):

    def __init__(self, rowLength, colLength):
        self.rowLength = rowLength
        self.colLength = colLength
        self.board = self.emptyBoard(rowLength, colLength)

    def __repr__(self):
        """string representation of Board"""
        string = ""
        for y in range(self.colLength):
            for x in range(self.rowLength):
                string += str(self.board[x][y]) + "\t"
            string += "\n\n\n"
        return string

    def addBoard(self, start_x, start_y, miniboard):
        """adds a 'miniboard' to self's board with the top left corner at the indicated position"""
        if start_x + miniboard.rowLength < self.rowLength:
            if start_y + miniboard.colLength < self.colLength:
                for x in range(miniboard.rowLength):
                    for y in range(miniboard.colLength):
                        self.board[start_x + x][start_y + y] = miniboard.board[x][y]
                return
        raise Exception("This board does not fit")

    def right(self):
        """faces the entrance of a trap to the left, given an initially downward facing trap"""
        board = self
        for i in range(1):
            board = board.rotateBoard90()
        return board
    
    def up(self):
        """faces the entrance of a trap to the left, given an initially downward facing trap"""
        board = self
        for i in range(2):
            board = board.rotateBoard90()
        return board

    def left(self):
        """faces the entrance of a trap to the left, given an initially downward facing trap"""
        board = self
        for i in range(3):
            board = board.rotateBoard90()
        return board

    def rotateBoard90(self):
        """returns a board rotated 90 degrees counter clockwise"""
        newRowLength = self.colLength
        newColLength = self.rowLength
        newBoard = Board(newRowLength, newColLength)
        for x in range(newRowLength):
            for y in range(newColLength):
                cell = self.board[newColLength-1-y][x]
                newBoard.board[x][y] = cell
        return newBoard

    def emptyBoard(self, rowLength, colLength):
        """generates a board full of dirt for a default terrain"""
        board = []
        for x in range(rowLength):
            row = []
            for y in range(colLength):
                row.append(Cell(x,y, CellType.dirt))
            board.append(row)
        return board

    def realTrap(self, rowLength, colLength):
        """chooses a trap from the real selection, filtered to right dimensions"""
        dimCheck = lambda trap: trap.rowLength == rowLength and trap.colLength == colLength
        filteredTraps = filter(dimCheck, functionalTraps)
        board = np.random.choice(filteredTraps, size=1)[0]
        #will want something to prevent repeated selection of a trap probably
        return board

    def randomTrap(self, rowLength, colLength):
        """randomly generates a trap with the given dimensions, with door at the bottom and food in the center"""
        #need to decide if inner cells have to be floor or can be trap pieces
        board = []
        bottom_y = colLength - 1
        center_x = m.ceil(rowLength / 2) - 1
        center_y = m.ceil(colLength / 2) - 1
        for x in range(rowLength):
            row = []
            for y in range(colLength):
                if x == center_x and y > center_y:
                    #allow path to food
                    piece = CellType.floor
                else:
                    piece = np.random.choice(trapPieces, size=1)[0]
                row.append(Cell(x, y, piece))
            board.append(row)
        #overwrite food and door placement
        board[center_x][bottom_y] = Cell(center_x, bottom_y, CellType.door)
        board[center_x][center_y] = Cell(center_x, center_y, CellType.food)
        return board

    