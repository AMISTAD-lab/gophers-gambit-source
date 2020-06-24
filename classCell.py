import abc
from abc import ABC, abstractmethod, ABCMeta
from typeAngle import *
from typeRotation import *
from typeThick import *

class Cell(metaclass = ABCMeta):
    def __init__(self, x, y, cellType, angleType=AngleType.na, rotationType=RotationType.na, thickType=ThickType.na, active = False):
        self.x = x
        self.y = y
        self.cellType = cellType
        self.angleType = angleType
        self.rotationType = rotationType
        self.thickType = thickType
        self.active = active

    def __repr__(self):
        return str(self.cellType.name)
    
    def toggleCell(self, x, y, status):
        self.x = x
        self.y = y
        self.active = status