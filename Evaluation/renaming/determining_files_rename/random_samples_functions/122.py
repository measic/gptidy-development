def function_def(earthquakes, blockNum, timeStep):
    """
    Produces a list of each earthquake and its magnitude
    
    Arguments:  earthquakes - the array containing all earthquake data
                blockNum - the number of blocks
                i - the block index to be examined
                
    Returned: a list containing the magnitude of each earthquake
    """
    quakes = []
    time = []
    count = 0
    quakeNum = -1
    dvOld = 0
    while count < len(earthquakes):
        dv = 0
        for i in range(0, blockNum):
            if dv < earthquakes[count, blockNum + i + 1]:
                dv = earthquakes[count, blockNum + i + 1]
        if dv > dvOld:
            quakeNum += 1
            quakes.append(0)
            time.append(earthquakes[count, 0])
            earthquakeLength = 0
            while dv > 0.0001 and count < len(earthquakes) - 1 and (earthquakeLength < 200):
                for i in range(0, blockNum):
                    quakes[quakeNum] += earthquakes[count, blockNum + i + 1] * timeStep
                count += 1
                dv = 0
                for i in range(0, blockNum):
                    if dv < earthquakes[count, blockNum + i + 1]:
                        dv = earthquakes[count, blockNum + i + 1]
                earthquakeLength += 1
        else:
            count += 1
        dvOld = dv
    return (time, quakes)