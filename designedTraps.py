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

#same as 8?
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

#same as 4?
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
    [Arrow(0,3, None, angleType=AngleType.racute, rotationType=RotationType.left, thickType=ThickType.wide), Door(1,3,None), Arrow(2,3, None, angleType=AngleType.lacute, rotationType=RotationType.right, thickType=ThickType.wide)]
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

# !! mor trapz !!
trap16 = [
    [Floor(0,0,None), Floor(1,0,None), Floor(2,0,None)],
    [Floor(0,1,None), Food(1,1, None), Floor(2,1,None)],
    [Arrow(0,2, None, angleType=AngleType.robtuse, rotationType=RotationType.up, thickType=ThickType.wide), Floor(1,2,None), Arrow(2,2, None, angleType=AngleType.lobtuse, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Wire(0,3, None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.wide), Door(1,3,None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.skinny)]
]

trap17 = [
    [Floor(0,0,None), Floor(1,0,None), Floor(2,0,None)],
    [Floor(0,1,None), Food(1,1, None), Floor(2,1,None)],
    [Floor(0,2, None), Floor(1,2,None), Floor(2,2, None)],
    [Arrow(0,3, None, angleType=AngleType.racute, rotationType=RotationType.left, thickType=ThickType.normal), Door(1,3,None), Arrow(2,3, None, angleType=AngleType.lacute, rotationType=RotationType.right, thickType=ThickType.normal)]
]

trap18 = [
    [Floor(0,0,None), Floor(1,0,None), Floor(2,0,None)],
    [Floor(0,1,None), Food(1,1, None), Floor(2,1,None)],
    [Floor(0,2, None), Floor(1,2,None), Floor(2,2, None)],
    [Arrow(0,3, None, angleType=AngleType.racute, rotationType=RotationType.left, thickType=ThickType.skinny), Door(1,3,None), Arrow(2,3, None, angleType=AngleType.lacute, rotationType=RotationType.right, thickType=ThickType.skinny)]
]

trap19 = [
    [Arrow(0,0, None, angleType=AngleType.racute, rotationType=RotationType.up, thickType=ThickType.wide), Floor(1,0, None),  Floor(2,0, None)],
    [Wire(0,1,None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.wide), Food(1,1, None), Floor(2,1, None)],
    [Wire(0,2,None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.wide), Floor(1,2, None), Arrow(2,2, None, angleType=AngleType.lright, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Wire(0,3,None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.wide), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.skinny)]
]

trap20 = [
    [Wire(0,0, None, angleType=AngleType.racute, rotationType=RotationType.up, thickType=ThickType.skinny), Wire(1,0, None, angleType=AngleType.straight, rotationType=RotationType.right, thickType=ThickType.skinny),  Arrow(2,0, None, angleType=AngleType.racute, rotationType=RotationType.right, thickType=ThickType.skinny)],
    [Wire(0,1,None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.skinny), Food(1,1, None), Floor(2,1, None)],
    [Wire(0,2,None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.skinny), Floor(1,2, None), Arrow(2,2, None, angleType=AngleType.lright, rotationType=RotationType.up, thickType=ThickType.wide)],
    [Wire(0,3,None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.skinny), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.wide)]
]

trap21 = [
    [Wire(0,0, None, angleType=AngleType.racute, rotationType=RotationType.up, thickType=ThickType.wide), Wire(1,0, None, angleType=AngleType.straight, rotationType=RotationType.right, thickType=ThickType.wide),  Arrow(2,0, None, angleType=AngleType.racute, rotationType=RotationType.right, thickType=ThickType.wide)],
    [Wire(0,1,None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.wide), Food(1,1, None), Arrow(2,1, None, angleType=AngleType.lright, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Wire(0,2,None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.wide), Floor(1,2, None), Wire(2,2, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Wire(0,3,None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.wide), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.skinny)]
]

trap22 = [
    [Wire(0,0, None, angleType=AngleType.racute, rotationType=RotationType.up, thickType=ThickType.normal), Wire(1,0, None, angleType=AngleType.straight, rotationType=RotationType.right, thickType=ThickType.normal),  Arrow(2,0, None, angleType=AngleType.racute, rotationType=RotationType.right, thickType=ThickType.normal)],
    [Wire(0,1,None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.normal), Food(1,1, None), Floor(2,1, None)],
    [Wire(0,2,None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.normal), Floor(1,2, None), Floor(2,2, None)],
    [Wire(0,3,None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.normal), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lacute, rotationType=RotationType.right, thickType=ThickType.normal)]
]

