import enum

class RotationType(enum.Enum):
    #based on pointing direction, which varies a little based on angle
    ## What about variations on stem of the arrow
    
    up = 0
    right = 2
    down = 4
    left = 6
    na = "x"