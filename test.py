from classTrap import *
from classTerrain import *
import visualize as v
import simulation as s
import algorithms as alg
import matplotlib.pyplot as plt
import experiment as e


def printProgressBar (iteration, total, prefix = 'Progress:', suffix = 'Complete', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()


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
terraininfo, trapinfo = e.test()
v.writeTojs(terraininfo, trapinfo)