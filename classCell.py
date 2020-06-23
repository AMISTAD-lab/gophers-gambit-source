import abc
from abc import ABC, abstractmethod, ABCMeta
from typeAngle import *
from typeRotation import *
from typeThick import *

class Cell(metaclass = ABCMeta):
    def __init__(self, row, col, cellType, angleType=AngleType.na, rotationType=RotationType.na, thickType=ThickType.na):
        self.row = row
        self.col = col
        self.cellType = cellType
        self.angleType = angleType
        self.rotationType = rotationType
        self.thickType = thickType
    def __repr__(self):
        return str(self.cellType.name)
