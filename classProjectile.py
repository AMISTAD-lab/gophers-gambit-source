from classProjectile import *

class Projectile:

    def __init__(self, direction, speed):
# later once we figure out the attributes of projectile
        self.direction = direction
        self.speed = 40 #40 what? miles? im not sure

    def launchProjectile(self, gopher, direction, Arrow):
        """this method launches the projectile in the given direction"""
        if gopher.inRoom(): # Can I just say if self.present: instead
            direction = Arrow.angleType
    
    ######## Cindy changed:
    def hitGopher(self, gopher):
        """determines if the gopher has been hit""" 

    update Projectile():
    