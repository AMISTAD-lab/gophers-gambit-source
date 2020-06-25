from typeDirection import *
import simulation as s

class Projectile:

    def __init__(self, start_x, start_y, direction, strength, ownerBoard):
# later once we figure out the attributes of projectile
        self.direction = direction
        self.strength = strength #uses thicktype
        #self.speed = 0 #what are units,    i think we may do one time step universally
        self.x = start_x
        self.y = start_y  
        self.ownerBoard = ownerBoard
        self.landProjectile()

  
    def landProjectile(self):
        """this method figures out where the projectile lands when moving in the given direction"""
        while self.x >= self.ownerBoard.x and self.x < self.ownerBoard.rowLength and self.y >= self.ownerBoard.y and self.y < self.ownerBoard.colLength:
            #while in bounds of trap
            if self.checkHitGopher():
                break
            if self.direction in [DirectionType.right, DirectionType.upperright, DirectionType.lowerright]:
                self.x += 1
            if self.direction in [DirectionType.left, DirectionType.upperleft, DirectionType.lowerleft]:
                self.x -= 1
            if self.direction in [DirectionType.up, DirectionType.upperleft, DirectionType.upperright]:
                self.y -= 1
            if self.direction in [DirectionType.down, DirectionType.lowerleft, DirectionType.lowerright]:
                self.y += 1
        s.gopher.trapTriggered()
        #if we want to do some explosion where it lands even if it misses, use self.x and self.y here
    

    def checkHitGopher(self):
        """determines if the gopher has been hit""" 
        if self.x == s.gopher.x and self.y == s.gopher.y:
            s.gopher.hitByProjectile(self)
            return True
        return False

