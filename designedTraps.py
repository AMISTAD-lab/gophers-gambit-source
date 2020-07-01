from classDoor import *
from classFloor import *
from classFood import *
from classDirt import *
from classWire import *
from classArrow import *


trap0 = [
    [Arrow(0,0, None, angleType=AngleType.racute, rotationType=RotationType.up, thickType=ThickType.skinny), Floor(1,0, None), Arrow(2,0, None, angleType=AngleType.lacute, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Wire(0,1, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.skinny), Food(1,1,None), Wire(2,1, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Wire(0,2, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.skinny), Floor(1,2,None), Wire(2,2,None,angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Wire(0,3, None, angleType=AngleType.lright, rotationType=RotationType.down, thickType=ThickType.skinny), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.skinny)],
]

trap1 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Arrow(0,1, None, angleType=AngleType.rright, rotationType=RotationType.up, thickType=ThickType.skinny),  Food(1,1, None), Arrow(2,1, None, angleType=AngleType.lright, rotationType=RotationType.up, thickType=ThickType.normal)],
    [Wire(0,2, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.skinny), Floor(1,2, None), Wire(2,2, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.normal)],
    [Wire(0,3, None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.skinny), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.normal)]
]

trap2 = [
    [Arrow(0,0, None, angleType=AngleType.racute, rotationType=RotationType.up, thickType=ThickType.normal), Floor(1,0, None), Floor(2,0, None)],
    [Wire(0,1, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.normal), Food(1,1, None), Floor(2,1, None)],
    [Wire(0,2, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.normal), Floor(1,2, None), Arrow(2,2, None, angleType=AngleType.lobtuse, rotationType=RotationType.up, thickType=ThickType.wide)],
    [Wire(0,3, None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.normal), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.wide)]
]

trap3 = [
    [Arrow(0,0, None, angleType=AngleType.racute, rotationType=RotationType.up, thickType=ThickType.wide), Arrow(1,0, None, angleType=AngleType.lright, rotationType=RotationType.left, thickType=ThickType.wide), Wire(2,0, None, angleType=AngleType.lright, rotationType=RotationType.up, thickType=ThickType.wide)],
    [Wire(0,1,None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.wide), Food(1,1, None), Wire(2,1, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.wide)],
    [Wire(0,2,None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.wide), Floor(1,2, None), Wire(2,2, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.wide)],
    [Wire(0,3,None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.wide), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.wide)]
    
]

trap4 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Floor(0,1, None), Food(1,1, None), Arrow(2,1, None, angleType=AngleType.lacute, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Arrow(0,2, None, angleType=AngleType.robtuse, rotationType=RotationType.up, thickType=ThickType.normal), Floor(1,2, None), Wire(2,2, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Wire(0,3, None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.normal), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.skinny)]
]

trap5 = [
    [Wire(0,0, None, angleType=AngleType.rright, rotationType=RotationType.up, thickType=ThickType.normal), Arrow(1,0, None, angleType=AngleType.rright, rotationType=RotationType.right, thickType=ThickType.normal), Floor(2,0, None)],
    [Wire(0,1, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.normal), Food(1,1, None), Arrow(2,1, None, angleType=AngleType.lright, rotationType=RotationType.up, thickType=ThickType.wide)],
    [Wire(0,2, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.normal), Floor(1,2, None), Wire(2,2, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.wide)],
    [Wire(0,3, None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.normal), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.wide)]
]

trap6 = [
    [Arrow(0,0, None, angleType=AngleType.racute, rotationType=RotationType.up, thickType=ThickType.wide), Floor(1,0, None),  Floor(2,0, None)],
    [Wire(0,1,None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.wide), Food(1,1, None), Arrow(2,1, None, angleType=AngleType.lright, rotationType=RotationType.up, thickType=ThickType.wide)],
    [Wire(0,2,None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.wide), Floor(1,2, None), Wire(2,2, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.wide)],
    [Wire(0,3,None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.wide), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.wide)]
]

trap7 = [
    [Floor(0,0,None), Floor(1,0,None), Floor(2,0,None)],
    [Floor(0,1,None), Food(1,1, None), Floor(2,1,None)],
    [Floor(0,2,None), Floor(1,2,None), Arrow(2,2, None, angleType=AngleType.lacute, rotationType=RotationType.up, thickType=ThickType.wide)],
    [Arrow(0,3, None, angleType=AngleType.racute, rotationType=RotationType.left, thickType=ThickType.skinny), Door(1,3,None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.wide)]
]

