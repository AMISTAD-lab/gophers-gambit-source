from classTrap import *
from classTerrain import *
import visualize as v
import simulation as s
import algorithms as alg
import matplotlib.pyplot as plt

enterProbs = []
astats = []
for i in range(6000):
    trap = Trap(3,4, True)
    ib, ac, gc, a = s.simulateTrap(trap, True)
    astats.append(a)
print(str(sum(astats)/len(astats)*100) + "%" + " alive")
#ib, ac, gc = s.simulateTrap(trap, False)
#s.viewRun(ib,ac,gc)
#all data needed for visual stuff comes from here!
#v.visualRun(5,5, False, [[trap, 0, 0]])

#s.viewRun(nib, nac, ngc)


