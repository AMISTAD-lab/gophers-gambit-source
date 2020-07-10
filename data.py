import csv
import copy
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats
import math as m

paramLabels = {
        "defaultProbEnter":r"Default Probability of Entering Trap",
        "probReal":r"Probability of Encountering a Designed Trap",
        "nTrapsWithoutFood":r"Maximum Fasting Interval",
        "maxProjectileStrength":r"Maximum Projectile Strength",
    }

def allDataToCSV(allData, filename):
    """takes in a data list obtained from simulateManySetups and writes all of the run information into a csv"""
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["BATCH #"] + ["RUN #"] + [key for key in allData[0]["runsData"][0]]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for batchIndex in range(len(allData)):
            batchData = allData[batchIndex]
            runsData = batchData["runsData"]
            for runIndex in range(len(runsData)):
                runDict = runsData[runIndex]
                runDict["BATCH #"] = batchIndex
                runDict["RUN #"] = runIndex
                writer.writerow(runDict)

def listStats(numList):
    """takes in a list of numbers and returns [average, standard deviation, 95% confidence interval]"""
    avg = stats.mean(numList)
    std = stats.stdev(numList)
    sem = std / m.sqrt(len(numList))
    z = 1.96 # 95% ci
    ci = (avg - z*sem, avg + z*sem)
    return [avg, std, ci]

def proportionStats(portion, total):
    p = portion / total
    ci = 196 * m.sqrt((p * (1-p))/total)
    p *= 100
    return p, (p-ci, p+ci)

def filterDataFrame(data, filterlist):
    data = copy.deepcopy(data)
    for param, value in filterlist:
        booleans = data[param] == value
        data = data[booleans]
    return data

def percentThoughtReal(filename, param):
    data = pd.read_csv(filename)
    data = filterDataFrame(data, [["intention", True]])
    for val, group in data.groupby(param):
        print(val)
        groupThoughtReal = 0
        groupTrapsPresentedWith = 0
        for index, gopher in group.iterrows():
            groupThoughtReal += gopher["numThoughtReal"]
            groupTrapsPresentedWith += gopher["numTraps"] + (gopher["status"] == 2) #if zapped, it saw one more trap than it survived
        print(groupThoughtReal / groupTrapsPresentedWith)
        print()


