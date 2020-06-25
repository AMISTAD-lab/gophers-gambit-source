from classTrap import *
from classWire import *
from typeRotation import *
from typeThick import *
from typeAngle import *
#from classDoor import *
from classGopher import *



#since each trap simulation is independent of the previous (no health measure, just killed or not, no hunger measure)
   # - if we decide to add them, they can be input parameters for the simulation/gopher
#we can run them all back to back
#and say lifespan is the sum of steps in each trap until the next death
trap = Trap(3,3, False)

trap.board = [
    [Wire(0,1, trap, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.normal, active=False),
    Wire(0,1, trap, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.normal, active=False),
    Wire(0,2, trap, angleType=AngleType.lright, rotationType=RotationType.down, thickType=ThickType.normal, active=False)],
    
    [Wire(1,0, trap, angleType=AngleType.straight, rotationType=RotationType.right, thickType=ThickType.normal, active=False),
    Wire(1,1, trap, angleType=AngleType.straight, rotationType=RotationType.down, thickType=ThickType.normal, active=False),
    Wire(1,2, trap, angleType=AngleType.straight, rotationType=RotationType.left, thickType=ThickType.normal, active=False)],

    [Wire(2,0, trap, angleType=AngleType.lright, rotationType=RotationType.up, thickType=ThickType.normal, active=False),
    Wire(2,1, trap, angleType=AngleType.straight, rotationType=RotationType.down, thickType=ThickType.normal, active=False),
    Wire(2,2, trap, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.normal, active=False)]
    ]


flatten = lambda l: [item for sublist in l for item in sublist]

for i in range(10):
    print("UPDATING\n\n\n")
    for cell in flatten(trap.board):
        cell.updateCell(i)
    print(trap)


def updateSimulation():
    print("hi")
