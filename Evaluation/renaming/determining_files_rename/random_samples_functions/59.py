def function_def(f, n, blockPositions, vBlock, blockNum, h1, h2, maxPoints, minBlockV, *args, verbose=False):
    """ 
    Solve a coupled system of ODEs by Euler method with fixed number of steps.

    Arguements: f - function giving ODE as y'=f(x,y)
                n - the number of ODEs
                blockPositions - the array containging the initial block positions
                vBlock - initial block velocity
                blockNum - the number of blocks
                interval - tuple region (a,b) on which to solve ODE
                steps - number of steps
    
    Returned: An array containing the positions and velocies of the blocks over time
    """
    points = np.zeros((maxPoints, blockNum * 2 + 1))
    t = 0
    points[0, 0] = t
    count = 0
    for l in range(1, blockNum + 1):
        points[0, l] = blockPositions[count]
        count += 1
    for m in range(blockNum + 1, blockNum * 2 + 1):
        points[0, m] = vBlock
    count = 1
    dv = 0
    r = (0, 0)
    while points[maxPoints - 1, 0] == 0:
        if dv < minBlockV:
            h = h1
            while dv < minBlockV and points[maxPoints - 1, 0] == 0:
                if verbose == True:
                    print('h1:', t)
                oldBlockPositions = blockPositions
                t = t + h
                points[count, 0] = t
                dv = 0
                for i in range(0, blockNum):
                    r = np.array([points[count - 1, i + 1], points[count - 1, i + 1 + blockNum]])
                    r_new = r + h * f(t, blockPositions, r[1], i, blockNum, *args)
                    r = r_new
                    blockPositions[i] = r[0]
                    if r[1] > dv:
                        dv = r[1]
                    if verbose == True:
                        print(i, blockPositions[i], r[1], dv)
                    points[count, i + 1] = r[0]
                    points[count, i + 1 + blockNum] = r[1]
                count += 1
        elif points[maxPoints - 1, 0] == 0:
            h = h2
            t -= h1
            count -= 1
            blockPositions = oldBlockPositions
            dv = 0
            while dv < minBlockV and points[maxPoints - 1, 0] == 0:
                if verbose == True:
                    print('h2:', t)
                oldBlockPositions = blockPositions
                t = t + h
                points[count, 0] = t
                dv = 0
                for i in range(0, blockNum):
                    r = np.array([points[count - 1, i + 1], points[count - 1, i + 1 + blockNum]])
                    r_new = r + h * f(t, blockPositions, r[1], i, blockNum, *args)
                    r = r_new
                    blockPositions[i] = r[0]
                    if r[1] > dv:
                        dv = r[1]
                    if verbose == True:
                        print(i, blockPositions[i], r[1], dv)
                    points[count, i + 1] = r[0]
                    points[count, i + 1 + blockNum] = r[1]
                count += 1
            while dv >= minBlockV and points[maxPoints - 1, 0] == 0:
                if verbose == True:
                    print('h2:', t)
                oldBlockPositions = blockPositions
                t = t + h
                points[count, 0] = t
                dv = 0
                for i in range(0, blockNum):
                    r = np.array([points[count - 1, i + 1], points[count - 1, i + 1 + blockNum]])
                    r_new = r + h * f(t, blockPositions, r[1], i, blockNum, *args)
                    r = r_new
                    blockPositions[i] = r[0]
                    if r[1] > dv:
                        dv = r[1]
                    if verbose == True:
                        print(i, blockPositions[i], r[1], dv)
                    points[count, i + 1] = r[0]
                    points[count, i + 1 + blockNum] = r[1]
                count += 1
    return points