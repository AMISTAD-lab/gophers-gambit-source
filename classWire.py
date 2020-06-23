from typeCell import *

class Wire(Cell):
    def __init__(self, row, col, cellType, rotationType, thickType):
        self.cellType = CellType.wire
        super().__init__(row, col, self.cellType, rotationType, thickType)
        