trap23 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Floor(0,1, None), Food(1,1, None), Arrow(2,1, None, angleType=AngleType.lright, rotationType=RotationType.up, thickType=ThickType.normal)],
    [Arrow(0,2,None, angleType=AngleType.rright, rotationType=RotationType.up, thickType=ThickType.wide), Floor(1,2, None), Wire(2,2, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.normal)],
    [Wire(0,3,None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.wide), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.normal)]
]

trap24 = [
    [Floor(0,0, None), Floor(1,0, None), Arrow(2,0, None, angleType=AngleType.lacute, rotationType=RotationType.up, thickType=ThickType.wide)],
    [Floor(0,1, None), Food(1,1,None), Wire(2,1, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.wide)],
    [Floor(0,2, None), Floor(1,2,None), Wire(2,2,None,angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.wide)],
    [Arrow(0,3, None, angleType=AngleType.racute, rotationType=RotationType.left, thickType=ThickType.skinny), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.wide)]
]

trap25 = [
    [Floor(0,0, None), Floor(1,0, None), Arrow(2,0, None, angleType=AngleType.lacute, rotationType=RotationType.up, thickType=ThickType.normal)],
    [Floor(0,1, None), Food(1,1,None), Wire(2,1, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.normal)],
    [Floor(0,2, None), Floor(1,2,None), Wire(2,2,None,angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.normal)],
    [Arrow(0,3, None, angleType=AngleType.racute, rotationType=RotationType.left, thickType=ThickType.wide), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.normal)]
]

trap26 = [
    [Floor(0,0, None), Floor(1,0, None), Arrow(2,0, None, angleType=AngleType.lacute, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Floor(0,1, None), Food(1,1,None), Wire(2,1, None, angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Floor(0,2, None), Floor(1,2,None), Wire(2,2,None,angleType=AngleType.straight, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Arrow(0,3, None, angleType=AngleType.racute, rotationType=RotationType.left, thickType=ThickType.normal), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.skinny)]
]

trap27 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Floor(0,1, None), Food(1,1,None), Floor(2,1, None)],
    [Arrow(0,2, None, angleType=AngleType.robtuse, rotationType=RotationType.up, thickType=ThickType.normal), Floor(1,2,None), Arrow(2,2,None,angleType=AngleType.lobtuse, rotationType=RotationType.up, thickType=ThickType.normal)],
    [Wire(0,3, None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.normal), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.normal)]
]

trap28 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Floor(0,1, None), Food(1,1,None), Floor(2,1, None)],
    [Arrow(0,2, None, angleType=AngleType.robtuse, rotationType=RotationType.up, thickType=ThickType.skinny), Floor(1,2,None), Arrow(2,2,None,angleType=AngleType.lobtuse, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Wire(0,3, None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.skinny), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.skinny)]
]

trap29 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Floor(0,1, None), Food(1,1,None), Floor(2,1, None)],
    [Arrow(0,2, None, angleType=AngleType.robtuse, rotationType=RotationType.up, thickType=ThickType.wide), Floor(1,2,None), Arrow(2,2,None,angleType=AngleType.lobtuse, rotationType=RotationType.up, thickType=ThickType.wide)],
    [Wire(0,3, None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.wide), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.wide)]
]

trap30 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Floor(0,1, None), Food(1,1,None), Floor(2,1, None)],
    [Arrow(0,2, None, angleType=AngleType.rright, rotationType=RotationType.up, thickType=ThickType.skinny), Floor(1,2,None), Arrow(2,2,None,angleType=AngleType.lright, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Wire(0,3, None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.skinny), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.skinny)]
]

