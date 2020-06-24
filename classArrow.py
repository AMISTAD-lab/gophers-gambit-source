from typeCell import *
import classCell as c
from typeAngle import *
from typeRotation import *
## this class constructs arrow like cells
class Arrow(Cell):
    def __init__(self, x, y, cellType, angleType, rotationType, thickType, active):
        self.cellType = CellType.arrow
        super.__init(x, y, self.cellType, angleType, rotationType, thickType, active)

    def signal(self, Wire):
        """this tells us if there is a signal from the arrow"""
        if

    def updateArrow():
        """this method updates the arrow everytime that