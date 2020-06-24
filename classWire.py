from typeCell import *
from classCell import * 
import classCell as c

class Wire(Cell):
    def __init__(self, x, y, cellType, rotationType, thickType, active):
        self.cellType = CellType.wire
        super().__init__(x, y, self.cellType, rotationType, thickType, active)
        
    def transferCurrent(self, rotationType):
        leftDestCell = Cell(self.x - 1)
        rightDestCell = Cell(self.x + 1)
        upperDestCell = Cell(self.y + 1)
        lowerDestCell = Cell(self.y - 1)

        if(self.rotationType == 0 or 1): #left or right
            if(leftDestCell.cellType == 2 or 3 and leftDestCell.rotationType == 0 or 1):
                c.toggleCell(leftDestCell.x, leftDestCell.y, True)
            if(rightDestCell.cellType == 2 or 3 and rightDestCell.rotationType == 0 or 1):
                c.toggleCell(rightDestCell.x, rightDestCell.y, True)

        if(self.rotationType == 2 or 3): #up or down
            if(upperDestCell.cellType == 2 or 3 and upperDestCell.rotationType == 2 or 3):
                c.toggleCell(upperDestCell.x, upperDestCell.y, True)
            if(lowerDestCell.cellType == 2 or 3 and lowerDestCell.rotationType == 2 or 3):
                c.toggleCell(lowerDestCell.x, lowerDestCell.y, True)
    
    ######## Cindy's notes (feel free to delete all comments as soon as you've read them)
    ### the method that would update the Wire

    def launchSignal(self):
        """This method is triggered by isActive() from the gopher class"""
        ### call the transfer current function that is above?
        ## I would like to add an member variable called signal
    
    