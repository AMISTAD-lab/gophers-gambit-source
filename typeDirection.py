import enum

class DirectionType(enum.Enum):
    #based on pointing direction, which varies a little based on angle
    up = 0
    upperright = 1
    right = 2
    lowerright = 3
    down = 4
    lowerleft = 5
    left = 6
    upperleft = 7
    