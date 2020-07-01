import csv

def allDataToCSV(allData, filename):
    """takes in a data list obtained from simulateManySetups and writes all of the run information into a csv"""
    with open(filename, 'w', newline='') as csvfile:
        print([key for key in allData[0]["runsData"][0]])
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