trap31 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Floor(0,1, None), Food(1,1,None), Floor(2,1, None)],
    [Arrow(0,2, None, angleType=AngleType.rright, rotationType=RotationType.up, thickType=ThickType.normal), Floor(1,2,None), Arrow(2,2,None,angleType=AngleType.lright, rotationType=RotationType.up, thickType=ThickType.normal)],
    [Wire(0,3, None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.normal), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.normal)]
]

trap32 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Floor(0,1, None), Food(1,1,None), Floor(2,1, None)],
    [Arrow(0,2, None, angleType=AngleType.rright, rotationType=RotationType.up, thickType=ThickType.wide), Floor(1,2,None), Arrow(2,2,None,angleType=AngleType.lright, rotationType=RotationType.up, thickType=ThickType.wide)],
    [Wire(0,3, None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.wide), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.wide)]
]

trap33 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Floor(0,1, None), Food(1,1,None), Floor(2,1, None)],
    [Arrow(0,2, None, angleType=AngleType.rright, rotationType=RotationType.up, thickType=ThickType.normal), Floor(1,2,None), Arrow(2,2,None,angleType=AngleType.lright, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Wire(0,3, None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.normal), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.skinny)]
]

trap34 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Floor(0,1, None), Food(1,1,None), Floor(2,1, None)],
    [Arrow(0,2, None, angleType=AngleType.rright, rotationType=RotationType.up, thickType=ThickType.normal), Floor(1,2,None), Arrow(2,2,None,angleType=AngleType.lacute, rotationType=RotationType.up, thickType=ThickType.wide)],
    [Wire(0,3, None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.normal), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.wide)]
]

trap35 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Floor(0,1, None), Food(1,1,None), Floor(2,1, None)],
    [Arrow(0,2, None, angleType=AngleType.rright, rotationType=RotationType.up, thickType=ThickType.normal), Floor(1,2,None), Arrow(2,2,None,angleType=AngleType.lacute, rotationType=RotationType.up, thickType=ThickType.normal)],
    [Wire(0,3, None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.normal), Door(1,3, None), Wire(2,3, None, angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.normal)]
]

# TODO: make these 4 traps
# traps 36, 37, 38, and 39 have not been made
    # sometimes buildings don't have a 13th floor either
# I think I lost my train of thought before moving onto one arrow traps... reminder do this @clay


## Many permutations in tinnyyy increments each time of working one arrow traps:

# yes we skipped four traps to trap 40. my b--- see above comment
trap40 = [
    [Floor(0,0,None), Floor(1,0,None), Floor(2,0,None)],
    [Floor(0,1,None), Food(1,1, None), Floor(2,1,None)],
    [Floor(0,2,None), Floor(1,2,None), Floor(2,2,None)],
    [Floor(0,3, None), Door(1,3,None), Arrow(2,3, None, angleType=AngleType.lacute, rotationType=RotationType.right, thickType=ThickType.skinny)]
]

trap41 = [
    [Floor(0,0,None), Floor(1,0,None), Floor(2,0,None)],
    [Floor(0,1,None), Food(1,1, None), Floor(2,1,None)],
    [Floor(0,2,None), Floor(1,2,None), Floor(2,2,None)],
    [Arrow(0,3, None, angleType=AngleType.racute, rotationType=RotationType.left, thickType=ThickType.skinny), Door(1,3,None), Floor(2,3, None)]
]

trap42 = [
    [Floor(0,0,None), Floor(1,0,None), Floor(2,0,None)],
    [Floor(0,1,None), Food(1,1, None), Floor(2,1,None)],
    [Floor(0,2,None), Floor(1,2,None), Floor(2,2,None)],
    [Arrow(0,3, None, angleType=AngleType.racute, rotationType=RotationType.left, thickType=ThickType.normal), Door(1,3,None), Floor(2,3, None)]
]

