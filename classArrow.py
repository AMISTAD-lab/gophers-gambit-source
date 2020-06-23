from typeCell import *
## this class constructs arrow like cells
class Arrow(Cell):
    def __init__(self, row, col, cellType, angleType, rotationType, thickType):
        self.cellType = CellType.arrow
        super.__init(row, col, self.cellType, angleType, rotationType, thickType)