from classTrap import *
from classTerrain import *
import visualize as v
import simulation as s
import algorithms as alg
import matplotlib.pyplot as plt
import experiment as e




# enterProbs = []
# astats = []
# for i in range(50000):
#     trap = Trap(3,4, False)
#     ib, ac, gc, a, e = s.simulateTrap(trap, True)
#     astats.append(a)
#     printProgressBar(i+1, 50000)
# survival = sum(astats)/len(astats)
# print("\nGopher Survived (pct):", "{:.2f}".format(100 * survival), "+/-", "{:.3f}".format(196 * np.sqrt((survival * (1-survival))/len(astats))))
#ib, ac, gc = s.simulateTrap(trap, False)
#s.viewRun(ib,ac,gc)
#all data needed for visual stuff comes from here!
#v.visualRun(5,5, False, [[trap, 0, 0]])

#s.viewRun(nib, nac, ngc)
trapInfo = e.expectedLethality(3,3,4, 500)
terrainInfo = [[[]], []]
#v.writeTojs(trapInfo, terrainInfo)