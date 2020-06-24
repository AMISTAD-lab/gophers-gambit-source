from classCell import *
from typeCell import *
from classBoard import *

class Trap(Board):
    def __init__(self, rowLength, colLength, functional):
        self.func = functional
        super().__init__(rowLength, colLength)
        if functional:
            self.board = super().realTrap(rowLength, colLength)
        else:
            self.board = super().randomTrap(rowLength, colLength)