def linearRunGraph(filename, param):
    data = pd.read_csv(filename)
    plt.style.use('ggplot')
    plt.rc('font', family='serif')
        
    df0 = filterDataFrame(data, [["intention", True], ["cautious", False]])
    df1 = filterDataFrame(data, [["intention", False]])
    df3 = filterDataFrame(data, [["intention", True], ["cautious", True]])

    dfs = [df0, df1, df3]
    modes = [r"With Intention", r"Without Intention", r"Cautious"]

    colorIter = iter(['#4FADAC', '#5386A6', '#2F5373'])
    
    fig, axes = plt.subplots(1,3)
    life_ax, food_ax, n_food_ax = axes.flat
    plt.tight_layout(rect=[0.05,0.05,0.90, 0.90], h_pad=1)

    for i in range(3):
        df = dfs[i]
        paramValues = []

        trap_vals = []
        t_up_ci = []
        t_low_ci = []

        food_vals = []
        f_up_ci = []
        f_low_ci = []

        n_food_vals = []
        n_f_up_ci = []
        n_f_low_ci = []

        # alive_vals = []
        # starved_vals = []
        # zapped_vals = []

        for val, group in df.groupby(param):
            paramValues.append(val)

            group_vals = group["numTraps"]
            groupLifeTimes = []
            for numTraps in group_vals:
                numTraps = int(numTraps)
                groupLifeTimes.append(numTraps)
            avg, std, ci = listStats(groupLifeTimes)
            trap_vals.append(avg)
            t_low_ci.append(ci[0])
            t_up_ci.append(ci[1])

            group_vals = group["numFood"]
            groupNumFood = []
            for numFood in group_vals:
                numFood = int(numFood)
                groupNumFood.append(numFood)
            avg, std, ci = listStats(groupNumFood)
            food_vals.append(avg)
            f_low_ci.append(ci[0])
            f_up_ci.append(ci[1])
            
            groupFoodPerTrap = [groupNumFood[j] / groupLifeTimes[j] for j in range(len(groupNumFood)) if groupLifeTimes[j] != 0] #we discard when insufficient data
            avg, std, ci = listStats(groupFoodPerTrap)
            n_food_vals.append(avg)
            n_f_low_ci.append(ci[0])
            n_f_up_ci.append(ci[1])

            # group_vals = group["status"]
            # alive = 0
            # starved = 0
            # zapped = 0
            # for status in group_vals:
            #     if status == 0:
            #         alive += 1
            #     elif status == 1:
            #         starved += 1
            #     else:
            #         zapped += 1
            # total = alive + starved + zapped
            # p_a, ci = proportionStats(alive, total)
            # p_s, ci = proportionStats(starved, total)
            # p_z, ci = proportionStats(zapped, total)
            # alive_vals.append(p_a)
            # starved_vals.append(p_s)
            # zapped_vals.append(p_z)
           
        color = next(colorIter)
        life_ax.plot(paramValues, trap_vals, label=modes[i], color=color, linewidth=2)
        life_ax.fill_between(paramValues, t_low_ci, t_up_ci, color=color, alpha=.15)

        food_ax.plot(paramValues, food_vals, label=modes[i], color=color, linewidth=2)
        food_ax.fill_between(paramValues, f_low_ci, f_up_ci, color=color, alpha=.15)

        n_food_ax.plot(paramValues, n_food_vals, label=modes[i], color=color, linewidth=2)
        n_food_ax.fill_between(paramValues, n_f_low_ci, n_f_up_ci, color=color, alpha=.15) 

        #status_axs[i].stackplot(paramValues, alive_vals, starved_vals, zapped_vals, colors=["#267347", "#F27405", "#D92B04"], labels=[r"Alive", r"Starved", r"Zapped"])
    
    life_ax.set(ylim=(0, 50))
    life_ax.set_ylabel(r"Gopher Lifespan (number of traps)")
    life_ax.set_xlabel(paramLabels[param], fontsize=10)
    life_ax.tick_params(axis='both', which='major', labelsize=10, direction='in')
    life_ax.set_title(r"Gopher Lifespan" + "\n" + r"vs" + "\n" + paramLabels[param], fontsize=11)
    life_ax.legend()

    food_ax.set(ylim=(0, 50))
    food_ax.set_ylabel(r"Number of Food Consumed", fontsize=10)
    food_ax.set_xlabel(paramLabels[param], fontsize=10)
    food_ax.tick_params(axis='both', which='major', labelsize=10, direction='in')
    food_ax.set_title(r"Food Consumption" + "\n" + r"vs" + "\n" + paramLabels[param], fontsize=11)
    food_ax.legend()

    n_food_ax.set(ylim=(0, 1))
    n_food_ax.set_ylabel(r"Food Consumed Per Trap Survived", fontsize=10)
    n_food_ax.set_xlabel(paramLabels[param], fontsize=10)
    n_food_ax.tick_params(axis='both', which='major', labelsize=10, direction='in')
    n_food_ax.set_title(r"Normalized Food Consumption" + "\n" + r"vs" + "\n" + paramLabels[param], fontsize=11)
    n_food_ax.legend()

    # for ax in status_axs:
    #     ax.set(ylim=(0,100))
    #     ax.set(xlim=(min(paramValues), max(paramValues)))
    #     ax.set_ylabel(r"Gophers Status After 50 Traps (%)", fontsize=10)
    #     ax.set_xlabel(paramLabels[param], fontsize=10)
    #     ax.tick_params(axis='both', which='major', labelsize=10, direction='in')
    #     ax.legend()
    # status_ax1.set_title(r"Status vs " + paramLabels[param] + "\n" + r"With Intention", fontsize=11)
    # status_ax2.set_title(r"Status vs " + paramLabels[param] + "\n" + r"Without Intention", fontsize=11)
    plt.rc('text', usetex=True)
    plt.show()






def statusOverTime(filename):

    data = pd.read_csv(filename)
    plt.style.use('ggplot')
    plt.rc('font', family='serif')
        
    df0 = filterDataFrame(data, [["intention", True]])
    df1 = filterDataFrame(data, [["intention", False]])

    dfs = [df0, df1]
    modes = [r"With Intention Perception", r"Without Intention Perception"]

    fig, axes = plt.subplots(1,2)
    status_axs = axes.flat

    for i in range(2):
        x = [t for t in range(1, 51)]
        alive = [0]*50
        starved = [0]*50
        zapped = [0]*50

        for index, gopher in dfs[i].iterrows():
            numTraps = int(gopher["numTraps"])
            status = int(gopher["status"])
            for j in range(numTraps):
                alive[j] += 1
            if status != 0:
                if status == 1:
                    dead_list = starved
                else:
                    dead_list = zapped
                for j in range(numTraps, 50):
                    dead_list[j] += 1

        total = alive[0] + starved[0] + zapped[0]
        alive = [a / total * 100 for a in alive]
        starved = [s / total * 100 for s in starved]
        zapped = [z / total * 100 for z in zapped]

        status_axs[i].stackplot(x, alive, starved, zapped, colors=["#267347", "#F27405", "#D92B04"], labels=[r"Alive", r"Starved", r"Zapped"])

    for ax in status_axs:
        ax.set(ylim=(0,100))
        ax.set(xlim=(1, 50))
        ax.set_ylabel(r"Gophers Status (%)", fontsize=10)
        ax.set_xlabel(r"Time (# of Traps Seen)", fontsize=10)
        ax.tick_params(axis='both', which='major', labelsize=10, direction='in')
        ax.legend()
    status_axs[0].set_title(r"Status Over Time" + "\n" + r"With Intention Perception", fontsize=11)
    status_axs[1].set_title(r"Status Over Time" + "\n" + r"Without Intention Perception", fontsize=11)

    plt.rc('text', usetex=True)
    plt.show()