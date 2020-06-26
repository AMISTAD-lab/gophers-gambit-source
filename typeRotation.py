import enum

class RotationType(enum.Enum):
    #based on pointing direction, which varies a little based on angle
    up = 0
    right = 2
    down = 4
    left = 6
    na = "x"