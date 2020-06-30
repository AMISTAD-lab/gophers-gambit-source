from typeCell import *
from classFloor import *
from typeRotation import *
import algorithms as alg
import numpy as np

class Gopher:
    def __init__(self, start_x, start_y, ownerBoard, intention, rotationType=RotationType.up):
        self.intention = intention
        self.ownerBoard = ownerBoard
        self.rotationType = rotationType
        self.alive = True
        self.hit = False
        self.x = start_x
        self.y = start_y
        self.entering = False
        self.leaving = False
        self.left = False
        self.hasEaten = False
        self.eatingTimer = 0

    def state(self):
        if not self.alive:
            state = 0
        elif self.hit:
            state = 2
        else:
            state = 1
        return state

    def updateCell(self):
        if self.hit:
            self.hit = False
        if self.entering:
            self.rotationType = RotationType.up
            self.enter()
        elif self.leaving:
            self.rotationType = RotationType.down
            self.leave()
        elif self.eatingTimer > 0:
            self.eat()
        else:
            #at beginning of trap, so figure out whether to enter or not (done in algs)
            if self.intention:
                probEnter = alg.gopherProbEnter2(self.ownerBoard) #currently using the cohesion one
            else:
                probEnter = 1 #arbitrarily chosen rn
            if np.random.binomial(1, probEnter) == 1:
                self.entering = True
                self.leaving = False
            else:
                self.entering = False
                self.leaving = False
                self.left = True

    def enter(self):
        self.y -= 1
        if self.ownerBoard.board[self.y][self.x].cellType == CellType.food:
            self.eatingTimer = 3 #set this randomly
            self.entering = False
            self.leaving = False
    
    def leave(self):
        self.y += 1
        self.eatingTimer = 0
        if self.ownerBoard.board[self.y-1][self.x].cellType == CellType.door:
            #if just passed door (exited trap)
            self.entering = False
            self.leaving = False
            self.left = True

    def eat(self):
        self.eatingTimer -= 1
        #increase food/hunger measure (if we care about that)
        if self.eatingTimer <= 0:
            self.hasEaten = True
            self.leaving = True
            self.entering = False

    def trapTriggered(self):
        """called after a projectile lands"""
        self.leaving = True
        self.entering = False

    def hitByProjectile(self, projectile, timeStep):
        """called when hit by a projectile"""
        if np.random.binomial(1, projectile.strength) == 1:
            self.alive = False
        else:
            self.hit = True
            self.leaving = True
            self.entering = False
            
### Brainstorming what a random walk might look like