trap43 = [
    [Floor(0,0,None), Floor(1,0,None), Floor(2,0,None)],
    [Floor(0,1,None), Food(1,1, None), Floor(2,1,None)],
    [Floor(0,2,None), Floor(1,2,None), Floor(2,2,None)],
    [Floor(0,3, None), Door(1,3,None), Arrow(2,3, None, angleType=AngleType.lacute, rotationType=RotationType.right, thickType=ThickType.normal)]
]

trap44 = [
    [Floor(0,0,None), Floor(1,0,None), Floor(2,0,None)],
    [Floor(0,1,None), Food(1,1, None), Floor(2,1,None)],
    [Floor(0,2,None), Floor(1,2,None), Floor(2,2,None)],
    [Arrow(0,3, None, angleType=AngleType.racute, rotationType=RotationType.left, thickType=ThickType.wide), Door(1,3,None), Floor(2,3, None)]
]

trap45 = [
    [Floor(0,0,None), Floor(1,0,None), Floor(2,0,None)],
    [Floor(0,1,None), Food(1,1, None), Floor(2,1,None)],
    [Floor(0,2,None), Floor(1,2,None), Floor(2,2,None)],
    [Floor(0,3, None), Door(1,3,None), Arrow(2,3, None, angleType=AngleType.lacute, rotationType=RotationType.right, thickType=ThickType.wide)]
]

trap46 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Floor(0,1, None), Food(1,1, None), Floor(2,1, None)],
    [Arrow(0,2, None, angleType=AngleType.robtuse, rotationType=RotationType.up, thickType=ThickType.skinny), Floor(1,2, None), Floor(2,2, None)],
    [Wire(0,3, None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.skinny), Door(1,3, None), Floor(2,3, None)]
]

trap47 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Floor(0,1, None), Food(1,1, None), Floor(2,1, None)],
    [Arrow(0,2, None, angleType=AngleType.robtuse, rotationType=RotationType.up, thickType=ThickType.normal), Floor(1,2, None), Floor(2,2, None)],
    [Wire(0,3, None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.normal), Door(1,3, None), Floor(2,3, None)]
]

trap48 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Floor(0,1, None), Food(1,1, None), Floor(2,1, None)],
    [Arrow(0,2, None, angleType=AngleType.robtuse, rotationType=RotationType.up, thickType=ThickType.wide), Floor(1,2, None), Floor(2,2, None)],
    [Wire(0,3, None, angleType=AngleType.rright, rotationType=RotationType.left, thickType=ThickType.wide), Door(1,3, None), Floor(2,3, None)]
]

trap49 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Floor(0,1, None), Food(1,1, None), Floor(2,1, None)],
    [Floor(0,2, None), Floor(1,2, None), Arrow(2,2, None,angleType=AngleType.lobtuse, rotationType=RotationType.up, thickType=ThickType.skinny)],
    [Floor(0,3, None), Door(1,3, None), Wire(2,3, None,angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.skinny)]
]

trap50 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Floor(0,1, None), Food(1,1, None), Floor(2,1, None)],
    [Floor(0,2, None), Floor(1,2, None), Arrow(2,2, None,angleType=AngleType.lobtuse, rotationType=RotationType.up, thickType=ThickType.normal)],
    [Floor(0,3, None), Door(1,3, None), Wire(2,3, None,angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.normal)]
]

trap51 = [
    [Floor(0,0, None), Floor(1,0, None), Floor(2,0, None)],
    [Floor(0,1, None), Food(1,1, None), Floor(2,1, None)],
    [Floor(0,2, None), Floor(1,2, None), Arrow(2,2, None,angleType=AngleType.lobtuse, rotationType=RotationType.up, thickType=ThickType.wide)],
    [Floor(0,3, None), Door(1,3, None), Wire(2,3, None,angleType=AngleType.lright, rotationType=RotationType.right, thickType=ThickType.wide)]
]

## see #notes channel for ideas on one arrow traps 52 - 63

traps = [trap0, trap1, trap2, trap3, trap4, trap5, trap6, trap7, trap8, trap9, trap10, trap11, trap12, trap13, trap14, trap15]