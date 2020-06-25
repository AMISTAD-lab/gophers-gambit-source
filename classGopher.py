class Gopher:
    def __init__(self, start_x, start_y):
        #self.present = False
        self.alive = True
        self.x = start_x  #the original position should be the gopher cell
        self.y = start_y
        self.entering = False
        self.leaving = False
        self.eatingTimer = 0
        self.health = 3

    def updateCell(self):
        if self.entering:
            self.enter()
        elif self.leaving:
            self.leave()
        elif self.eatingTimer > 0:
            self.eat()
        else:
            print("i am deciding")
            #at beginning of trap, so figure out whether to enter or not (done in algs)

    def enter(self):
        print("i am entering")
        #move forward
        #if at food, start timer
            #entering = False
            #leaving = False
    
    def leave(self):
        print("i am leaving")
        #exit
        #if exiting door
            #entering = False
            #leaving = False
            #simulation of trap over

    def eat(self):
        self.eatingTimer -= 1
        #increase food/hunger measure (if we care about that)
        if self.eatingTimer <= 0:
            self.leaving = True
            self.entering = False

    def trapTriggered(self):
        """called after a projectile lands"""
        self.leaving = True
        self.entering = False

    def hitByProjectile(self, projectile):
        """called when hit by a projectile"""
        #figure out whether the hit was fatal and act accordingly (done in algs)
        #need to include probability
        newHealth = self.health - projectile.strength
        self.health = newHealth
        if self.health != 0:
            self.leaving = True
            self.entering = False
        else:
            self.alive = False
    

    # we'll make this the door's job
    ## This method should continually run until 
    #def isActive(self):
    #    """returns true when the gopher has entered the room"""
    #    while present == false:
    #        if gopher.position == doorCell: #unsure how to refer to the position of the doorcell here
    #            Wire.launchSignal()  ## launch the signal at this point
    #            present == True
    #            return True

    ### maybe delete this function because it is too similar to isActive?
    ### but its a simpler version of isActive cause it just returns the status of present
    #def inRoom(self):
    #    """Boolean Method: returns whether gopher is in room"""
    #    return self.present

    #def isAlive():
    #    """continually checks on whether gopher is alive"""
    #    while alive == false:
    #        if gopher.position and projectile.position == foodCell # !!! These are not yet valid names!!
    #            alive = False
    #            return alive
       



