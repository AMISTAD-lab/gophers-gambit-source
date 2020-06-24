# what does the Gopher simulate, where do we inherit from?
class Gopher:
    def __init__(self, position):
        self.present = False
        self.alive = True
        self.position = 0  #the original position should be the gopher cell


## Cindy's comments: (feel free to delete all comments as soon as you've read them)
####### ok so there isn't an updateGopher method, but all of these methods update the gopher...

## This method should continually run until 
    def isActive(self):
        """returns true when the gopher has entered the room"""
        while present == false:
            if gopher.position == doorCell: #unsure how to refer to the position of the doorcell here
                Wire.launchSignal()  ## launch the signal at this point
                present == True
                return True

### maybe delete this function because it is too similar to isActive?
### but its a simpler version of isActive cause it just returns the status of present
    def inRoom(self):
        """Boolean Method: returns whether gopher is in room"""
        return self.present

    def isAlive():
        """continually checks on whether gopher is alive"""
        while alive == false:
            if gopher.position && projectile.position == foodCell # !!! These are not yet valid names!!
                alive = False
                return alive

### same reasoning to delete this method as the reason to delete inRoom
    def striked(self):
        return alive



