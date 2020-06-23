import enum

class RotationType(enum.Enum):
    #based on pointing direction, which varies a little based on angle
    left = 0
    right = 1
    up = 2
    down = 3
    na = 4