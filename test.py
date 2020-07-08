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

# trapInfo = []
# for trapboard in dt.traps:
#     trap = Trap(3,4,trapboard)
#     ib, ac, gc, a, e = s.simulateTrap(trap, False)
#     trapInfo.append([ib, ac, gc])
# v.writeTojs(trapInfo)
#bins = [i for i in range(-10, 10)]

# def histProbEnter():
#     probList = []
#     #allTraps = e.trapEnumerator(3,4,3)
#     for trapboard in dt.traps:
#         trap = Trap(3,4,False,trapboard)
#         probEnter = int(alg.isTrap(trap, -0.25))
#         probList.append(probEnter)
#     plt.hist(probList)
#     plt.title("2.5, real traps")
#     plt.show()

# histProbEnter()

def histProbEnter(alg, real):
    probList = []
    if real:
        traps = [Trap(3,4,False,trapboard) for trapboard in dt.traps]
    else:
        print("Generating Traps")
        traps = e.trapEnumerator(3,4,4)
    num_traps = len(traps)
    for i in range(num_traps):
        e.printProgressBar(i+1,num_traps)
        trap = traps[i]
        probEnter = alg(trap)
        probList.append(probEnter)
    print(max(probList))
    plt.hist(probList)
    plt.title("Distribution of FSC for Traps\nReal: " + str(real))
    plt.show()

#histProbEnter(alg.isDoorArrow, True)
def histNumTraps(n):
    num_list = []
    for i in range(n):
        e.printProgressBar(i+1,n)
        data, trapInfo = e.simulate(e.pref)
        num_list.append(data["numTraps"])
    plt.hist(num_list)
    plt.title("Distribution of numTraps")
    plt.show()
#histNumTraps(10000)
#e.expectedLethality(3,4,3,500)

method = lambda trap: alg.functional_specified_complexity(alg.connectionsPerPiece(trap))
histProbEnter(method, False)



# method = lambda trap: 1 - (alg.trapDanger3(trap))**5
# histProbEnter(method, True)
#histNumTraps(10000)
# def lowFSCtraps():
#     trapInfo = []
#     for trapboard in dt.traps:
#         trap = Trap(3,4,False,trapboard)
#         if alg.isTrap(trap, 3.33) == False:
#             ib, ac, gc, a, e = s.simulateTrap(trap, False)
#             trapInfo.append([ib, ac, gc])
#     v.writeTojs(trapInfo)
#     print("done")

# lowFSCtraps()

#e.expectedLethality(3,4,3,100)
#e.runExperiment("testrun.csv", "defaultProbEnter", 100)

#histProbEnter(alg.gopherProbEnter3)


#e.saveCohesionValues(alg.trapDanger3, 3)

# probList = []
# allTraps = e.trapEnumerator(3, 4, 2)
# for trap in allTraps:
#     # c = alg.trapDanger3(trap)
#     # fsc = alg.fsc(c)
#     # probList.append(fsc)
#     probList.append(int(alg.isTrap(trap, alg.trapDanger3)))
# plt.hist(probList)
# plt.title("random")
# plt.show()

# probList = []
# for trapboard in dt.traps:
#     trap = Trap(3,4, True, trapboard)
#     # c = alg.trapDanger3(trap)
#     # fsc = alg.fsc(c)
#     # probList.append(fsc)
#     probList.append(int(alg.isTrap(trap, alg.trapDanger3)))
# plt.hist(probList)
# plt.title("real")
# plt.show()
#trap = Trap(3,4, True, dt.trap6)
#data, trapinfo = e.simulate(e.pref)
#print(alg.totalConnections(trap))

