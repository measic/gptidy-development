blockPositions = []
testBlockPositions = []
averageSpacing = 1
kp = 40
kc = 250
mass = 1
variable_def = 50
v0 = 0.01
vBlock = 0
vf = 3.0
blockNum = 25
maxTimeSteps = 50000
minBLockV = 1e-08
timeStepShort = 0.005
timeStepLong = 1
variation = 0.001
for n in range(0, blockNum + 1):
    blockPositions.append(n * averageSpacing + (random.random() - 0.5) * 2 * variation)
    testBlockPositions.append(n)