# Sets up new array for plotting
earthquakePlot = np.copy(earthquake)

# Normalizes block positions relative to their equilibrium positions
for n in range(1, blockNum + 1):
    for m in range(0, maxTimeSteps):
        earthquakePlot[m,n] += -n + 1