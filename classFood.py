from typeCell import *
from typeAngle import *
from typeRotation import *
from typeThick import *
import classCell as c

class Food(c.Cell):
    def __init__(self, x, y, ownerBoard, angleType=AngleType.na, rotationType=RotationType.na, thickType=ThickType.na, active=False):
        super().__init__(x, y, CellType.food, ownerBoard)
        self.foodCount = 5 #Potentially can use this variable to decrease food on the foodtile? Do we want the food to stay? Or not?