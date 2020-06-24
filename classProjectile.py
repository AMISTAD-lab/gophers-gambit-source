from classProjectile import *

class Projectile:

    def __init__(self, direction, speed):
# later once we figure out the attributes of projectile
        self.direction = direction
        self.speed = 0 #what are units
        self.position = [0][0]  #just set a random defauly

######## Cindy's notes (feel free to delete all comments as soon as you've read them)
    def launchProjectile(self, gopher, direction, Arrow):
        """this method launches the projectile in the given direction"""
        ### Do we need a while condition here before the if
        ### while gopher.present == true: seomthing like tht
        if Arrow.signalReady():
            ### launch animation
    

    def hitGopher(self, gopher):
        """determines if the gopher has been hit""" 
        return gopher.isAlive()
        # return gopher.striked()
        ### see Gopher Class for these methods
    

    ##update Projectile():
