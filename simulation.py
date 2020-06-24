from classTrap import *
from classTerrain import *

trap = Trap(3,4, False)
terrain = Terrain(10,10,[[trap, 1, 1, "hi"], [trap, 5, 0, "hi"]])
print(terrain)