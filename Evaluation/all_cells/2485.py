# model dimensions
nlay, nrow, ncol = 1, 1, 200
delr = 50.
delc = 1.

# boundary heads
h1 = 23.
h2 = 5.

# cell centroid locations
x = np.arange(0., float(ncol)*delr, delr) + delr / 2.

# ibound
ibound = np.ones((nlay, nrow, ncol), dtype=np.int)
ibound[:, :, 0] = -1
ibound[:, :, -1] = -1

# bottom of the model
botm = 25 * np.ones((nlay + 1, nrow, ncol), dtype=np.float)
base = 20.
for j in range(ncol):
    botm[1, :, j] = base
    #if j > 0 and j % 40 == 0:
    if j+1 in [40,80,120,160]:
        base -= 5

# starting heads
strt = h1 * np.ones((nlay, nrow, ncol), dtype=np.float)
strt[:, :, -1] = h2