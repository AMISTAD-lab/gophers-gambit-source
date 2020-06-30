from classTrap import *
from classDoor import *
from classFloor import *
from classFood import *
from classDirt import *
from classWire import *
from classArrow import *

test1 = [
    [Arrow(0,0, None, angleType=AngleType.racute, rotationType=RotationType.up, thickType=ThickType.normal, active=False), Wire(1,0, None, angleType=AngleType.straight, rotationType=RotationType.right, thickType=ThickType.normal, active=False), Arrow(2,0, None, angleType=AngleType.lacute, rotationType=RotationType.up, thickType=ThickType.normal, active=False)],
    [Wire(0,1, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.normal, active=False),Food(1,1, None),Wire(2,1, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.normal, active=False)],
    [Wire(0,2, None, angleType=AngleType.straight, rotationType=RotationType.down, thickType=ThickType.normal, active=False),Floor(1,2, None),Wire(2,2, None, angleType=AngleType.straight, rotationType=RotationType.down, thickType=ThickType.normal, active=False)],
    [Wire(0,3, None, angleType=AngleType.lright, rotationType=RotationType.down, thickType=ThickType.normal, active=False),Door(1,3, None, angleType=AngleType.straight, rotationType=RotationType.up, active=False),Wire(2,3, None, angleType=AngleType.rright, rotationType=RotationType.down, thickType=ThickType.normal, active=False)]
    ]

trap0 = [
    [Arrow(0,0, None, angleType=AngleType.racute, rotationType=RotationType.up, thickType=ThickType.skinny), Arrow(1,0, None, angleType=AngleType.lright, rotationType=RotationType.left, thickType=ThickType.normal), Wire(2,0, None, angleType=AngleType.lright, rotationType=RotationType.up, thickType=ThickType.normal)],
    [Wire(0,1, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.skinny), Food(1,1,None), Wire(2,1,None,angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.normal)],
    [Wire(0,2, None, angleType=AngleType.lright, rotationType=RotationType.down, thickType=ThickType.skinny), Door(1,2, None), Wire(2,2, None, angleType=AngleType.lright, rotationType=RotationType.left, thickType=ThickType.normal)],
]

trap1 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Arrow(0,1, None, angleType=AngleType.rright, rotationType=RotationType.up, thickType=ThickType.normal), Food(1,1, None), Arrow(2,1, None, angleType=AngleType.lright, rotationType=RotationType.up, thickType=ThickType.normal)],
    [Wire(0,2, None, angleType=AngleType.lright, rotationType=RotationType.left, thickType=ThickType.normal), Door(1,2, None), Wire(2,2, None, angleType=AngleType.rright, rotationType=RotationType.right, thickType=ThickType.normal)]
]

traps = [trap0, trap1]