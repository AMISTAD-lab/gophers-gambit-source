from typeDirection import *
from typeThick import *
import simulation as s


class Projectile:

    def __init__(self, start_x, start_y, direction, thickType, ownerBoard, timeStep):
# later once we figure out the attributes of projectile
        self.direction = direction
        self.strength = self.assignStrength(thickType) 
        #self.speed = 0 #what are units,    i think we may do one time step universally
        self.x = start_x
        self.y = start_y  
        self.ownerBoard = ownerBoard
        self.landProjectile(timeStep)

  
    def landProjectile(self, timeStep):
        """this method figures out where the projectile lands when moving in the given direction"""
        s.gopher.trapTriggered()
        while self.x >= 0 and self.x < self.ownerBoard.rowLength and self.y >= 0 and self.y < self.ownerBoard.colLength:
            #while in bounds of trap
            if self.checkHitGopher(timeStep):
                break
            if self.direction in [DirectionType.right, DirectionType.upperright, DirectionType.lowerright]:
                self.x += 1
            if self.direction in [DirectionType.left, DirectionType.upperleft, DirectionType.lowerleft]:
                self.x -= 1
            if self.direction in [DirectionType.up, DirectionType.upperleft, DirectionType.upperright]:
                self.y -= 1
            if self.direction in [DirectionType.down, DirectionType.lowerleft, DirectionType.lowerright]:
                self.y += 1
        #if we want to do some explosion where it lands even if it misses, use self.x and self.y here
    

    def checkHitGopher(self, timeStep):
        """determines if the gopher has been hit""" 
        if self.x == s.gopher.x and self.y == s.gopher.y:
            s.gopher.hitByProjectile(self, timeStep)
            return True
        return False

    def assignStrength(self, thicktype):
        """assigns strength based on thick type"""
        #assigning random strength values, definitely subject to change
        if(thicktype == ThickType.skinny):
            return .2
        elif(thicktype == ThickType.normal):
            return .4
        elif(thicktype == ThickType.wide):
            return .6
        else:
            raise Exception("No bueno")



    