trap8 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Floor(0,1, None), Food(1,1, None), Arrow(2,1, None, angleType=AngleType.lacute, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Arrow(0,2, None, angleType=AngleType.robtuse, rotationType=RotationType.up, thickType=ThickType.normal), Floor(1,2, None), Wire(2,2, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Wire(0,3, None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.normal), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.skinny)]
]

trap9 = [
    [Floor(0,0,None), Arrow(1,0,None, angleType=AngleType.lright, rotationType=RotationType.left, thickType=ThickType.normal),  Wire(2,0, None, angleType=AngleType.lright, rotationType=RotationType.up, thickType=ThickType.normal)],
    [Floor(0,1,None), Food(1,1, None), Wire(2,1, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.normal)],
    [Arrow(0,2,None, angleType=AngleType.robtuse, rotationType=RotationType.up, thickType=ThickType.skinny), Floor(1,2, None), Wire(2,2, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.normal)],
    [Wire(0,3,None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.skinny), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.normal)]
]

trap10 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Arrow(0,1,None, angleType=AngleType.rright, rotationType=RotationType.up, thickType=ThickType.wide), Food(1,1, None), Floor(2,1, None)],
    [Wire(0,2,None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.wide), Floor(1,2, None), Arrow(2,2, None, angleType=AngleType.lright, rotationType=RotationType.up, thickType=ThickType.wide)],
    [Wire(0,3,None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.wide), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.wide)]
]

trap11 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Floor(0,1, None), Food(1,1, None), Floor(2,1, None)],
    [Arrow(0,2,None, angleType=AngleType.rright, rotationType=RotationType.up, thickType=ThickType.wide), Floor(1,2, None), Arrow(2,2, None, angleType=AngleType.lright, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Wire(0,3,None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.wide), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.skinny)]
]

trap12 = [
    [Arrow(0,0, None, angleType=AngleType.racute, rotationType=RotationType.up, thickType=ThickType.normal), Floor(1,0, None),  Floor(2,0, None)],
    [Wire(0,1,None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.normal), Food(1,1, None), Floor(2,1, None)],
    [Wire(0,2,None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.normal), Floor(1,2, None), Arrow(2,2, None, angleType=AngleType.lobtuse, rotationType=RotationType.up, thickType=ThickType.normal)],
    [Wire(0,3,None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.normal), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.normal)]
]

trap13 = [
    [Floor(0,0,None), Floor(1,0,None), Floor(2,0,None)],
    [Floor(0,1,None), Food(1,1, None), Floor(2,1,None)],
    [Floor(0,2,None), Floor(1,2,None), Floor(2,2,None)],
    [Arrow(0,3, None, angleType=AngleType.racute, rotationType=RotationType.left, thickType=ThickType.wide), Door(1,3,None), Wire(2,3, None, angleType=AngleType.lacute, rotationType=RotationType.right, thickType=ThickType.wide)]
]

trap14 = [
    [Floor(0,0,None), Floor(1,0,None), Arrow(2,0, None, angleType=AngleType.lacute, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Floor(0,1, None), Food(1,1, None), Wire(2,1, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Arrow(0,2,None, angleType=AngleType.racute, rotationType=RotationType.up, thickType=ThickType.skinny), Floor(1,2, None), Wire(2,2, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Wire(0,3,None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.skinny), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.skinny)]
]

trap15 = [
    [Floor(0,0,None), Floor(1,0,None), Floor(2,0,None)],
    [Floor(0,1,None), Food(1,1, None), Floor(2,1,None)],
    [Arrow(0,2, None, angleType=AngleType.robtuse, rotationType=RotationType.up, thickType=ThickType.normal), Floor(1,2,None), Arrow(2,2, None, angleType=AngleType.lacute, rotationType=RotationType.up, thickType=ThickType.wide)],
    [Wire(0,3, None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.normal), Door(1,3,None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.wide)]
]

traps = [trap0, trap1, trap2, trap3, trap4, trap5, trap6, trap7, trap8, trap9, trap10, trap11, trap12, trap13, trap14, trap15]