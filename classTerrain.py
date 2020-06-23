from classCell import *
from typeCell import *

class Terrain:
    def __init__(self, numRows, numCols, trapList):
        self.numRows = numRows
        self.numCols = numCols
        self.trapList = trapList
        self.board = self.__emptyBoard(numRows, numCols)
   

    def __emptyBoard(self, numRows, numCols):
        board = []
        for r in range(numRows):
            row = []
            for c in range(numCols):
                row.append(Cell(r,c, CellType.dirt))
            board.append(row)
        return board
