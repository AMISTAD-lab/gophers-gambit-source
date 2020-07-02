from classTrap import *
from classTerrain import *
import visualize as v
import simulation as s
import algorithms as alg
import matplotlib.pyplot as plt
import experiment as e
import designedTraps as dt

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
# trapInfo = e.expectedLethality(3,4,3, 500)
# terrainInfo = [[[]], []]

# trapInfo = []
# i = 0
# isKilled = True
# while len(trapInfo) < 10 or isKilled == True:
#     i += 1
#     data, trapInfo = e.simulate(e.pref)
#     isKilled = data["killedByHunger"]
# print(i)
# print(len(trapInfo))
# v.writeTojs(trapInfo)

trapInfo = []
for trapboard in dt.traps:
    trap = Trap(3,4,trapboard)
    ib, ac, gc, a, e = s.simulateTrap(trap, False)
    trapInfo.append([ib, ac, gc])
v.writeTojs(trapInfo)

# def histProbEnter(algorithm):
#     probList = []
#     allTraps = e.trapEnumerator(3, 4, 2)
#     for trap in allTraps:
#         #trap = Trap(3,4,trapboard)
#         probEnter = algorithm(trap)
#         probList.append(probEnter)
#     plt.hist(probList)
#     plt.show()

#e.expectedLethality(3,4,3,100)
#e.runExperiment("testrun.csv", "defaultProbEnter", 100)

#histProbEnter(alg.gopherProbEnter3)