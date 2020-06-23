
functionalTraps = [] #list of handmade traps

class Trap:
    def __init__(self, length, width, functional):
        self.length = length
        self.width = width
        if functional:
            self.trapBoard #= choose trap randomly from functionalTraps
        else:
            self.trapBoard #= call create random trap method