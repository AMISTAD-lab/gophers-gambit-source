from classCell import *
from typeCell import *
from classBoard import *

class Trap(Board):
    def __init__(self, rowLength, colLength, functional, chosenBoard=None):
        self.func = functional
        super().__init__(rowLength, colLength)
        if chosenBoard:
            self.board = super().realTrap(rowLength, colLength, chosenBoard)
        elif functional:
            self.board = super().realTrap(rowLength, colLength)
        else:
            self.board = super().randomTrap(rowLength, colLength)