from typeCell import *
from classCell import *
from typeAngle import *
from typeRotation import *
from classProjectile import *
import algorithms as alg

## this class constructs arrow like cells
class Arrow(Cell):
    def __init__(self, x, y, angleType, rotationType, thickType, active):
        endpoints = [(rotationType.value + 4) % 8]
        super.__init(x, y, CellType.arrow, angleType, rotationType, thickType, endpoints, active)
  

    def updateCell(self, timeStep):
        """this method updates the arrow every time step from simulation"""
        if self.active and timeStep > self.activatedTimeStep:
            #do its thing if its active (and not same turn that it was activated) -- important so that this works independent of order of cells updating
            self.launchProjectile(timeStep)
            self.active = False

    def launchProjectile(self):
        #figure out direction
        direction = alg.findDir(self.rotationType, self.angleType)
        #launch projectile
        Projectile(self.x, self.y, direction, self.thickType, self.ownerBoard)
    
 #this is handled by the previous cell turning on or not turning on this cell
   # def signalReady(self, Wire):
    #    """this tells us if there is a signal from the arrow"""
    #    while gopher.present == true: ###while the gopher has entered the room/the signal has launched and is crawling upu the wire
    #        if Arrow.position == Signal.position:
    #            return true