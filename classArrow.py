from typeCell import *
import classCell as c
from typeAngle import *
from typeRotation import *
## this class constructs arrow like cells
class Arrow(Cell):
    def __init__(self, x, y, cellType, angleType, rotationType, thickType, active):
        self.cellType = CellType.arrow
        self.position = 0
        super.__init(x, y, self.cellType, angleType, rotationType, thickType, active)

######## Cindy's notes (feel free to delete all comments as soon as you've read them)

### I imagine that a signal would be traveling up the wire cells
### such that we could track its position
### Thus since "signal" isnt defined this is mostly pseudo code
    def signalReady(self, Wire):
        """this tells us if there is a signal from the arrow"""
        while gopher.present == true: ###while the gopher has entered the room/the signal has launched and is crawling upu the wire
            if Arrow.position == Signal.position:
                return true

    def updateArrow():
        """this method updates the arrow everytime that

    